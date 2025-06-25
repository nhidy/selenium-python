import random

from webui_test.running.config import F8Config
from webui_test.case import *

class FormAction(TestCase):

# -------------------------- handle FO - CUSTOMER --------------------------
    # CTM_APR: Approve customer
    def ctm_apr(self, customer_code, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.open_fo('CTM_APR', 'Approve customer')
        self.wait_for_button_available('Accept')
        self.assert_form_title('Approve customer')
        # enter value
        self.fo_write('Customer code', str(customer_code).replace('-', ''))
        self.wait_loading()
        self.fo_write_text('Description', 'AUTO TEST')
        if ifc_codes:
            self.add_fees(ifc_codes, values, total_fee)
        # click 'Accept'
        self.click_button('Accept')
        # approve
        if approve_later=='Y':
            self.click_button('Later')
        if approve_on_form=='Y':
            self.fo_approve_in_popup(
                username=username,
                password=password,
                reason=reason
            )
        if list_error_message:
        # verify error
            self.assert_error_message()
            self.assert_list_error_message(list_error_message)
            print('Transaction failed!')
        else:
        # verify success
            self.assert_button_disable('Accept')
            self.assert_notification("Saved successfully!")
            if expected_posting:
                self.assert_posting_data(**expected_posting)
            transaction_references=self.fo_get_text('Transaction references')
            print(f'Transaction references CTM_APR: {transaction_references}')
            customer_code_mask=self.fo_get_value('Customer code')
            print(f'Customer code: {customer_code_mask}')
            return transaction_references, customer_code_mask

    # CTM_CCN: Change customer name
    def ctm_ccn(self, customer_code, new_first_name_en=None, new_last_name_en=None, new_father_name=None, new_full_name=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.open_fo('CTM_CCN', 'Change customer name')
        self.wait_for_button_available('Accept')
        self.assert_form_title('Change Customer Name')
        # enter value
        self.fo_write('Customer code', str(customer_code).replace('-', ''))
        self.wait_loading()
        if new_first_name_en:
            self.fo_write_text('New First Name (en)', new_first_name_en)
        if new_last_name_en:
            self.fo_write_text('New Last Name (en)', new_last_name_en)
        if new_father_name:
            self.fo_write_text('New Father Name', new_father_name)
        if new_full_name:
            self.fo_assert_text('New Full Name', new_full_name)
        if ifc_codes:
            self.add_fees(ifc_codes, values, total_fee)
        self.fo_write_text('Description', 'AUTO TEST')
        # click 'Accept'
        self.click_button('Accept')
        # approve
        if approve_later=='Y':
            self.click_button('Later')
        if approve_on_form=='Y':
            self.fo_approve_in_popup(
                username=username,
                password=password,
                reason=reason
            )
        if list_error_message:
        # verify error
            self.assert_error_message()
            self.assert_list_error_message(list_error_message)
            print('Transaction failed!')
        else:
        # verify success
            self.assert_button_disable('Accept')
            self.assert_notification("Saved successfully!")
            if expected_posting:
                self.assert_posting_data(**expected_posting)
            transaction_references=self.fo_get_text('Transaction references')
            print(f'Transaction references CTM_CCN: {transaction_references}')
            customer_code_mask=self.fo_get_value('Customer code')
            print(f'Customer code: {customer_code_mask}')
            return transaction_references, customer_code_mask

    # CTM_CPN: Change customer paper number
    def ctm_cpn(self, customer_code, paper_type, paper_number, state=None, district=None, type=None, registration_no=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.open_fo('CTM_CPN', 'Change customer paper number')
        self.wait_for_button_available('Accept')
        self.assert_form_title('Change Customer Paper Number')
        # enter value
        self.fo_write('Customer code', str(customer_code).replace('-', ''))
        self.wait_loading()
        self.fo_write_text('Description', 'AUTO TEST')
        self.fo_select('Paper type', paper_type)
        if state:
            self.fo_select('State', state)
        if district:
            self.fo_select('District', district)
        if type:
            self.fo_select('Type', type)
        if registration_no:
            self.fo_select('Registration No', registration_no)
        if paper_type=='NRC':
            self.fo_assert_text('Paper number', paper_number)
        if paper_type!='NRC':
            self.fo_write_text('Paper number', paper_number)
        if ifc_codes:
            self.add_fees(ifc_codes, values, total_fee)
        # click 'Accept'
        self.click_button('Accept')
        # approve
        if approve_later=='Y':
            self.click_button('Later')
        if approve_on_form=='Y':
            self.fo_approve_in_popup(
                username=username,
                password=password,
                reason=reason
            )
        if list_error_message:
        # verify error
            self.assert_error_message()
            self.assert_list_error_message(list_error_message)
            print('Transaction failed!')
        else:
        # verify success
            self.assert_button_disable('Accept')
            self.assert_notification("Saved successfully!")
            if expected_posting:
                self.assert_posting_data(**expected_posting)
            transaction_references=self.fo_get_text('Transaction references')
            print(f'Transaction references CTM_CPN: {transaction_references}')
            customer_code_mask=self.fo_get_value('Customer code')
            print(f'Customer code: {customer_code_mask}')
            return transaction_references, customer_code_mask

    #  CTM_CAS: Change customer status
    def ctm_cas(self, customer_code, new_status, current_status=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.open_fo('CTM_CAS', 'Change customer status')
        self.wait_for_button_available('Accept')
        self.assert_form_title('Change customer status')
        # enter value
        self.fo_write_group('Customer code', str(customer_code).replace('-', ''))
        self.wait_loading()
        self.fo_write_text('Description', 'AUTO TEST')
        self.fo_select('New status', new_status)
        if current_status:
            self.fo_assert_select('Current status', current_status)
        if ifc_codes:
            self.add_fees(ifc_codes, values, total_fee)
        # click 'Accept'
        self.click_button('Accept')
        # approve
        if approve_later=='Y':
            self.click_button('Later')
        if approve_on_form=='Y':
            self.fo_approve_in_popup(
                username=username,
                password=password,
                reason=reason
            )
        if list_error_message:
        # verify error
            self.assert_error_message()
            self.assert_list_error_message(list_error_message)
            print('Transaction failed!')
        else:
        # verify success
            self.assert_button_disable('Accept')
            self.assert_notification("Saved successfully!")
            if expected_posting:
                self.assert_posting_data(**expected_posting)
            transaction_references=self.fo_get_text('Transaction references')
            print(f'Transaction references CTM_CAS: {transaction_references}')
            customer_code_mask=self.fo_get_value_group('Customer code')
            print(f'Customer code: {customer_code_mask}')
            return transaction_references, customer_code_mask

# -------------------------- handle FO - DEPOSIT --------------------------
    # DPT_OPN: 1100: Open new deposit account
    # def dpt_opn(self, customer_code, customer_type, catalogue_code, reason_of_account_opening, catalogue_name=None, deposit_type=None, deposit_sub_type=None, deposit_purpose=None, account_holder_name=None, rollover_option=None, auto_transfer_option=None, relation_customers=None, customer_segmentation=None, business_purpose_code=None, agent_hub_referral=None, employer_organization_name=None, relationship_manager=None, to_account_number=None, i_m_banking=False, mpu_card=False, passbook_cheque_book=False, wallet=False, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
    #     # open form
    #     self.close_all_form()
    #     self.open_fo('DPT_OPN', 'Open')
    #     self.wait_for_button_available('Accept')
    #     self.assert_form_title('1100: Open new deposit account')
    #     # enter value
    #     self.fo_write('Customer code', customer_code)
    #     self.fo_select('Customer type', customer_type)
    #     self.fo_write('Catalogue code', catalogue_code)
    #     if catalogue_name:
    #         self.fo_assert_text('Catalogue name', catalogue_name)
    #     if deposit_type:
    #         self.fo_assert_text('Deposit type', deposit_type)
    #     if deposit_sub_type:
    #         self.fo_assert_select('Deposit sub type', deposit_sub_type)
    #     if deposit_purpose:
    #         self.fo_assert_select('Deposit purpose', deposit_purpose)
    #     if account_holder_name:
    #         self.fo_assert_text('Account holder name', account_holder_name)
    #     if rollover_option:
    #         self.fo_assert_select('Rollover option', rollover_option)
    #     if auto_transfer_option:
    #         self.fo_assert_select('Auto transfer option', auto_transfer_option)
    #     if relation_customers:
    #         self.fo_select_multi('Relation customers', relation_customers)
    #     if agent_hub_referral:
    #         self.fo_write_group('Agent hub referral', agent_hub_referral)
    #     if customer_segmentation:
    #         self.fo_select('Customer segmentation', customer_segmentation)
    #     if business_purpose_code:
    #         self.fo_write_text_group('Business Purpose Code', business_purpose_code)
    #     self.fo_write_text('Reason of Account Opening', reason_of_account_opening)
    #     if employer_organization_name:
    #         self.fo_write_text('Employer Organization Name', employer_organization_name)
    #     self.key_escape()
    #     if relationship_manager:
    #         self.fo_select('Relationship Manager', relationship_manager)
    #     self.fo_write_text('Description', 'AUTO TEST')
    #     if to_account_number:
    #         self.fo_write_group('To Account number', to_account_number)
    #     if i_m_banking:
    #         self.fo_click_checkbox('I/M Banking')
    #     if mpu_card:
    #         self.fo_click_checkbox('MPU Card')
    #     if passbook_cheque_book:
    #         self.fo_click_checkbox('Passbook/Cheque Book')
    #     if wallet:
    #         self.fo_click_checkbox('Wallet')
    #     if ifc_codes:
    #         self.add_fees(ifc_codes, values, total_fee)
    #     self.fo_click_checkbox('Caution!  There is no doubt that banks may be used as a means of Money Laundering/ Terrorist Financing/ Proliferation of Weapons of Mass Destruction.')
    #     # click 'Accept'
    #     self.click_button('Accept')
    #     # approve
    #     if approve_later=='Y':
    #         self.click_button('Later')
    #     if approve_on_form=='Y':
    #         self.fo_approve_in_popup(
    #             username=username,
    #             password=password,
    #             reason=reason
    #         )
    #     if list_error_message:
    #     # verify error
    #         self.assert_error_message()
    #         self.assert_list_error_message(list_error_message)
    #         print('Transaction failed!')
    #     else:
    #     # verify success
    #         self.assert_button_disable('Accept')
    #         self.assert_notification('Saved successfully!')
    #         if expected_posting:
    #             self.assert_posting_data(**expected_posting)
    #         transaction_references=self.fo_get_text('Transaction references')
    #         print(f'Transaction references DPT_OPN: {transaction_references}')
    #         deposit_account_mask=self.fo_get_value_group('Account number')
    #         print(f'Account number: {deposit_account_mask}')
    #         return transaction_references, deposit_account_mask

    def dpt_opn(self, customer_type=None, customer_code=None, relation_customers=None, catalogue_code=None, customer_segmentation=None, business_purpose_code=None, to_account_number=None, agent_hub_referral=None, employer_organization_name=None, reason_of_account_opening=None, relationship_manager=None, description=None, im_banking=None, mpu_card=None, passbookcheque_book=None, wallet=None, account_number=None, catalogue_name=None, deposit_type=None, deposit_sub_type=None, deposit_purpose=None, account_holder_name=None, rollover_option=None, auto_transfer_option=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.open_fo('DPT_OPN', '1100: Open new deposit account')
        self.wait_for_button_available('Accept')
        self.assert_form_title('1100: Open new deposit account')
        # enter value
        self.key_escape()
        if customer_type:
            self.fo_select('Customer type', customer_type)
        if customer_code:
            self.fo_write('Customer code', customer_code)
        self.key_escape()
        if relation_customers:
            self.fo_select_multi('Relation customers', relation_customers)
        if catalogue_code:
            self.fo_write('Catalogue code', catalogue_code)
        self.key_escape()
        if customer_segmentation:
            self.fo_select('Customer segmentation', customer_segmentation)
        if business_purpose_code:
            self.fo_write_text_group('Business Purpose Code', business_purpose_code)
        if to_account_number:
            self.fo_write_group('To Account number', to_account_number)
        if agent_hub_referral:
            self.fo_write_group('Agent hub referral', agent_hub_referral)
        if employer_organization_name:
            self.fo_write_text('Employer Organization Name', employer_organization_name)
        if reason_of_account_opening:
            self.fo_write_text('Reason of Account Opening', reason_of_account_opening)
        self.key_escape()
        if relationship_manager:
            self.fo_select('Relationship Manager', relationship_manager)
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_write_text('Description', description)
        if im_banking is None or im_banking == '':
            im_banking = False
        if im_banking:
            self.fo_click_checkbox('I/M Banking')
        if mpu_card is None or mpu_card == '':
            mpu_card = False
        if mpu_card:
            self.fo_click_checkbox('MPU Card')
        if passbookcheque_book is None or passbookcheque_book == '':
            passbookcheque_book = False
        if passbookcheque_book:
            self.fo_click_checkbox('Passbook/Cheque Book')
        if wallet is None or wallet == '':
            wallet = False
        if wallet:
            self.fo_click_checkbox('Wallet')
        if account_number:
            self.fo_assert_value_group('Account number', account_number)
        if catalogue_name:
            self.fo_assert_text('Catalogue name', catalogue_name)
        if deposit_type:
            self.fo_assert_text('Deposit type', deposit_type)
        if deposit_sub_type:
            self.fo_assert_select('Deposit sub type', deposit_sub_type)
        if deposit_purpose:
            self.fo_assert_select('Deposit purpose', deposit_purpose)
        if account_holder_name:
            self.fo_assert_text('Account holder name', account_holder_name)
        if rollover_option:
            self.fo_assert_select('Rollover option', rollover_option)
        if auto_transfer_option:
            self.fo_assert_select('Auto transfer option', auto_transfer_option)
        self.wait_loading()
        self.fo_click_checkbox('Caution!  There is no doubt that banks may be used as a means of Money Laundering/ Terrorist Financing/ Proliferation of Weapons of Mass Destruction.')
        self.wait_loading()
        # click 'Accept'
        self.click_button('Accept')
        # approve
        if approve_later=='Y':
            self.click_button('Later')
        if approve_on_form=='Y':
            self.fo_approve_in_popup(
                username=username,
                password=password,
                reason=reason
            )
        if list_error_message:
        # verify error
            self.assert_error_message()
            self.assert_list_error_message(list_error_message)
            print('Transaction failed!')
        else:
        # verify success
            self.assert_button_disable('Accept')
            self.switch_to_core_banking()
            self.assert_notification('Saved successfully!')
            self.close_voucher()
            if expected_posting:
                self.assert_posting_data(**expected_posting)
            transaction_references=self.fo_get_text('Transaction references')
            print(f'Transaction references DPT_OPN: {transaction_references}')
            account_number_out=self.fo_get_value_group('Account number')
            print(f'Account number: {account_number_out}')
            return transaction_references, account_number_out

    def dpt_opn_view(self, transaction_references, customer_type=None, customer_code=None, catalogue_code=None, business_purpose_code=None, agent_hub_referral=None, employer_organization_name=None, reason_of_account_opening=None, relationship_manager=None, description=None, im_banking=None, mpu_card=None, passbookcheque_book=None, wallet=None, account_number=None, relation_customers=None, catalogue_name=None, deposit_type=None, deposit_sub_type=None, deposit_purpose=None, customer_segmentation=None, account_holder_name=None, rollover_option=None, auto_transfer_option=None, to_account_number=None, expected_posting=None):
        self.transaction_view(transaction_references, '1100: Open new deposit account')
        # compare value
        if customer_type:
            self.fo_assert_select('Customer type', customer_type)
        if customer_code:
            self.fo_assert_value('Customer code', self.customer_code_mask(customer_code))
        if catalogue_code:
            self.fo_assert_value('Catalogue code', catalogue_code)
        if business_purpose_code:
            self.fo_assert_text_group('Business Purpose Code', business_purpose_code)
        if agent_hub_referral:
            self.fo_assert_value_group('Agent hub referral', agent_hub_referral)
        if employer_organization_name:
            self.fo_assert_text('Employer Organization Name', employer_organization_name)
        if reason_of_account_opening:
            self.fo_assert_text('Reason of Account Opening', reason_of_account_opening)
        if relationship_manager:
            self.fo_assert_select('Relationship Manager', relationship_manager)
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_assert_text('Description', description)
        if im_banking is None or im_banking == '':
            im_banking = False
        if im_banking is not None or im_banking != '':
            self.fo_assert_checkbox('I/M Banking', im_banking)
        if mpu_card is None or mpu_card == '':
            mpu_card = False
        if mpu_card is not None or mpu_card != '':
            self.fo_assert_checkbox('MPU Card', mpu_card)
        if passbookcheque_book is None or passbookcheque_book == '':
            passbookcheque_book = False
        if passbookcheque_book is not None or passbookcheque_book != '':
            self.fo_assert_checkbox('Passbook/Cheque Book', passbookcheque_book)
        if wallet is None or wallet == '':
            wallet = False
        if wallet is not None or wallet != '':
            self.fo_assert_checkbox('Wallet', wallet)
        if account_number:
            self.fo_assert_value_group('Account number', self.deposit_account_number_mask(account_number))
        if relation_customers:
            self.fo_assert_select_multi('Relation customers', relation_customers)
        if catalogue_name:
            self.fo_assert_text('Catalogue name', catalogue_name)
        if deposit_type:
            self.fo_assert_text('Deposit type', deposit_type)
        if deposit_sub_type:
            self.fo_assert_select('Deposit sub type', deposit_sub_type)
        if deposit_purpose:
            self.fo_assert_select('Deposit purpose', deposit_purpose)
        if customer_segmentation:
            self.fo_assert_select('Customer segmentation', customer_segmentation)
        if account_holder_name:
            self.fo_assert_text('Account holder name', account_holder_name)
        if rollover_option:
            self.fo_assert_select('Rollover option', rollover_option)
        if auto_transfer_option:
            self.fo_assert_select('Auto transfer option', auto_transfer_option)
        if to_account_number:
            self.fo_assert_value_group('To Account number', to_account_number)
        if expected_posting:
            self.assert_posting_data(**expected_posting)
        self.fo_assert_checkbox('Caution!  There is no doubt that banks may be used as a means of Money Laundering/ Terrorist Financing/ Proliferation of Weapons of Mass Destruction.', True)

    # DPT_APR: Approve deposit account
    # def dpt_apr(self, account_number, account_holder_name=None, account_holding_branch_name=None, catalogue_code=None, catalogue_name=None, customer_segmentation=None, deposit_type=None, deposit_sub_type=None, linkage_account_number=None, created_by=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
    #     # open form
    #     self.close_all_form()
    #     self.open_fo('DPT_APR', 'Approve')
    #     self.wait_for_button_available('Accept')
    #     self.assert_form_title('Approve deposit account')
    #     # enter value
    #     self.fo_write_group('Account number', str(account_number).replace('-', ''))
    #     self.wait_loading()
    #     self.fo_write_text('Description', 'AUTO TEST')
    #     if account_holder_name:
    #         self.fo_assert_text('Account holder name', account_holder_name)
    #     if account_holding_branch_name:
    #         self.fo_assert_text('Account holding branch name', account_holding_branch_name)
    #     if catalogue_code:
    #         self.fo_assert_text('Catalogue code', catalogue_code)
    #     if catalogue_name:
    #         self.fo_assert_text('Catalogue name', catalogue_name)
    #     if customer_segmentation:
    #         self.fo_assert_text('Customer segmentation', customer_segmentation)
    #     if deposit_type:
    #         self.fo_assert_select('Deposit type', deposit_type)
    #     if deposit_sub_type:
    #         self.fo_assert_select('Deposit sub type', deposit_sub_type)
    #     if linkage_account_number:
    #         self.fo_assert_value_group('Linkage account number', linkage_account_number)
    #     if created_by:
    #         self.fo_assert_select('Created by', created_by)
    #     if ifc_codes:
    #         self.add_fees(ifc_codes, values, total_fee)
    #     # click 'Accept'
    #     self.click_button('Accept')
    #     # approve
    #     if approve_later=='Y':
    #         self.click_button('Later')
    #     if approve_on_form=='Y':
    #         self.fo_approve_in_popup(
    #             username=username,
    #             password=password,
    #             reason=reason
    #         )
    #     if list_error_message:
    #     # verify error
    #         self.assert_error_message()
    #         self.assert_list_error_message(list_error_message)
    #         print('Transaction failed!')
    #     else:
    #     # verify success
    #         self.switch_to_core_banking()
    #         self.assert_button_disable('Accept')
    #         self.assert_notification("Saved successfully!")
    #         self.close_voucher()
    #         if expected_posting:
    #             self.assert_posting_data(**expected_posting)
    #         transaction_references=self.fo_get_text('Transaction references')
    #         print(f'Transaction references DPT_APR: {transaction_references}')
    #         deposit_account_mask=self.fo_get_value_group('Account number')
    #         print(f'Account number: {deposit_account_mask}')
    #         return transaction_references, deposit_account_mask

    def dpt_apr(self, account_number=None, description=None, account_holder_name=None, account_holding_branch_name=None, catalogue_code=None, catalogue_name=None, customer_segmentation=None, deposit_type=None, deposit_sub_type=None, linkage_account_number=None, created_by=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.open_fo('DPT_APR', 'Approve deposit account ')
        self.wait_for_button_available('Accept')
        self.assert_form_title('Approve deposit account ')
        # enter value
        if account_number:
            self.fo_write_group('Account number', str(account_number).replace('-', ''))
            self.wait_loading()
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_write_text('Description', description)
        if account_holder_name:
            self.fo_assert_text('Account holder name', account_holder_name)
        if account_holding_branch_name:
            self.fo_assert_text('Account holding branch name', account_holding_branch_name)
        if catalogue_code:
            self.fo_assert_text('Catalogue code', catalogue_code)
        if catalogue_name:
            self.fo_assert_text('Catalogue name', catalogue_name)
        if customer_segmentation:
            self.fo_assert_text('Customer segmentation', customer_segmentation)
        if deposit_type:
            self.fo_assert_select('Deposit type', deposit_type)
        if deposit_sub_type:
            self.fo_assert_select('Deposit sub type', deposit_sub_type)
        if linkage_account_number:
            self.fo_assert_value_group('Linkage account number', linkage_account_number)
        if created_by:
            self.fo_assert_select('Created by', created_by)
        self.wait_loading()
        # click 'Accept'
        self.click_button('Accept')
        # approve
        if approve_later=='Y':
            self.click_button('Later')
        if approve_on_form=='Y':
            self.fo_approve_in_popup(
                username=username,
                password=password,
                reason=reason
            )
        if list_error_message:
        # verify error
            self.assert_error_message()
            self.assert_list_error_message(list_error_message)
            print('Transaction failed!')
        else:
        # verify success
            self.assert_button_disable('Accept')
            self.switch_to_core_banking()
            self.assert_notification('Saved successfully!')
            self.close_voucher()
            if expected_posting:
                self.assert_posting_data(**expected_posting)
            transaction_references=self.fo_get_text('Transaction references')
            print(f'Transaction references DPT_APR: {transaction_references}')
            account_number_out=self.fo_get_value_group('Account number')
            print(f'Account number: {account_number_out}')
            return transaction_references, account_number_out

    def dpt_apr_view(self, transaction_references, account_number=None, description=None, account_holder_name=None, account_holding_branch_name=None, catalogue_code=None, catalogue_name=None, customer_segmentation=None, deposit_type=None, deposit_sub_type=None, linkage_account_number=None, created_by=None, expected_posting=None):
        self.transaction_view(transaction_references, 'Approve deposit account ')
        # compare value
        if account_number:
            self.fo_assert_value_group('Account number', self.deposit_account_number_mask(account_number))
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_assert_text('Description', description)
        if account_holder_name:
            self.fo_assert_text('Account holder name', account_holder_name)
        if account_holding_branch_name:
            self.fo_assert_text('Account holding branch name', account_holding_branch_name)
        if catalogue_code:
            self.fo_assert_text('Catalogue code', catalogue_code)
        if catalogue_name:
            self.fo_assert_text('Catalogue name', catalogue_name)
        if customer_segmentation:
            self.fo_assert_text('Customer segmentation', customer_segmentation)
        if deposit_type:
            self.fo_assert_select('Deposit type', deposit_type)
        if deposit_sub_type:
            self.fo_assert_select('Deposit sub type', deposit_sub_type)
        if linkage_account_number:
            self.fo_assert_value_group('Linkage account number', linkage_account_number)
        if created_by:
            self.fo_assert_select('Created by', created_by)
        if expected_posting:
            self.assert_posting_data(**expected_posting)

    # DPT_REJ: Reject deposit account 
    def dpt_rej(self, account_number, account_holder_name=None, account_holding_branch_name=None, catalogue_code=None, catalogue_name=None, customer_segmentation=None, deposit_type=None, deposit_sub_type=None, created_by=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.open_fo('DPT_REJ', 'Reject deposit')
        self.wait_for_button_available('Accept')
        self.assert_form_title('Reject deposit account')
        # enter value
        self.fo_write_group('Account number', str(account_number).replace('-', ''))
        self.wait_loading()
        self.fo_write_text('Description', 'AUTO TEST')
        if account_holder_name:
            self.fo_assert_text('Account holder name', account_holder_name)
        if account_holding_branch_name:
            self.fo_assert_text('Account holding branch name', account_holding_branch_name)
        if catalogue_code:
            self.fo_assert_text('Catalogue code', catalogue_code)
        if catalogue_name:
            self.fo_assert_text('Catalogue name', catalogue_name)
        if customer_segmentation:
            self.fo_assert_text('Customer segmentation', customer_segmentation)
        if deposit_type:
            self.fo_assert_select('Deposit type', deposit_type)
        if deposit_sub_type:
            self.fo_assert_select('Deposit sub type', deposit_sub_type)
        if created_by:
            self.fo_assert_select('Created by', created_by)
        if ifc_codes:
            self.add_fees(ifc_codes, values, total_fee)
        # click 'Accept'
        self.click_button('Accept')
        # approve
        if approve_later=='Y':
            self.click_button('Later')
        if approve_on_form=='Y':
            self.fo_approve_in_popup(
                username=username,
                password=password,
                reason=reason
            )
        if list_error_message:
        # verify error
            self.assert_error_message()
            self.assert_list_error_message(list_error_message)
            print('Transaction failed!')
        else:
        # verify success
            self.switch_to_core_banking()
            self.assert_button_disable('Accept')
            self.assert_notification("Saved successfully!")
            self.close_voucher()
            if expected_posting:
                self.assert_posting_data(**expected_posting)
            transaction_references=self.fo_get_text('Transaction references')
            print(f'Transaction references DPT_REJ: {transaction_references}')
            deposit_account_mask=self.fo_get_value_group('Account number')
            print(f'Account number: {deposit_account_mask}')
            return transaction_references, deposit_account_mask

    # DPT_CDP: 1110: Cash deposit
    # def dpt_cdp(self, account_number, amount_deposit, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
    #     # open form
    #     self.close_all_form()
    #     self.open_fo('DPT_CDP', '1110')
    #     self.wait_for_button_available('Accept')
    #     self.assert_form_title('1110: Cash deposit')
    #     # enter value
    #     self.fo_write_group('Account number', account_number)
    #     self.fo_write_number('Amount deposit', str(amount_deposit).replace(',', ''))
    #     if self.fo_get_value('Amount deposit')!= amount_deposit:
    #         self.fo_write_number('Amount deposit', str(amount_deposit).replace(',', ''))
    #     self.fo_write_text('Description', 'AUTO TEST')
    #     if ifc_codes:
    #         self.add_fees(ifc_codes, values, total_fee)
    #     self.wait_loading()
    #     self.fo_click_checkbox('Caution!  There is no doubt that banks may be used as a means of Money Laundering/ Terrorist Financing/ Proliferation of Weapons of Mass Destruction.')
    #     # click 'Accept'
    #     self.click_button('Accept')
    #     # approve
    #     if approve_later=='Y':
    #         self.click_button('Later')
    #     if approve_on_form=='Y':
    #         self.fo_approve_in_popup(
    #             username=username,
    #             password=password,
    #             reason=reason
    #         )
    #     if list_error_message:
    #     # verify error
    #         self.assert_error_message()
    #         self.assert_list_error_message(list_error_message)
    #         print('Transaction failed!')
    #     else:
    #     # verify success
    #         self.assert_button_disable('Accept')
    #         self.switch_to_core_banking()
    #         self.assert_notification('Saved successfully!')
    #         self.close_voucher()
    #         if expected_posting:
    #             self.assert_posting_data(**expected_posting)
    #         transaction_references=self.fo_get_text('Transaction references')
    #         print(f'Transaction references DPT_CDP: {transaction_references}')
    #         deposit_account_mask=self.fo_get_value_group('Account number')
    #         print(f'Account number: {deposit_account_mask}')
    #         return transaction_references, deposit_account_mask

    def dpt_cdp(self, account_number=None, amount_deposit=None, depositor_code=None, depositor_address=None, mobile_phone=None, nrc=None, description=None, account_holding_branch_name=None, depositor_name=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.open_fo('DPT_CDP', '1110: Cash deposit')
        self.wait_for_button_available('Accept')
        self.assert_form_title('1110: Cash deposit')
        # enter value
        if account_number:
            self.fo_write_group('Account number', str(account_number).replace('-', ''))
            self.wait_loading()
        if amount_deposit:
            self.fo_write_number('Amount deposit', str(amount_deposit).replace(',', ''))
            self.wait_loading()
        if depositor_code:
            self.fo_write('Depositor code', depositor_code)
        if depositor_address:
            self.fo_write_text('Depositor address', depositor_address)
        if mobile_phone:
            self.fo_click_collap('Depositor description')
            self.fo_write_text_multi('Depositor description', 'Mobile phone', mobile_phone)
        if nrc:
            self.fo_click_collap('Depositor description')
            self.fo_write_text_multi('Depositor description', 'NRC', nrc)
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_write_text('Description', description)
        if account_holding_branch_name:
            self.fo_assert_text('Account holding branch name', account_holding_branch_name)
        if depositor_name:
            self.fo_assert_text('Depositor name', depositor_name)
        if ifc_codes:
            self.add_fees(ifc_codes, values, total_fee)
        self.wait_loading()
        self.fo_click_checkbox('Caution!  There is no doubt that banks may be used as a means of Money Laundering/ Terrorist Financing/ Proliferation of Weapons of Mass Destruction.')
        self.wait_loading()
        # click 'Accept'
        self.click_button('Accept')
        # approve
        if approve_later=='Y':
            self.click_button('Later')
        if approve_on_form=='Y':
            self.fo_approve_in_popup(
                username=username,
                password=password,
                reason=reason
            )
        if list_error_message:
        # verify error
            self.assert_error_message()
            self.assert_list_error_message(list_error_message)
            print('Transaction failed!')
        else:
        # verify success
            self.assert_button_disable('Accept')
            self.switch_to_core_banking()
            self.assert_notification('Saved successfully!')
            self.close_voucher()
            if expected_posting:
                self.assert_posting_data(**expected_posting)
            transaction_references=self.fo_get_text('Transaction references')
            print(f'Transaction references DPT_CDP: {transaction_references}')
            account_number_out=self.fo_get_value_group('Account number')
            print(f'Account number: {account_number_out}')
            return transaction_references, account_number_out

    def dpt_cdp_view(self, transaction_references, account_number=None, amount_deposit=None, depositor_code=None, depositor_address=None, mobile_phone=None, nrc=None, description=None, account_holding_branch_name=None, depositor_name=None, expected_posting=None):
        self.transaction_view(transaction_references, '1110: Cash deposit')
        # compare value
        if account_number:
            self.fo_assert_value_group('Account number', self.deposit_account_number_mask(account_number))
        if amount_deposit:
            self.fo_assert_value('Amount deposit', amount_deposit)
        if depositor_code:
            self.fo_assert_value('Depositor code', depositor_code)
        if depositor_address:
            self.fo_assert_text('Depositor address', depositor_address)
        if mobile_phone:
            self.fo_click_collap('Depositor description')
            self.fo_assert_text_multi('Depositor description', 'Mobile phone', mobile_phone)
        if nrc:
            self.fo_click_collap('Depositor description')
            self.fo_assert_text_multi('Depositor description', 'NRC', nrc)
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_assert_text('Description', description)
        if account_holding_branch_name:
            self.fo_assert_text('Account holding branch name', account_holding_branch_name)
        if depositor_name:
            self.fo_assert_text('Depositor name', depositor_name)
        if expected_posting:
            self.assert_posting_data(**expected_posting)
        self.fo_assert_checkbox('Caution!  There is no doubt that banks may be used as a means of Money Laundering/ Terrorist Financing/ Proliferation of Weapons of Mass Destruction.', True)

    # # DPT_MDP: 1112: Miscellaneous deposit
    # def dpt_mdp(self, account_number, amount_deposit, debit_accounting, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
    #     # open form
    #     self.close_all_form()
    #     self.open_fo('DPT_MDP', '1112')
    #     self.wait_for_button_available('Accept')
    #     self.assert_form_title('1112: Miscellaneous deposit')
    #     # enter value
    #     self.fo_write_group('Account number', str(account_number).replace('-', ''))
    #     self.fo_write_number_group('Amount Deposit', str(amount_deposit).replace(',', ''))
    #     if self.fo_get_value_group('Amount Deposit')!= amount_deposit:
    #         self.fo_write_number_group('Amount Deposit', str(amount_deposit).replace(',', ''))
    #     self.fo_write_group('Debit accounting', str(debit_accounting).replace('-', ''))
    #     self.fo_write_text('Description', 'AUTO TEST')
    #     if ifc_codes:
    #         self.add_fees(ifc_codes, values, total_fee)
    #     # click 'Accept'
    #     self.click_button('Accept')
    #     # approve
    #     if approve_later=='Y':
    #         self.click_button('Later')
    #     if approve_on_form=='Y':
    #         self.fo_approve_in_popup(
    #             username=username,
    #             password=password,
    #             reason=reason
    #         )
    #     if list_error_message:
    #     # verify error
    #         self.assert_error_message()
    #         self.assert_list_error_message(list_error_message)
    #         print('Transaction failed!')
    #     else:
    #     # verify success
    #         self.assert_button_disable('Accept')
    #         self.switch_to_core_banking()
    #         self.assert_notification('Saved successfully!')
    #         self.close_voucher()
    #         if expected_posting:
    #             self.assert_posting_data(**expected_posting)
    #         transaction_references=self.fo_get_text('Transaction references')
    #         print(f'Transaction references DPT_MDP: {transaction_references}')
    #         deposit_account_mask=self.fo_get_value_group('Account number')
    #         print(f'Account number: {deposit_account_mask}')
    #         debit_accounting_mask=self.fo_get_value_group('Debit accounting')
    #         print(f'Debit accounting: {debit_accounting_mask}')
    #         return transaction_references, deposit_account_mask, debit_accounting_mask

    def dpt_mdp(self, account_number=None, amount_deposit=None, debit_accounting=None, depositor_name=None, depositor_code=None, depositor_address=None, mobile_phone=None, nrc=None, description=None, _account_holding_branch_name=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.open_fo('DPT_MDP', '1112: Miscellaneous deposit')
        self.wait_for_button_available('Accept')
        self.assert_form_title('1112: Miscellaneous deposit')
        # enter value
        if account_number:
            self.fo_write_group('Account number', str(account_number).replace('-', ''))
            self.wait_loading()
        if amount_deposit:
            self.fo_write_number_group('Amount Deposit', str(amount_deposit).replace(',', ''))
            self.wait_loading()
        if debit_accounting:
            self.fo_write_group('Debit accounting', str(debit_accounting).replace('-', ''))
            self.wait_loading()
        if depositor_name:
            self.fo_write_text('Depositor name', depositor_name)
        if depositor_code:
            self.fo_write('Depositor code', str(depositor_code).replace('-', ''))
        if depositor_address:
            self.fo_write_text('Depositor address', depositor_address)
        if mobile_phone:
            self.fo_click_collap('Depositor description')
            self.fo_write_text_multi('Depositor description', 'Mobile phone', mobile_phone)
        if nrc:
            self.fo_click_collap('Depositor description')
            self.fo_write_text_multi('Depositor description', 'NRC', nrc)
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_write_text('Description', description)
        if _account_holding_branch_name:
            self.fo_assert_text(' Account holding branch name', _account_holding_branch_name)
        if ifc_codes:
            self.add_fees(ifc_codes, values, total_fee)
        self.wait_loading()
        # click 'Accept'
        self.click_button('Accept')
        # approve
        if approve_later=='Y':
            self.click_button('Later')
        if approve_on_form=='Y':
            self.fo_approve_in_popup(
                username=username,
                password=password,
                reason=reason
            )
        if list_error_message:
        # verify error
            self.assert_error_message()
            self.assert_list_error_message(list_error_message)
            print('Transaction failed!')
        else:
        # verify success
            self.assert_button_disable('Accept')
            self.switch_to_core_banking()
            self.assert_notification('Saved successfully!')
            self.close_voucher()
            if expected_posting:
                self.assert_posting_data(**expected_posting)
            transaction_references=self.fo_get_text('Transaction references')
            print(f'Transaction references DPT_MDP: {transaction_references}')
            account_number_out=self.fo_get_value_group('Account number')
            print(f'Account number: {account_number_out}')
            debit_accounting_out=self.fo_get_value_group('Debit accounting')
            print(f'Debit accounting: {debit_accounting_out}')
            return transaction_references, account_number_out, debit_accounting_out

    def dpt_mdp_view(self, transaction_references, account_number=None, amount_deposit=None, debit_accounting=None, depositor_name=None, depositor_code=None, depositor_address=None, mobile_phone=None, nrc=None, description=None, _account_holding_branch_name=None, expected_posting=None):
        self.transaction_view(transaction_references, '1112: Miscellaneous deposit')
        # compare value
        if account_number:
            self.fo_assert_value_group('Account number', self.deposit_account_number_mask(account_number))
        if amount_deposit:
            self.fo_assert_value_group('Amount Deposit', amount_deposit)
        if debit_accounting:
            self.fo_assert_value_group('Debit accounting', self.gl_account_number_mask(debit_accounting))
        if depositor_name:
            self.fo_assert_text('Depositor name', depositor_name)
        if depositor_code:
            self.fo_assert_value('Depositor code', self.customer_code_mask(depositor_code))
        if depositor_address:
            self.fo_assert_text('Depositor address', depositor_address)
        if mobile_phone:
            self.fo_click_collap('Depositor description')
            self.fo_assert_text_multi('Depositor description', 'Mobile phone', mobile_phone)
        if nrc:
            self.fo_click_collap('Depositor description')
            self.fo_assert_text_multi('Depositor description', 'NRC', nrc)
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_assert_text('Description', description)
        if _account_holding_branch_name:
            self.fo_assert_text(' Account holding branch name', _account_holding_branch_name)
        if expected_posting:
            self.assert_posting_data(**expected_posting)

    # DPT_TRF: 1130: Transfer from deposit account to deposit account
    def dpt_trf(self, debit_account, amount, credit_account, passbook_number=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.open_fo('DPT_TRF', '1130')
        self.wait_for_button_available('Accept')
        self.assert_form_title('1130: Transfer from deposit account to deposit account')
        # enter value
        self.fo_write_group('Debit account', str(debit_account).replace('-', ''))
        self.fo_write_group('Credit account', str(credit_account).replace('-', ''))
        self.fo_write_number('Amount', str(amount).replace(',', ''))
        if self.fo_get_value('Amount')!= amount:
            self.fo_write_number('Amount', str(amount).replace(',', ''))
        self.fo_write_group('Credit account', str(credit_account).replace('-', ''))
        self.fo_write_text('Description', 'AUTO TEST')
        if ifc_codes:
            self.add_fees(ifc_codes, values, total_fee)
        self.wait_loading()
        if passbook_number:
            self.assertEqual(self.fo_get_text('Passbook number'), str(passbook_number).replace('-', ''))
        self.fo_click_checkbox('Caution!  There is no doubt that banks may be used as a means of Money Laundering/ Terrorist Financing/ Proliferation of Weapons of Mass Destruction.')
        # click 'Accept'
        self.click_button('Accept')
        # approve
        if approve_later=='Y':
            self.click_button('Later')
        if approve_on_form=='Y':
            self.fo_approve_in_popup(
                username=username,
                password=password,
                reason=reason
            )
        if list_error_message:
        # verify error
            self.assert_error_message()
            self.assert_list_error_message(list_error_message)
            print('Transaction failed!')
        else:
        # verify success
            self.assert_button_disable('Accept')
            self.switch_to_core_banking()
            self.assert_notification('Saved successfully!')
            self.close_voucher()
            if expected_posting:
                self.assert_posting_data(**expected_posting)
            transaction_references=self.fo_get_text('Transaction references')
            print(f'Transaction references DPT_TRF: {transaction_references}')
            debit_account_mask=self.fo_get_value_group('Debit account')
            print(f'Debit account: {debit_account_mask}')
            credit_account_mask=self.fo_get_value_group('Credit account')
            print(f'Credit account: {credit_account_mask}')
            return transaction_references, debit_account_mask, credit_account_mask

    # DPT_CWR: 1120: Cash withdrawal
    def dpt_cwr(self, account_number, withdraw_amount, passbook_number=None, withdrawer_name=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        self.close_all_form()
        self.open_fo('DPT_CWR', '1120')
        self.wait_for_button_available('Accept')
        self.assert_form_title('1120: Cash withdrawal')
        self.fo_write_group('Account number', account_number)
        self.fo_write_text('Description', 'AUTO TEST')
        self.fo_write_number('Withdraw amount', str(withdraw_amount).replace(',', ''))
        if self.fo_get_value('Withdraw amount')!= withdraw_amount:
            self.fo_write_number('Withdraw amount', str(withdraw_amount).replace(',', ''))
        self.wait_loading()
        if passbook_number:
            self.assertEqual(self.fo_get_text('Passbook number'), str(passbook_number).replace('-', ''))
        if withdrawer_name:
            self.fo_write_text('Withdrawer name', withdrawer_name)
        if ifc_codes:
            self.add_fees(ifc_codes, values, total_fee)
        self.wait_loading()
        self.fo_click_checkbox('Caution!  There is no doubt that banks may be used as a means of Money Laundering/ Terrorist Financing/ Proliferation of Weapons of Mass Destruction.')
        # click 'Accept'
        self.click_button('Accept')
        # approve
        if approve_later=='Y':
            self.click_button('Later')
        if approve_on_form=='Y':
            self.fo_approve_in_popup(
                username=username,
                password=password,
                reason=reason
            )
        if list_error_message:
        # verify error
            self.assert_error_message()
            self.assert_list_error_message(list_error_message)
            print('Transaction failed!')
        else:
        # verify success
            self.assert_button_disable('Accept')
            self.switch_to_core_banking()
            self.assert_notification('Saved successfully!')
            self.close_voucher()
            if expected_posting:
                self.assert_posting_data(**expected_posting)
            transaction_references=self.fo_get_text('Transaction references')
            print(f'Transaction references DPT_CWR: {transaction_references}')
            deposit_account_mask=self.fo_get_value_group('Account number')
            print(f'Account number: {deposit_account_mask}')
            return transaction_references, deposit_account_mask

    # DPT_MWR: 1122: Miscellaneous withdrawal
    def dpt_mwr(self, account_number, withdraw_amount, credit_accounting, passbook_number=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.open_fo('DPT_MWR', '1122')
        self.wait_for_button_available('Accept')
        self.assert_form_title('1122: Miscellaneous withdrawal')
        # enter value
        self.fo_write_group('Account number', str(account_number).replace('-', ''))
        self.fo_write_group('Credit accounting', str(credit_accounting).replace('-', ''))
        self.fo_write_number('Withdraw amount', str(withdraw_amount).replace(',', ''))
        if self.fo_get_value('Withdraw amount')!= withdraw_amount:
            self.fo_write_number('Withdraw amount', str(withdraw_amount).replace(',', ''))
        self.fo_write_text('Description', 'AUTO TEST')
        if ifc_codes:
            self.add_fees(ifc_codes, values, total_fee)
        self.wait_loading()
        if passbook_number:
            self.assertEqual(self.fo_get_text('Passbook number'), str(passbook_number).replace('-', ''))
        self.fo_click_checkbox('Caution!  There is no doubt that banks may be used as a means of Money Laundering/ Terrorist Financing/ Proliferation of Weapons of Mass Destruction.')
        # click 'Accept'
        self.click_button('Accept')
        # approve
        if approve_later=='Y':
            self.click_button('Later')
        if approve_on_form=='Y':
            self.fo_approve_in_popup(
                username=username,
                password=password,
                reason=reason
            )
        if list_error_message:
        # verify error
            self.assert_error_message()
            self.assert_list_error_message(list_error_message)
            print('Transaction failed!')
        else:
        # verify success
            self.assert_button_disable('Accept')
            self.switch_to_core_banking()
            self.assert_notification('Saved successfully!')
            self.close_voucher()
            if expected_posting:
                self.assert_posting_data(**expected_posting)
            transaction_references=self.fo_get_text('Transaction references')
            print(f'Transaction references DPT_MWR: {transaction_references}')
            deposit_account_mask=self.fo_get_value_group('Account number')
            print(f'Account number: {deposit_account_mask}')
            credit_accounting_mask=self.fo_get_value_group('Credit accounting')
            print(f'Credit accounting: {credit_accounting_mask}')
            return transaction_references, deposit_account_mask

    # DPT_CAS: 11841: Change account status
    def dpt_cas(self, account_number, new_status, current_status=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.open_fo('DPT_CAS', '11841')
        self.wait_for_button_available('Accept')
        self.assert_form_title('11841: Change account status')
        # enter value
        self.fo_write_group('Account number', str(account_number).replace('-', ''))
        self.fo_write_text('Description', 'AUTO TEST')
        self.fo_select('New status', new_status)
        self.wait_loading()
        if current_status:
            self.fo_assert_text('Current status', current_status)
        if ifc_codes:
            self.add_fees(ifc_codes, values, total_fee)
        # click 'Accept'
        self.click_button('Accept')
        # approve
        if approve_later=='Y':
            self.click_button('Later')
        if approve_on_form=='Y':
            self.fo_approve_in_popup(
                username=username,
                password=password,
                reason=reason
            )
        if list_error_message:
        # verify error
            self.assert_error_message()
            self.assert_list_error_message(list_error_message)
            print('Transaction failed!')
        else:
        # verify success
            self.assert_button_disable('Accept')
            self.switch_to_core_banking()
            self.assert_notification('Saved successfully!')
            self.close_voucher()
            if expected_posting:
                self.assert_posting_data(**expected_posting)
            transaction_references=self.fo_get_text('Transaction references')
            print(f'Transaction references DPT_CAS: {transaction_references}')
            deposit_account_mask=self.fo_get_value_group('Account number')
            print(f'Account number: {deposit_account_mask}')
            new_status_actual=self.fo_get_select('New status')
            print(f'New status: {new_status_actual}')
            return transaction_references, deposit_account_mask, new_status_actual

    # DPT_BLK: 11840: Block account
    def dpt_blk(self, account_number, block_reason=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.open_fo('DPT_BLK', '11840')
        self.wait_for_button_available('Accept')
        self.assert_form_title('11840: Block account')
        # enter value
        self.fo_write_group('Account number', str(account_number).replace('-', ''))
        self.wait_loading()
        if block_reason:
            self.fo_select('Block reason', block_reason)
        self.fo_write_text('Description', 'AUTO TEST')
        self.key_escape()
        if ifc_codes:
            self.add_fees(ifc_codes, values, total_fee)
        # click 'Accept'
        self.click_button('Accept')
        # approve
        if approve_later=='Y':
            self.click_button('Later')
        if approve_on_form=='Y':
            self.fo_approve_in_popup(
                username=username,
                password=password,
                reason=reason
            )
        if list_error_message:
        # verify error
            self.assert_error_message()
            self.assert_list_error_message(list_error_message)
            print('Transaction failed!')
        else:
        # verify success
            self.assert_button_disable('Accept')
            self.switch_to_core_banking()
            self.assert_notification('Saved successfully!')
            self.close_voucher()
            if expected_posting:
                self.assert_posting_data(**expected_posting)
            transaction_references=self.fo_get_text('Transaction references')
            print(f'Transaction references DPT_BLK: {transaction_references}')
            deposit_account_mask=self.fo_get_value_group('Account number')
            print(f'Account number: {deposit_account_mask}')
            return transaction_references, deposit_account_mask

    # DPT_RLS: 11843: Release block account
    def dpt_rls(self, account_number, block_reason=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.open_fo('DPT_RLS', '11843')
        self.wait_for_button_available('Accept')
        self.assert_form_title('11843: Release block account')
        # enter value
        self.fo_write_group('Account number', str(account_number).replace('-', ''))
        self.fo_write_text('Description', 'AUTO TEST')
        if ifc_codes:
            self.add_fees(ifc_codes, values, total_fee)
        self.wait_loading()
        if block_reason:
            self.fo_assert_select('Block reason', block_reason)
        # click 'Accept'
        self.click_button('Accept')
        # approve
        if approve_later=='Y':
            self.click_button('Later')
        if approve_on_form=='Y':
            self.fo_approve_in_popup(
                username=username,
                password=password,
                reason=reason
            )
        if list_error_message:
        # verify error
            self.assert_error_message()
            self.assert_list_error_message(list_error_message)
            print('Transaction failed!')
        else:
        # verify success
            self.assert_button_disable('Accept')
            self.switch_to_core_banking()
            self.assert_notification('Saved successfully!')
            self.close_voucher()
            if expected_posting:
                self.assert_posting_data(**expected_posting)
            transaction_references=self.fo_get_text('Transaction references')
            print(f'Transaction references DPT_RLS: {transaction_references}')
            deposit_account_mask=self.fo_get_value_group('Account number')
            print(f'Account number: {deposit_account_mask}')
            return transaction_references, deposit_account_mask

    # DPT_IFC: 1169: Adjust deposit interest
    def dpt_ifc(self, account_number, ifc_code, adjustment_amount, account_holding_branch_name=None, customer_code=None, account_name=None, accrual_interest_amount=None, interest_due_amount=None, interest_repayable_amount=None, current_ifc_amount=None, ifc_type=None, new_ifc_amount=None, adjusted_accrual_interest=None, adjusted_due_interest=None, adjusted_payable_interest=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.open_fo('DPT_IFC', '1169')
        self.wait_for_button_available('Accept')
        self.assert_form_title('DPT-1169: Adjust Deposit Interest')
        # enter value
        self.fo_write_group('Account number', str(account_number).replace('-', ''))
        self.wait_loading()
        self.lookup_data('IFC code', 'Code', ifc_code)
        self.wait_loading()
        self.fo_write_text('Description', 'AUTO TEST')
        self.wait_loading()
        self.fo_write_number('Adjustment amount', str(adjustment_amount).replace(',', ''))
        if self.fo_get_value('Adjustment amount')!= adjustment_amount:
            self.fo_write_number('Adjustment amount', str(adjustment_amount).replace(',', ''))
        self.wait_loading()
        if account_holding_branch_name:
            self.fo_assert_text('Account holding branch name', account_holding_branch_name)
        if customer_code:
            self.fo_assert_value('Customer code', customer_code)
        if account_name:
            self.fo_assert_text('Account name', account_name)
        if accrual_interest_amount:
            self.fo_assert_value('Accrual interest amount', accrual_interest_amount)
        if interest_due_amount:
            self.fo_assert_value('Interest due amount', interest_due_amount)
        if interest_repayable_amount:
            self.fo_assert_value('Interest repayable amount', interest_repayable_amount)
        if current_ifc_amount:
            self.fo_assert_value('Current IFC amount', current_ifc_amount)
        if ifc_type:
            self.fo_assert_select('IFC Type', ifc_type)
        if new_ifc_amount:
            self.fo_assert_value('New ifc amount', new_ifc_amount)
        if adjusted_accrual_interest:
            self.fo_assert_value('Adjusted accrual interest', adjusted_accrual_interest)
        if adjusted_due_interest:
            self.fo_assert_value('Adjusted due interest', adjusted_due_interest)
        if adjusted_payable_interest:
            self.fo_assert_value('Adjusted payable interest', adjusted_payable_interest)
        if ifc_codes:
            self.add_fees(ifc_codes, values, total_fee)
        # click 'Accept'
        self.click_button('Accept')
        # approve
        if approve_later=='Y':
            self.click_button('Later')
        if approve_on_form=='Y':
            self.fo_approve_in_popup(
                username=username,
                password=password,
                reason=reason
            )
        if list_error_message:
        # verify error
            self.assert_error_message()
            self.assert_list_error_message(list_error_message)
            print('Transaction failed!')
        else:
        # verify success
            self.assert_button_disable('Accept')
            self.switch_to_core_banking()
            self.assert_notification('Saved successfully!')
            self.close_voucher()
            if expected_posting:
                self.assert_posting_data(**expected_posting)
            transaction_references=self.fo_get_text('Transaction references')
            print(f'Transaction references DPT_IFC: {transaction_references}')
            account_number_mask=self.fo_get_value_group('Account number')
            print(f'Account number: {account_number_mask}')
            return transaction_references, account_number_mask

    # DPT_CIP: 1140: Interest payment by cash
    def dpt_cip(self, account_number, account_holding_branch_name=None, passbook_number=None, interest_payable_receivable=None, interest_due=None, interest_overdue=None, interest_not_paid=None, interest_amount=None, gross_paid_interest_amount=None, receiver_name=None, receiver_id=None, receiver_address=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.open_fo('DPT_CIP', '1140')
        self.wait_for_button_available('Accept')
        self.assert_form_title('1140: Interest payment by cash')
        # enter value
        self.fo_write_group('Account number', str(account_number).replace('-', ''))
        self.wait_loading()
        if account_holding_branch_name:
            self.fo_assert_text('Account holding branch name', account_holding_branch_name)
        if passbook_number:
            self.fo_assert_text('Passbook number', passbook_number)
        if interest_payable_receivable:
            self.fo_assert_value('Interest payable/receivable', interest_payable_receivable)
        if interest_due:
            self.fo_assert_value('Interest due', interest_due)
        if interest_overdue:
            self.fo_assert_value('Interest overdue', interest_overdue)
        if interest_not_paid:
            self.fo_assert_value('Interest not paid', interest_not_paid)
        if interest_amount:
            self.fo_assert_value_group('Interest amount', interest_amount)
        if gross_paid_interest_amount:
            self.fo_assert_value('Gross paid interest amount', gross_paid_interest_amount)
        if receiver_name:
            self.fo_assert_text('Receiver name', receiver_name)
        if receiver_id:
            self.fo_assert_value('Receiver id', receiver_id)
        if receiver_address:
            self.fo_assert_text('Receiver address', receiver_address)
        self.fo_write_text('Description', 'AUTO TEST')
        if ifc_codes:
            self.add_fees(ifc_codes, values, total_fee)
        self.wait_loading()
        self.fo_click_checkbox('Caution!  There is no doubt that banks may be used as a means of Money Laundering/ Terrorist Financing/ Proliferation of Weapons of Mass Destruction.')
        # click 'Accept'
        self.click_button('Accept')
        # approve
        if approve_later=='Y':
            self.click_button('Later')
        if approve_on_form=='Y':
            self.fo_approve_in_popup(
                username=username,
                password=password,
                reason=reason
            )
        if list_error_message:
        # verify error
            self.assert_error_message()
            self.assert_list_error_message(list_error_message)
            print('Transaction failed!')
        else:
        # verify success
            self.assert_button_disable('Accept')
            self.switch_to_core_banking()
            self.assert_notification('Saved successfully!')
            self.close_voucher()
            if expected_posting:
                self.assert_posting_data(**expected_posting)
            transaction_references=self.fo_get_text('Transaction references')
            print(f'Transaction references DPT_CIP: {transaction_references}')
            account_number_mask=self.fo_get_value_group('Account number')
            print(f'Account number: {account_number_mask}')
            return transaction_references, account_number_mask

    # DPT_DIP: 1141: Interest payment to deposit account
    def dpt_dip(self, deposit_account, account_holding_branch_name=None, passbook_number=None, interest_payble_receivable=None, interest_due=None, interest_overdue=None, interest_not_paid=None, interest_amount=None, cross_interest_amount=None, paid_to_this_deposit_account=None, depositor_name=None, depositor_id=None, depositor_address=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.open_fo('DPT_DIP', '1141')
        self.wait_for_button_available('Accept')
        self.assert_form_title('1141: Interest payment to deposit account')
        # enter value
        self.fo_write_group('Deposit account', str(deposit_account).replace('-', ''))
        self.wait_loading()
        self.fo_write_group('Paid to this deposit account', str(paid_to_this_deposit_account).replace('-', ''))
        self.wait_loading()
        if account_holding_branch_name:
            self.fo_assert_text('Account holding branch name', account_holding_branch_name)
        if passbook_number:
            self.fo_assert_text('Passbook number', passbook_number)
        if interest_payble_receivable:
            self.fo_assert_value('Interest payble/receivable', interest_payble_receivable)
        if interest_due:
            self.fo_assert_value('Interest due', interest_due)
        if interest_overdue:
            self.fo_assert_value('Interest overdue', interest_overdue)
        if interest_not_paid:
            self.fo_assert_value('Interest not paid', interest_not_paid)
        if interest_amount:
            self.fo_assert_value_group('Interest amount', interest_amount)
        if cross_interest_amount:
            self.fo_assert_value('Cross interest amount', cross_interest_amount)
        if depositor_name:
            self.fo_assert_text('Depositor name', depositor_name)
        if depositor_id:
            self.fo_assert_value('Depositor id', depositor_id)
        if depositor_address:
            self.fo_assert_text('Depositor address', depositor_address)
        self.fo_write_text('Description', 'AUTO TEST')
        if ifc_codes:
            self.add_fees(ifc_codes, values, total_fee)
        self.wait_loading()
        self.fo_click_checkbox('Caution!  There is no doubt that banks may be used as a means of Money Laundering/ Terrorist Financing/ Proliferation of Weapons of Mass Destruction.')
        # click 'Accept'
        self.click_button('Accept')
        # approve
        if approve_later=='Y':
            self.click_button('Later')
        if approve_on_form=='Y':
            self.fo_approve_in_popup(
                username=username,
                password=password,
                reason=reason
            )
        if list_error_message:
        # verify error
            self.assert_error_message()
            self.assert_list_error_message(list_error_message)
            print('Transaction failed!')
        else:
        # verify success
            self.assert_button_disable('Accept')
            self.switch_to_core_banking()
            self.assert_notification('Saved successfully!')
            self.close_voucher()
            if expected_posting:
                self.assert_posting_data(**expected_posting)
            transaction_references=self.fo_get_text('Transaction references')
            print(f'Transaction references DPT_DIP: {transaction_references}')
            account_number_mask=self.fo_get_value_group('Deposit account')
            print(f'Account number: {account_number_mask}')
            return transaction_references, account_number_mask

    # DPT_MIP: 1142: Miscellaneous interest payment
    def dpt_mip(self, account_number, gl_account, account_holding_branch_name=None, passbook_number=None, interest_payble_receivable=None, interest_due=None, interest_overdue=None, interest_suspense=None, interest_not_paid=None, interest_amount=None, gross_interest_paid_out=None, depositor_name=None, depositor_id=None, depositor_address=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.open_fo('DPT_MIP', '1142')
        self.wait_for_button_available('Accept')
        self.assert_form_title('1142: Miscellaneous interest payment')
        # enter value
        self.fo_write_group('Account number', str(account_number).replace('-', ''))
        self.wait_loading()
        self.fo_write_group('GL account', str(gl_account).replace('-', ''))
        self.wait_loading()
        self.fo_write_text('Description', 'AUTO TEST')
        self.wait_loading()
        if account_holding_branch_name:
            self.fo_assert_text('Account holding branch name', account_holding_branch_name)
        if passbook_number:
            self.fo_assert_text('Passbook number', passbook_number)
        if interest_payble_receivable:
            self.fo_assert_value('Interest payble/receivable', interest_payble_receivable)
        if interest_due:
            self.fo_assert_value('Interest due', interest_due)
        if interest_overdue:
            self.fo_assert_value('Interest overdue', interest_overdue)
        if interest_suspense:
            self.fo_assert_value('Interest suspense', interest_suspense)
        if interest_not_paid:
            self.fo_assert_value('Interest not paid', interest_not_paid)
        if interest_amount:
            self.fo_assert_value_group('Interest amount', interest_amount)
        if gross_interest_paid_out:
            self.fo_assert_value('Gross interest paid out', gross_interest_paid_out)
        if depositor_name:
            self.fo_assert_text('Depositor name', depositor_name)
        if depositor_id:
            self.fo_assert_value('Depositor id', depositor_id)
        if depositor_address:
            self.fo_assert_text('Depositor address', depositor_address)
        if ifc_codes:
            self.add_fees(ifc_codes, values, total_fee)
        self.wait_loading()
        self.fo_click_checkbox('Caution!  There is no doubt that banks may be used as a means of Money Laundering/ Terrorist Financing/ Proliferation of Weapons of Mass Destruction.')
        # click 'Accept'
        self.click_button('Accept')
        # approve
        if approve_later=='Y':
            self.click_button('Later')
        if approve_on_form=='Y':
            self.fo_approve_in_popup(
                username=username,
                password=password,
                reason=reason
            )
        if list_error_message:
        # verify error
            self.assert_error_message()
            self.assert_list_error_message(list_error_message)
            print('Transaction failed!')
        else:
        # verify success
            self.assert_button_disable('Accept')
            self.switch_to_core_banking()
            self.assert_notification('Saved successfully!')
            self.close_voucher()
            if expected_posting:
                self.assert_posting_data(**expected_posting)
            transaction_references=self.fo_get_text('Transaction references')
            print(f'Transaction references DPT_MIP: {transaction_references}')
            account_number_mask=self.fo_get_value_group('Account number')
            print(f'Account number: {account_number_mask}')
            return transaction_references, account_number_mask

    # DPT_IPR: Payment interest for prepaid fixed deposit
    def dpt_ipr(self, account_number, credit_account, ifc_code=None, prepaid_interest=None, fee_collect_method=None, account_number_for_fee=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.open_fo('DPT_IPR', 'Prepaid')
        self.wait_for_button_available('Accept')
        self.assert_form_title('Payment Interest For Prepaid Fixed Deposit')
        # enter value
        self.fo_write_group('Account number', str(account_number).replace('-', ''))
        self.wait_loading()
        self.fo_write_group('Credit account', str(credit_account).replace('-', ''))
        self.wait_loading()
        if ifc_code:
            self.fo_assert_text('IFC code', ifc_code)
        if prepaid_interest:
            self.fo_assert_value('Prepaid interest', prepaid_interest)
        if fee_collect_method:
            self.fo_select('Fee collect method', fee_collect_method)
        if account_number_for_fee:
            self.fo_write_text_group('Account number for fee', account_number_for_fee)
        if ifc_codes:
            self.add_fees(ifc_codes, values, total_fee=total_fee)
        self.fo_write_text('Description', 'AUTO TEST')
        self.wait_loading()
        self.fo_click_checkbox('Caution!  There is no doubt that banks may be used as a means of Money Laundering/ Terrorist Financing/ Proliferation of Weapons of Mass Destruction.')
        # click 'Accept'
        self.click_button('Accept')
        # approve
        if approve_later=='Y':
            self.click_button('Later')
        if approve_on_form=='Y':
            self.fo_approve_in_popup(
                username=username,
                password=password,
                reason=reason
            )
        if list_error_message:
        # verify error
            self.assert_error_message()
            self.assert_list_error_message(list_error_message)
            print('Transaction failed!')
        else:
        # verify success
            self.assert_button_disable('Accept')
            self.switch_to_core_banking()
            self.assert_notification("Saved successfully!")
            self.close_voucher()
            if expected_posting:
                self.assert_posting_data(**expected_posting)
            transaction_references=self.fo_get_text('Transaction references')
            print(f'Transaction references DPT_IPR: {transaction_references}')
            account_number_mask=self.fo_get_value_group('Account number')
            print(f'Account number: {account_number_mask}')
            return transaction_references, account_number_mask

    # DPT_EMK: 1180: Hold balance
    def dpt_emk(self, account_number, hold_amount, expired_date, reference_code=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.open_fo('DPT_EMK', '1180')
        self.wait_for_button_available('Accept')
        self.assert_form_title('1180:Hold balance')
        # enter value
        self.fo_write_group('Account number', str(account_number).replace('-', ''))
        self.wait_loading()
        self.fo_write_number('Hold amount',  str(hold_amount).replace(',', ''))
        if self.fo_get_value('Hold amount')!= hold_amount:
            self.fo_write_number('Hold amount',  str(hold_amount).replace(',', ''))
        self.key_escape()
        if reference_code:
            self.fo_select('Reference code', reference_code)
        self.fo_write_date('Expired date', expired_date)
        self.fo_write_text('Description', 'AUTO TEST')
        if ifc_codes:
            self.add_fees(ifc_codes, values, total_fee)
        # click 'Accept'
        self.click_button('Accept')
        # approve
        if approve_later=='Y':
            self.click_button('Later')
        if approve_on_form=='Y':
            self.fo_approve_in_popup(
                username=username,
                password=password,
                reason=reason
            )
        if list_error_message:
        # verify error
            self.assert_error_message()
            self.assert_list_error_message(list_error_message)
            print('Transaction failed!')
        else:
        # verify success
            self.assert_button_disable('Accept')
            self.switch_to_core_banking()
            self.assert_notification('Saved successfully!')
            self.close_voucher()
            if expected_posting:
                self.assert_posting_data(**expected_posting)
            transaction_references=self.fo_get_text('Transaction references')
            print(f'Transaction references DPT_EMK: {transaction_references}')
            deposit_account_mask=self.fo_get_value_group('Account number')
            print(f'Account number: {deposit_account_mask}')
            return transaction_references, deposit_account_mask

    # DPT_ERL: 11851: Release hold balance
    def dpt_erl(self, account_number, holding_amount=None, earmark_amount=None, expired_date=None, reference_code=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.open_fo('DPT_ERL', '11851')
        self.wait_for_button_available('Accept')
        self.assert_form_title('11851:Release hold balance')
        # enter value
        self.fo_write_group('Account number', str(account_number).replace('-', ''))
        self.wait_loading()
        self.key_escape()
        self.fo_write_text('Description', 'AUTO TEST')
        self.wait_loading()
        if reference_code:
            self.fo_select('Reference code', reference_code)
        if holding_amount:
            self.fo_assert_value('Holding amount', holding_amount)
        if earmark_amount:
            self.fo_assert_value('Earmark amount', earmark_amount)
        if expired_date:
            self.fo_assert_date('Expired date', expired_date)
        if ifc_codes:
            self.add_fees(ifc_codes, values, total_fee)
        # click 'Accept'
        self.click_button('Accept')
        # approve
        if approve_later=='Y':
            self.click_button('Later')
        if approve_on_form=='Y':
            self.fo_approve_in_popup(
                username=username,
                password=password,
                reason=reason
            )
        if list_error_message:
        # verify error
            self.assert_error_message()
            self.assert_list_error_message(list_error_message)
            print('Transaction failed!')
        else:
        # verify success
            self.assert_button_disable('Accept')
            self.switch_to_core_banking()
            self.assert_notification('Saved successfully!')
            self.close_voucher()
            if expected_posting:
                self.assert_posting_data(**expected_posting)
            transaction_references=self.fo_get_text('Transaction references')
            print(f'Transaction references DPT_ERL: {transaction_references}')
            deposit_account_mask=self.fo_get_value_group('Account number')
            print(f'Account number: {deposit_account_mask}')
            return transaction_references, deposit_account_mask

    # DPT_FEE: 1185: Fee collection by transfer
    def dpt_fee(self, account_number, account_holding_branch_name=None, passbook_number=None, amount_for_fee_calculation=None, ifc_codes=None, values=None, total_fee=None, total_fee_amount=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.open_fo('DPT_FEE', '1185')
        self.wait_for_button_available('Accept')
        self.assert_form_title('1185: Fee collection by transfer')
        # enter value
        self.fo_write_group('Account number', str(account_number).replace('-', ''))
        self.wait_loading()
        if account_holding_branch_name:
            self.fo_assert_text('Account holding branch name', account_holding_branch_name)
        if passbook_number:
            self.fo_assert_text('Passbook number', passbook_number)
        if amount_for_fee_calculation:
            self.fo_write_number('Amount for fee calculation', str(amount_for_fee_calculation).replace(',', ''))
            if self.fo_get_value('Amount for fee calculation')!= amount_for_fee_calculation:
                self.fo_write_number('Amount for fee calculation', str(amount_for_fee_calculation).replace(',', ''))
        # add fee
        if ifc_codes:
            self.add_fees(ifc_codes, values, total_fee=total_fee)
        if total_fee_amount:
            self.fo_assert_value('Total fee amount', total_fee_amount)
        self.fo_write_text('Description', 'AUTO TEST')
        self.wait_loading()
        self.fo_click_checkbox('Caution!  There is no doubt that banks may be used as a means of Money Laundering/ Terrorist Financing/ Proliferation of Weapons of Mass Destruction.')
        # click 'Accept'
        self.click_button('Accept')
        # approve
        if approve_later=='Y':
            self.click_button('Later')
        if approve_on_form=='Y':
            self.fo_approve_in_popup(
                username=username,
                password=password,
                reason=reason
            )
        if list_error_message:
        # verify error
            self.assert_error_message()
            self.assert_list_error_message(list_error_message)
            print('Transaction failed!')
        else:
        # verify success
            self.assert_button_disable('Accept')
            self.switch_to_core_banking()
            self.assert_notification('Saved successfully!')
            self.close_voucher()
            if expected_posting:
                self.assert_posting_data(**expected_posting)
            transaction_references=self.fo_get_text('Transaction references')
            print(f'Transaction references DPT_FEE: {transaction_references}')
            account_number_mask=self.fo_get_value_group('Account number')
            print(f'Account number: {account_number_mask}')
            return transaction_references, account_number_mask

    # DPT_FOC: 1184: Fee collection by cash for DD
    def dpt_foc(self, account_number, account_holding_branch_name=None, customer_code=None, amount_for_fee_calculation=None, ifc_codes=None, values=None, total_fee=None, total_fee_amount=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.open_fo('DPT_FOC', '1184')
        self.wait_for_button_available('Accept')
        self.assert_form_title('1184: Fee collection by cash for DD')
        # enter value
        self.fo_write_group('Account number', str(account_number).replace('-', ''))
        self.wait_loading()
        if account_holding_branch_name:
            self.fo_assert_text('Account holding branch name', account_holding_branch_name)
        if customer_code:
            self.fo_assert_value('Customer code', customer_code)
        if amount_for_fee_calculation:
            self.fo_write_number('Amount for fee calculation', str(amount_for_fee_calculation).replace(',', ''))
            if self.fo_get_value('Amount for fee calculation')!= amount_for_fee_calculation:
                self.fo_write_number('Amount for fee calculation', str(amount_for_fee_calculation).replace(',', ''))
        # add fee
        if ifc_codes:
            self.add_fees(ifc_codes, values, total_fee=total_fee)
        if total_fee_amount:
            self.fo_assert_value('Total fee amount', total_fee_amount)
        self.fo_write_text('Description', 'AUTO TEST')
        self.wait_loading()
        self.fo_click_checkbox('Caution!  There is no doubt that banks may be used as a means of Money Laundering/ Terrorist Financing/ Proliferation of Weapons of Mass Destruction.')
        # click 'Accept'
        self.click_button('Accept')
        # approve
        if approve_later=='Y':
            self.click_button('Later')
        if approve_on_form=='Y':
            self.fo_approve_in_popup(
                username=username,
                password=password,
                reason=reason
            )
        if list_error_message:
        # verify error
            self.assert_error_message()
            self.assert_list_error_message(list_error_message)
            print('Transaction failed!')
        else:
        # verify success
            self.assert_button_disable('Accept')
            self.switch_to_core_banking()
            self.assert_notification('Saved successfully!')
            self.close_voucher()
            if expected_posting:
                self.assert_posting_data(**expected_posting)
            transaction_references=self.fo_get_text('Transaction references')
            print(f'Transaction references DPT_FOC: {transaction_references}')
            account_number_mask=self.fo_get_value_group('Account number')
            print(f'Account number: {account_number_mask}')
            return transaction_references, account_number_mask

    # DPT_RCTM: Change deposit account name and relation customers
    def dpt_rctm(self, account_number, new_account_name, new_relation_customers=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.open_fo('DPT_RCTM', 'Change Deposit')
        self.wait_for_button_available('Accept')
        self.assert_form_title('DPT - Change Deposit Account Name And Relation Customers')
        # enter value
        self.fo_write_group('Account number', str(account_number).replace('-', ''))
        self.wait_loading()
        self.fo_write_text('New account name', new_account_name)
        if new_relation_customers:
            self.fo_select_multi('New relation customers', new_relation_customers)
        self.fo_write_text('Description', 'AUTO TEST')
        if ifc_codes:
            self.add_fees(ifc_codes, values, total_fee)
        self.wait_loading()
        self.fo_click_checkbox('Caution!  There is no doubt that banks may be used as a means of Money Laundering/ Terrorist Financing/ Proliferation of Weapons of Mass Destruction.')
        # click 'Accept'
        self.click_button('Accept')
        # approve
        if approve_later=='Y':
            self.click_button('Later')
        if approve_on_form=='Y':
            self.fo_approve_in_popup(
                username=username,
                password=password,
                reason=reason
            )
        if list_error_message:
        # verify error
            self.assert_error_message()
            self.assert_list_error_message(list_error_message)
            print('Transaction failed!')
        else:
        # verify success
            self.assert_button_disable('Accept')
            self.assert_notification("Saved successfully!")
            if expected_posting:
                self.assert_posting_data(**expected_posting)
            transaction_references=self.fo_get_text('Transaction references')
            print(f'Transaction references DPT_RCTM: {transaction_references}')
            account_number_mask=self.fo_get_value_group('Account number')
            print(f'Account number: {account_number_mask}')
            return transaction_references, account_number_mask

    # DPT_CLS: 1193: Close deposit account
    def dpt_cls(self, account_number, account_holding_branch_name=None, passbook_number=None, balance=None, interest_payable_receivable=None, interest_due=None, interest_re_calculate=None, gross_paid_interest_amount=None, penalty_fee=None, balance_received=None, gross_paid_interest_amount_update=None, balance_received_update=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.open_fo('DPT_CLS', '1193')
        self.wait_for_button_available('Accept')
        self.assert_form_title('1193: Close deposit account')
        # enter value
        self.fo_write_group('Account number', str(account_number).replace('-', ''))
        self.wait_loading()
        if account_holding_branch_name:
            self.fo_assert_text('Account holding branch name', account_holding_branch_name)
        if passbook_number:
            self.fo_assert_text('Passbook number', passbook_number)
        if balance:
            self.fo_assert_value('Balance', balance)
        if interest_payable_receivable:
            self.fo_assert_value('Interest payable/receivable', interest_payable_receivable)
        if interest_due:
            self.fo_assert_value('Interest due', interest_due)
        if interest_re_calculate:
            self.fo_assert_value('Interest re-calculate', interest_re_calculate)
        if gross_paid_interest_amount:
            self.fo_assert_value('Gross paid interest amount', gross_paid_interest_amount)
        if penalty_fee:
            self.fo_assert_value('Penalty fee', penalty_fee)
        if balance_received:
            self.fo_assert_value('Balance received', balance_received)
        if gross_paid_interest_amount_update:
            self.fo_write_number('Gross paid interest amount', str(gross_paid_interest_amount_update).replace(',', ''))
            if self.fo_get_value('Gross paid interest amount')!= gross_paid_interest_amount_update:
                self.fo_write_number('Gross paid interest amount', str(gross_paid_interest_amount_update).replace(',', ''))
        if balance_received_update:
            self.fo_assert_value('Balance received', balance_received_update)
        self.wait_loading()
        if ifc_codes:
            self.add_fees(ifc_codes, values, total_fee)
        self.fo_write_text('Description', 'AUTO TEST')
        self.wait_loading()
        self.fo_click_checkbox('Caution!  There is no doubt that banks may be used as a means of Money Laundering/ Terrorist Financing/ Proliferation of Weapons of Mass Destruction.')
        # click 'Accept'
        self.click_button('Accept')
        # approve
        if approve_later=='Y':
            self.click_button('Later')
        if approve_on_form=='Y':
            self.fo_approve_in_popup(
                username=username,
                password=password,
                reason=reason
            )
        if list_error_message:
        # verify error
            self.assert_error_message()
            self.assert_list_error_message(list_error_message)
            print('Transaction failed!')
        else:
        # verify success
            self.assert_button_disable('Accept')
            self.switch_to_core_banking()
            self.assert_notification('Saved successfully!')
            self.close_voucher()
            if expected_posting:
                self.assert_posting_data(**expected_posting)
            transaction_references=self.fo_get_text('Transaction references')
            print(f'Transaction references DPT_CLS: {transaction_references}')
            deposit_account_mask=self.fo_get_value_group('Account number')
            print(f'Account number: {deposit_account_mask}')
            return transaction_references, deposit_account_mask

    # DPT_DLS: 1190: Close deposit account by deposit
    def dpt_dls(self, account_number, another_deposit_account, account_holding_branch_name=None, passbook_number=None, balance=None, interest_payable_receivable=None, interest_due=None, interest_re_calculate=None, gross_paid_interest_amount=None, penalty_fee=None, balance_received=None, gross_paid_interest_amount_update=None, balance_received_update=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.open_fo('DPT_DLS', '1190')
        self.wait_for_button_available('Accept')
        self.assert_form_title('1190: Close deposit account by deposit')
        # enter value
        self.fo_write_group('Account number', str(account_number).replace('-', ''))
        self.wait_loading()
        self.fo_write_group('Another deposit account', str(another_deposit_account).replace('-', ''))
        self.wait_loading()
        self.fo_write_text('Description', 'AUTO TEST')
        if account_holding_branch_name:
            self.fo_assert_text('Account holding branch name', account_holding_branch_name)
        if passbook_number:
            self.fo_assert_text('Passbook number', passbook_number)
        if balance:
            self.fo_assert_value('Balance', balance)
        if interest_payable_receivable:
            self.fo_assert_value('Interest payable/receivable', interest_payable_receivable)
        if interest_due:
            self.fo_assert_value('Interest due', interest_due)
        if interest_re_calculate:
            self.fo_assert_value('Interest re-calculate', interest_re_calculate)
        if gross_paid_interest_amount:
            self.fo_assert_value('Gross interest paid out', gross_paid_interest_amount)
        if penalty_fee:
            self.fo_assert_value('Penalty fee', penalty_fee)
        if balance_received:
            self.fo_assert_value('Balance received', balance_received)
        if gross_paid_interest_amount_update:
            self.fo_write_number('Gross interest paid out', str(gross_paid_interest_amount_update).replace(',', ''))
            if self.fo_get_value('Gross interest paid out')!= gross_paid_interest_amount_update:
                self.fo_write_number('Gross interest paid out', str(gross_paid_interest_amount_update).replace(',', ''))
        if balance_received_update:
            self.fo_assert_value('Balance received', balance_received_update)
        self.wait_loading()
        self.fo_write_text('Description', 'AUTO TEST')
        if ifc_codes:
            self.add_fees(ifc_codes, values, total_fee)
        self.wait_loading()
        self.fo_click_checkbox('Caution!  There is no doubt that banks may be used as a means of Money Laundering/ Terrorist Financing/ Proliferation of Weapons of Mass Destruction.')
        # click 'Accept'
        self.click_button('Accept')
        # approve
        if approve_later=='Y':
            self.click_button('Later')
        if approve_on_form=='Y':
            self.fo_approve_in_popup(
                username=username,
                password=password,
                reason=reason
            )
        if list_error_message:
        # verify error
            self.assert_error_message()
            self.assert_list_error_message(list_error_message)
            print('Transaction failed!')
        else:
        # verify success
            self.assert_button_disable('Accept')
            self.switch_to_core_banking()
            self.assert_notification('Saved successfully!')
            self.close_voucher()
            if expected_posting:
                self.assert_posting_data(**expected_posting)
            transaction_references=self.fo_get_text('Transaction references')
            print(f'Transaction references DPT_DLS: {transaction_references}')
            deposit_account_mask=self.fo_get_value_group('Account number')
            print(f'Account number: {deposit_account_mask}')
            another_deposit_account_mask=self.fo_get_value_group('Another deposit account')
            print(f'Another deposit account: {another_deposit_account_mask}')
            return transaction_references, deposit_account_mask, another_deposit_account_mask

    # DPT_MLS: 1191: Close deposit account by miscellaneous
    def dpt_mls(self, account_number, accounting_number, account_holding_branch_name=None, passbook_number=None, balance=None, interest_payable_receivable=None, interest_due=None, interest_re_calculate=None, gross_paid_interest_amount=None, penalty_fee=None, balance_received=None, gross_paid_interest_amount_update=None, balance_received_update=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.open_fo('DPT_MLS', '1191')
        self.wait_for_button_available('Accept')
        self.assert_form_title('1191: Close deposit account by miscellaneous')
        # enter value
        self.fo_write_group('Account number', str(account_number).replace('-', ''))
        self.wait_loading()
        self.fo_write_group('Accounting number', str(accounting_number).replace('-', ''))
        self.wait_loading()
        self.fo_write_text('Description', 'AUTO TEST')
        if account_holding_branch_name:
            self.fo_assert_text('Account holding branch name', account_holding_branch_name)
        if passbook_number:
            self.fo_assert_text('Passbook number', passbook_number)
        if balance:
            self.fo_assert_value('Balance', balance)
        if interest_payable_receivable:
            self.fo_assert_value('Interest payable/receivable', interest_payable_receivable)
        if interest_due:
            self.fo_assert_value('Interest due', interest_due)
        if interest_re_calculate:
            self.fo_assert_value('Interest re-calculate', interest_re_calculate)
        if gross_paid_interest_amount:
            self.fo_assert_value('Interest amount', gross_paid_interest_amount)
        if penalty_fee:
            self.fo_assert_value('Penalty fee', penalty_fee)
        if balance_received:
            self.fo_assert_value('Balance received', balance_received)
        if gross_paid_interest_amount_update:
            self.fo_write_number('Interest amount', str(gross_paid_interest_amount_update).replace(',', ''))
            if self.fo_get_value('Interest amount')!= gross_paid_interest_amount_update:
                self.fo_write_number('Interest amount', str(gross_paid_interest_amount_update).replace(',', ''))
        if balance_received_update:
            self.fo_assert_value('Balance received', balance_received_update)
        self.wait_loading()
        self.fo_write_text('Description', 'AUTO TEST')
        if ifc_codes:
            self.add_fees(ifc_codes, values, total_fee)
        self.wait_loading()
        self.fo_click_checkbox('Caution!  There is no doubt that banks may be used as a means of Money Laundering/ Terrorist Financing/ Proliferation of Weapons of Mass Destruction.')
        # click 'Accept'
        self.click_button('Accept')
        # approve
        if approve_later=='Y':
            self.click_button('Later')
        if approve_on_form=='Y':
            self.fo_approve_in_popup(
                username=username,
                password=password,
                reason=reason
            )
        if list_error_message:
        # verify error
            self.assert_error_message()
            self.assert_list_error_message(list_error_message)
            print('Transaction failed!')
        else:
        # verify success
            self.assert_button_disable('Accept')
            self.switch_to_core_banking()
            self.assert_notification('Saved successfully!')
            self.close_voucher()
            if expected_posting:
                self.assert_posting_data(**expected_posting)
            transaction_references=self.fo_get_text('Transaction references')
            print(f'Transaction references DPT_MLS: {transaction_references}')
            deposit_account_mask=self.fo_get_value_group('Account number')
            print(f'Account number: {deposit_account_mask}')
            accounting_number_mask=self.fo_get_value_group('Accounting number')
            print(f'Accounting number: {accounting_number_mask}')
            return transaction_references, deposit_account_mask, accounting_number_mask

    # DPT_HIS: 1160: Transaction history inquiry
    def dpt_his(self, account_number, from_date=None, to_date=None, transaction_codes=None, expected_debits=None, expected_credits=None, expected_balances=None, expected_channels=None, expected_transaction_code=None, expected_transaction_codes=None, expected_debit=None, expected_credit=None, expected_balance=None, expected_channel=None, transaction_numbers=None, expected_transaction_number=None, expected_transaction_dates=None, expected_transaction_date=None, expected_created_bys=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.open_fo('DPT_HIS', '1160')
        self.wait_for_button_available('Accept')
        self.assert_form_title('1160: Transaction history inquiry')
        # enter value
        self.fo_write_group('Account number', str(account_number).replace('-', ''))
        self.wait_loading()
        if from_date:
            self.fo_write_date('From date', from_date)
        if to_date:
            self.fo_write_date('To date', to_date)
        self.fo_write_text('Description', 'AUTO TEST')
        if ifc_codes:
            self.add_fees(ifc_codes, values, total_fee)
        self.wait_loading()
        # click 'Accept'
        self.click_button('Accept')
        # approve
        if approve_later=='Y':
            self.click_button('Later')
        if approve_on_form=='Y':
            self.fo_approve_in_popup(
                username=username,
                password=password,
                reason=reason
            )
        if list_error_message:
        # verify error
            self.assert_error_message()
            self.assert_list_error_message(list_error_message)
            print('Transaction failed!')
        else:
        # verify success
            self.assert_button_disable('Accept')
            self.assert_notification('Saved successfully!')
            # compare value by list transaction code
            if transaction_codes:
                if expected_transaction_dates:
                    for transaction_code, transaction_date in zip(transaction_codes, expected_transaction_dates):
                        self.fo_assert_text_table('Transaction code', transaction_code, 'Transaction date', transaction_date)
                if expected_debits:
                    for transaction_code, debit in zip(transaction_codes, expected_debits):
                        self.fo_assert_text_table('Transaction code', transaction_code, 'Debit', debit)
                if expected_credits:
                    for transaction_code, credit in zip(transaction_codes, expected_credits):
                        self.fo_assert_text_table('Transaction code', transaction_code, 'Credit', credit)
                if expected_balances:
                    for transaction_code, balance in zip(transaction_codes, expected_balances):
                        self.fo_assert_text_table('Transaction code', transaction_code, 'Balance', balance)
                if expected_channels:
                    for transaction_code, channel in zip(transaction_codes, expected_channels):
                        self.fo_assert_text_table('Transaction code', transaction_code, 'Channel', channel)
                if expected_created_bys:
                    for transaction_code, created_by in zip(transaction_codes, expected_created_bys):
                        self.fo_assert_text_table('Transaction code', transaction_code, 'Created by', created_by)
            # compare value by list transaction number
            if transaction_numbers:
                if expected_transaction_codes:
                    for transaction_number, transaction_code in zip(transaction_numbers, expected_transaction_codes):
                        self.fo_assert_text_table('Transaction number', transaction_number, 'Transaction code', transaction_code, xpath_type='preceding')
                if expected_transaction_dates:
                    for transaction_number, transaction_date in zip(transaction_numbers, expected_transaction_dates):
                        self.fo_assert_text_table('Transaction number', transaction_number, 'Transaction date', transaction_date)
                if expected_debits:
                    for transaction_number, debit in zip(transaction_numbers, expected_debits):
                        self.fo_assert_text_table('Transaction number', transaction_number, 'Debit', debit)
                if expected_credits:
                    for transaction_number, credit in zip(transaction_numbers, expected_credits):
                        self.fo_assert_text_table('Transaction number', transaction_number, 'Credit', credit)
                if expected_balances:
                    for transaction_number, balance in zip(transaction_numbers, expected_balances):
                        self.fo_assert_text_table('Transaction number', transaction_number, 'Balance', balance)
                if expected_channels:
                    for transaction_number, channel in zip(transaction_numbers, expected_channels):
                        self.fo_assert_text_table('Transaction number', transaction_number, 'Channel', channel)
                if expected_created_bys:
                    for transaction_number, created_by in zip(transaction_numbers, expected_created_bys):
                        self.fo_assert_text_table('Transaction number', transaction_number, 'Created by', created_by)
                # compare value by transaction number
            if expected_transaction_number:
                if expected_transaction_date:
                    self.fo_assert_text_table('Transaction number', expected_transaction_number, 'Transaction date', expected_transaction_date)
                if expected_debit:
                    self.fo_assert_text_table('Transaction number', expected_transaction_number, 'Debit', expected_debit)
                if expected_credit:
                    self.fo_assert_text_table('Transaction number', expected_transaction_number, 'Credit', expected_credit)
                if expected_balance:
                    self.fo_assert_text_table('Transaction number', expected_transaction_number, 'Balance', expected_balance)
                if expected_channel:
                    self.fo_assert_text_table('Transaction number', expected_transaction_number, 'Channel', expected_channel)
                if expected_transaction_date:
                    self.fo_assert_text_table('Transaction number', expected_transaction_number, 'Transaction date', expected_transaction_date)
                if expected_transaction_code:
                    self.fo_assert_text_table('Transaction number', expected_transaction_number, 'Transaction code', expected_transaction_code, xpath_type='preceding')
            if expected_posting:
                self.assert_posting_data(**expected_posting)
            transaction_references=self.fo_get_text('Transaction references')
            print(f'Transaction references DPT_HIS: {transaction_references}')
            deposit_account_mask=self.fo_get_value_group('Account number')
            print(f'Account number: {deposit_account_mask}')
            return transaction_references, deposit_account_mask

# -------------------------- handle FO - STOCK --------------------------
    # DPT_SRG: 11830: Stock registration
    def dpt_srg(self, stock_type, from_serial, to_serial, stock_prefix, number_of_leaves, number_of_book, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.open_fo('DPT_SRG', '11830')
        self.wait_for_button_available('Accept')
        self.assert_form_title('11830: Stock registration')
        # enter data
        self.fo_select('Stock type', stock_type)
        self.fo_write('From serial', from_serial)
        self.fo_write('To serial', to_serial)
        self.fo_write_text('Description', 'AUTO TEST')
        self.wait_loading()
        self.fo_assert_text('Stock prefix', stock_prefix)
        self.fo_assert_value('Number of leaves', number_of_leaves)
        self.fo_assert_value('Number of book', number_of_book)
        if ifc_codes:
            self.add_fees(ifc_codes, values, total_fee)
        # click 'Accept'
        self.click_button('Accept')
        # approve
        if approve_later=='Y':
            self.click_button('Later')
        if approve_on_form=='Y':
            self.fo_approve_in_popup(
                username=username,
                password=password,
                reason=reason
            )
        if list_error_message:
        # verify error
            self.assert_error_message()
            self.assert_list_error_message(list_error_message)
            print('Transaction failed!')
        else:
        # verify success
            self.assert_button_disable('Accept')
            self.assert_notification("Saved successfully!")
            if expected_posting:
                self.assert_posting_data(**expected_posting)
            transaction_references=self.fo_get_text('Transaction references')
            print(f'Transaction references DPT_SRG: {transaction_references}')
            from_serial_mask=self.fo_get_value('From serial')
            print(f'From serial: {from_serial_mask}')
            to_serial_mask=self.fo_get_value('To serial')
            print(f'To serial: {to_serial_mask}')
            return transaction_references, from_serial_mask, to_serial_mask

    # DPT_SAT: 11832: Stock assign to Staff
    def dpt_sat(self, stock_type, from_serial, to_serial, assigned_staff_code, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.open_fo('DPT_SAT', '11832')
        self.wait_for_button_available('Accept')
        self.assert_form_title('11832: Stock assign to Staff')
        # enter data
        self.fo_select('Stock type', stock_type)
        self.fo_write_text('Description', 'AUTO TEST')
        self.fo_write('From serial', from_serial)
        self.fo_write('To serial', to_serial)
        self.fo_write_group('Assigned staff code', assigned_staff_code)
        self.wait_loading()
        if ifc_codes:
            self.add_fees(ifc_codes, values, total_fee)
        # click 'Accept'
        self.click_button('Accept')
        # approve
        if approve_later=='Y':
            self.click_button('Later')
        if approve_on_form=='Y':
            self.fo_approve_in_popup(
                username=username,
                password=password,
                reason=reason
            )
        if list_error_message:
        # verify error
            self.assert_error_message()
            self.assert_list_error_message(list_error_message)
            print('Transaction failed!')
        else:
        # verify success
            self.assert_button_disable('Accept')
            self.assert_notification("Saved successfully!")
            if expected_posting:
                self.assert_posting_data(**expected_posting)
            transaction_references=self.fo_get_text('Transaction references')
            print(f'Transaction references DPT_SAT: {transaction_references}')
            from_serial_mask=self.fo_get_value('From serial')
            print(f'From serial: {from_serial_mask}')
            to_serial_mask=self.fo_get_value('To serial')
            print(f'To serial: {to_serial_mask}')
            return transaction_references, from_serial_mask, to_serial_mask

    # DPT_CCR: 11834: Stock Confirm Received
    def dpt_ccr(self, stock_type, from_serial, to_serial, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.open_fo('DPT_CCR', '11834')
        self.wait_for_button_available('Accept')
        self.assert_form_title('DPT-11834: Stock Confirm Received')
        # enter data
        self.fo_select('Stock type', stock_type)
        self.fo_write_text('Description', 'AUTO TEST')
        self.fo_write('From serial', from_serial)
        self.fo_write('To serial', to_serial)
        if ifc_codes:
            self.add_fees(ifc_codes, values, total_fee)
        self.wait_loading()
        # click 'Accept'
        self.click_button('Accept')
        # approve
        if approve_later=='Y':
            self.click_button('Later')
        if approve_on_form=='Y':
            self.fo_approve_in_popup(
                username=username,
                password=password,
                reason=reason
            )
        if list_error_message:
        # verify error
            self.assert_error_message()
            self.assert_list_error_message(list_error_message)
            print('Transaction failed!')
        else:
        # verify success
            self.assert_button_disable('Accept')
            self.assert_notification("Saved successfully!")
            if expected_posting:
                self.assert_posting_data(**expected_posting)
            transaction_references=self.fo_get_text('Transaction references')
            print(f'Transaction references DPT_CCR: {transaction_references}')
            from_serial_mask=self.fo_get_value('From serial')
            print(f'From serial: {from_serial_mask}')
            to_serial_mask=self.fo_get_value('To serial')
            print(f'To serial: {to_serial_mask}')
            return transaction_references, from_serial_mask, to_serial_mask

    # DPT_SRA: 11835: Reject assigned stock
    def dpt_sra(self, stock_type, from_serial, to_serial, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.open_fo('DPT_SRA', '11835')
        self.wait_for_button_available('Accept')
        self.assert_form_title('DPT-11835: Reject Assigned Stock')
        # enter value
        self.fo_select('Stock type', stock_type)
        self.fo_write_text('Description', 'AUTO TEST')
        self.fo_write('From serial', from_serial)
        self.fo_write('To serial', to_serial)
        if ifc_codes:
            self.add_fees(ifc_codes, values, total_fee)
        self.wait_loading()
        # click 'Accept'
        self.click_button('Accept')
        # approve
        if approve_later=='Y':
            self.click_button('Later')
        if approve_on_form=='Y':
            self.fo_approve_in_popup(
                username=username,
                password=password,
                reason=reason
            )
        if list_error_message:
        # verify error
            self.assert_error_message()
            self.assert_list_error_message(list_error_message)
            print('Transaction failed!')
        else:
        # verify success
            self.assert_button_disable('Accept')
            self.assert_notification("Saved successfully!")
            if expected_posting:
                self.assert_posting_data(**expected_posting)
            transaction_references=self.fo_get_text('Transaction references')
            print(f'Transaction references DPT_SRA: {transaction_references}')
            from_serial_mask=self.fo_get_value('From serial')
            print(f'From serial: {from_serial_mask}')
            to_serial_mask=self.fo_get_value('To serial')
            print(f'To serial: {to_serial_mask}')
            return transaction_references, from_serial_mask, to_serial_mask

    # DPT_CRT: 11833: Stock returned
    def dpt_crt(self, stock_type, from_serial, to_serial, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.open_fo('DPT_CRT', '11833')
        self.wait_for_button_available('Accept')
        self.assert_form_title('11833: Stock returned')
        # enter value
        self.fo_select('Stock type', stock_type)
        self.fo_write_text('Description', 'AUTO TEST')
        self.fo_write('From serial', from_serial)
        self.fo_write('To serial', to_serial)
        if ifc_codes:
            self.add_fees(ifc_codes, values, total_fee)
        self.wait_loading()
        # click 'Accept'
        self.click_button('Accept')
        # approve
        if approve_later=='Y':
            self.click_button('Later')
        if approve_on_form=='Y':
            self.fo_approve_in_popup(
                username=username,
                password=password,
                reason=reason
            )
        if list_error_message:
        # verify error
            self.assert_error_message()
            self.assert_list_error_message(list_error_message)
            print('Transaction failed!')
        else:
        # verify success
            self.assert_button_disable('Accept')
            self.assert_notification("Saved successfully!")
            if expected_posting:
                self.assert_posting_data(**expected_posting)
            transaction_references=self.fo_get_text('Transaction references')
            print(f'Transaction references DPT_CRT: {transaction_references}')
            from_serial_mask=self.fo_get_value('From serial')
            print(f'From serial: {from_serial_mask}')
            to_serial_mask=self.fo_get_value('To serial')
            print(f'To serial: {to_serial_mask}')
            return transaction_references, from_serial_mask, to_serial_mask

    # DPT_SAB: DPT-11831: Stock Assigned To Branch
    def dpt_sab(self, stock_type, from_serial, to_serial, branch_code, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.open_fo('DPT_SAB', '11831')
        self.wait_for_button_available('Accept')
        self.assert_form_title('DPT-11831: Stock Assigned To Branch')
        # enter data
        self.fo_select('Stock type', stock_type)
        self.fo_write_text('Description', ' AUTO TEST')
        self.fo_write('From serial', from_serial)
        self.fo_write('To serial', to_serial)
        self.fo_write_group('Branch code', branch_code)
        if ifc_codes:
            self.add_fees(ifc_codes, values, total_fee)
        self.wait_loading()
        # click 'Accept'
        self.click_button('Accept')
        # approve
        if approve_later=='Y':
            self.click_button('Later')
        if approve_on_form=='Y':
            self.fo_approve_in_popup(
                username=username,
                password=password,
                reason=reason
            )
        if list_error_message:
        # verify error
            self.assert_error_message()
            self.assert_list_error_message(list_error_message)
            print('Transaction failed!')
        else:
        # verify success
            self.assert_button_disable('Accept')
            self.assert_notification("Saved successfully!")
            if expected_posting:
                self.assert_posting_data(**expected_posting)
            transaction_references=self.fo_get_text('Transaction references')
            print(f'Transaction references DPT_SAB: {transaction_references}')
            from_serial_mask=self.fo_get_value('From serial')
            print(f'From serial: {from_serial_mask}')
            to_serial_mask=self.fo_get_value('To serial')
            print(f'To serial: {to_serial_mask}')
            branch_code_assign=self.fo_get_value_group('Branch code')
            print(f'Branch code: {branch_code_assign}')
            return transaction_references, from_serial_mask, to_serial_mask, branch_code_assign

    # DPT_CIS: 11801: Cheque book issued
    def dpt_cis(self, account_number, from_serial, to_serial, number_of_leaves=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.open_fo('DPT_CIS', '11801')
        self.wait_for_button_available('Accept')
        self.assert_form_title('11801: Cheque book issued')
        # enter data
        self.fo_write_group('Account number', str(account_number).replace('-', ''))
        self.wait_loading()
        self.fo_write('From serial', from_serial)
        self.fo_write('To serial', to_serial)
        self.wait_loading()
        self.fo_write_text('Description', 'AUTO TEST')
        if number_of_leaves:
            self.fo_assert_value('Number of leaves', number_of_leaves)
        if ifc_codes:
            self.add_fees(ifc_codes, values, total_fee)
        self.wait_loading()
        self.fo_click_checkbox('Caution!  There is no doubt that banks may be used as a means of Money Laundering/ Terrorist Financing/ Proliferation of Weapons of Mass Destruction.')
        self.wait_loading()
        # click 'Accept'
        self.click_button('Accept')
        # approve
        if approve_later=='Y':
            self.click_button('Later')
        if approve_on_form=='Y':
            self.fo_approve_in_popup(
                username=username,
                password=password,
                reason=reason
            )
        if list_error_message:
        # verify error
            self.assert_error_message()
            self.assert_list_error_message(list_error_message)
            print('Transaction failed!')
        else:
        # verify success
            self.assert_button_disable('Accept')
            self.switch_to_core_banking()
            self.assert_notification('Saved successfully!')
            self.close_voucher()
            if expected_posting:
                self.assert_posting_data(**expected_posting)
            transaction_references=self.fo_get_text('Transaction references')
            print(f'Transaction references DPT_CIS: {transaction_references}')
            deposit_account_mask=self.fo_get_value_group('Account number')
            print(f'Account number: {deposit_account_mask}')
            from_serial_mask=self.fo_get_value('From serial')
            print(f'From serial: {from_serial_mask}')
            to_serial_mask=self.fo_get_value('To serial')
            print(f'To serial: {to_serial_mask}')
            return transaction_references, from_serial_mask, to_serial_mask

    # DPT_CEI: 11850:Issued hold balance for cheque
    def dpt_cei(self, cheque_no, cheque_amount, account_number=None, account_holding_branch_name=None, purpose_of_hold_amount=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.open_fo('DPT_CEI', '11850')
        self.wait_for_button_available('Accept')
        self.assert_form_title('11850:Issued hold balance for cheque')
        # enter value
        self.fo_write('Cheque no', cheque_no)
        self.wait_loading()
        self.fo_write_number('Cheque amount', str(cheque_amount).replace(',', ''))
        if self.fo_get_value('Cheque amount')!= cheque_amount:
            self.fo_write_number('Cheque amount', str(cheque_amount).replace(',', ''))
        self.wait_loading()
        if account_number:
            self.fo_assert_value_group('Account number', account_number)
        if account_holding_branch_name:
            self.fo_assert_text('Account holding branch name', account_holding_branch_name)
        if purpose_of_hold_amount:
            self.fo_select('Purpose of hold amount', purpose_of_hold_amount)
        self.key_escape()
        self.wait_loading()
        self.fo_write_text('Description', 'AUTO TEST')
        if ifc_codes:
            self.add_fees(ifc_codes, values, total_fee)
        self.wait_loading()
        self.fo_click_checkbox('Caution!  There is no doubt that banks may be used as a means of Money Laundering/ Terrorist Financing/ Proliferation of Weapons of Mass Destruction.')
        self.wait_loading()
        # click 'Accept'
        self.click_button('Accept')
        # approve
        if approve_later=='Y':
            self.click_button('Later')
        if approve_on_form=='Y':
            self.fo_approve_in_popup(
                username=username,
                password=password,
                reason=reason
            )
        if list_error_message:
        # verify error
            self.assert_error_message()
            self.assert_list_error_message(list_error_message)
            print('Transaction failed!')
        else:
        # verify success
            self.assert_button_disable('Accept')
            self.assert_notification('Saved successfully!')
            self.close_voucher()
            if expected_posting:
                self.assert_posting_data(**expected_posting)
            transaction_references=self.fo_get_text('Transaction references')
            print(f'Transaction references DPT_CEI: {transaction_references}')
            cheque_no_mask=self.fo_get_value('Cheque no')
            print(f'Cheque no: {cheque_no_mask}')
            deposit_account_mask=self.fo_get_value_group('Account number')
            print(f'Account number: {deposit_account_mask}')
            return transaction_references, cheque_no_mask, deposit_account_mask

    # DPT_REC: 11852:Release hold balance for cheque
    def dpt_rec(self, cheque_no, cheque_amount, account_number=None, account_holding_branch_name=None, purpose_of_hold_amount=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.open_fo('DPT_REC', '11852')
        self.wait_for_button_available('Accept')
        self.assert_form_title('11852:Release hold balance for cheque')
        # enter value
        self.fo_write('Cheque no', cheque_no)
        self.wait_loading()
        self.fo_write_number('Cheque amount', str(cheque_amount).replace(',', ''))
        if self.fo_get_value('Cheque amount')!= cheque_amount:
            self.fo_write_number('Cheque amount', str(cheque_amount).replace(',', ''))
        self.wait_loading()
        if account_number:
            self.fo_assert_value_group('Account number', account_number)
        if account_holding_branch_name:
            self.fo_assert_text('Account holding branch name', account_holding_branch_name)
        if purpose_of_hold_amount:
            self.fo_select('Purpose of hold amount', purpose_of_hold_amount)
        self.key_escape()
        self.wait_loading()
        self.fo_write_text('Description', 'AUTO TEST')
        if ifc_codes:
            self.add_fees(ifc_codes, values, total_fee)
        self.wait_loading()
        self.fo_click_checkbox('Caution!  There is no doubt that banks may be used as a means of Money Laundering/ Terrorist Financing/ Proliferation of Weapons of Mass Destruction.')
        self.wait_loading()
        # click 'Accept'
        self.click_button('Accept')
        # approve
        if approve_later=='Y':
            self.click_button('Later')
        if approve_on_form=='Y':
            self.fo_approve_in_popup(
                username=username,
                password=password,
                reason=reason
            )
        if list_error_message:
        # verify error
            self.assert_error_message()
            self.assert_list_error_message(list_error_message)
            print('Transaction failed!')
        else:
        # verify success
            self.assert_button_disable('Accept')
            self.assert_notification('Saved successfully!')
            self.close_voucher()
            if expected_posting:
                self.assert_posting_data(**expected_posting)
            transaction_references=self.fo_get_text('Transaction references')
            print(f'Transaction references DPT_REC: {transaction_references}')
            cheque_no_mask=self.fo_get_value('Cheque no')
            print(f'Cheque no: {cheque_no_mask}')
            deposit_account_mask=self.fo_get_value_group('Account number')
            print(f'Account number: {deposit_account_mask}')
            return transaction_references, cheque_no_mask, deposit_account_mask

    # DPT_CDT: 1111: Deposit by cheque
    def dpt_cdt(self, cheque_no, debit_amount, credit_account, debit_account=None, account_holding_branch_name=None, balance=None, available_balance=None, debit_account_name=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.open_fo('DPT_CDT', '1111')
        self.wait_for_button_available('Accept')
        self.assert_form_title('1111: Deposit by cheque')
        # enter value
        self.fo_write('Cheque no', cheque_no)
        self.fo_write_number('Debit amount', str(debit_amount).replace(',', ''))
        if self.fo_get_value('Debit amount')!= debit_amount:
            self.fo_write_number('Debit amount', str(debit_amount).replace(',', ''))
        self.fo_write_group('Credit account', str(credit_account).replace('-', ''))
        if debit_account:
            self.fo_assert_value_group('Debit account', debit_account)
        if account_holding_branch_name:
            self.fo_assert_text('Account holding branch name', account_holding_branch_name)
        if balance:
            self.fo_assert_value('Balance', balance)
        if available_balance:
            self.fo_assert_value('Available balance', available_balance)
        if debit_account_name:
            self.fo_assert_value('Debit account name', debit_account_name)
        # self.key_escape()
        self.fo_write_text('Description', 'AUTO TEST')
        if ifc_codes:
            self.add_fees(ifc_codes, values, total_fee)
        self.wait_loading()
        self.fo_click_checkbox('Caution!  There is no doubt that banks may be used as a means of Money Laundering/ Terrorist Financing/ Proliferation of Weapons of Mass Destruction.')
        # click 'Accept'
        self.click_button('Accept')
        # approve
        if approve_later=='Y':
            self.click_button('Later')
        if approve_on_form=='Y':
            self.fo_approve_in_popup(
                username=username,
                password=password,
                reason=reason
            )
        if list_error_message:
        # verify error
            self.assert_error_message()
            self.assert_list_error_message(list_error_message)
            print('Transaction failed!')
        else:
        # verify success
            self.assert_button_disable('Accept')
            self.assert_notification('Saved successfully!')
            self.close_voucher()
            if expected_posting:
                self.assert_posting_data(**expected_posting)
            transaction_references=self.fo_get_text('Transaction references')
            print(f'Transaction references DPT_CDT: {transaction_references}')
            cheque_no_mask=self.fo_get_value('Cheque no')
            print(f'Cheque no: {cheque_no_mask}')
            debit_account_mask=self.fo_get_value_group('Debit account')
            print(f'Debit account: {debit_account_mask}')
            credit_account_mask=self.fo_get_value_group('Credit account')
            print(f'Credit account: {credit_account_mask}')
            return transaction_references, cheque_no_mask, credit_account_mask

    # DPT_CWC: 1121: Cash withdrawal by cheque
    def dpt_cwc(self, cheque_no, cheque_amount, account_number=None, account_holding_branch_name=None, current_balance=None, available_balance=None, withdrawer_name=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.open_fo('DPT_CWC', '1121')
        self.wait_for_button_available('Accept')
        self.assert_form_title('1121: Cash withdrawal by cheque')
        # enter value
        self.fo_write('Cheque no', cheque_no)
        self.wait_loading()
        self.fo_write_number('Cheque amount', str(cheque_amount).replace(',', ''))
        if self.fo_get_value('Cheque amount')!= cheque_amount:
            self.fo_write_number('Cheque amount', str(cheque_amount).replace(',', ''))
        self.wait_loading()
        if account_number:
            self.fo_assert_value_group('Account number', account_number)
        if account_holding_branch_name:
            self.fo_assert_text('Account holding branch name', account_holding_branch_name)
        if current_balance:
            self.fo_assert_value('Current balance', current_balance)
        if available_balance:
            self.fo_assert_value('Available balance', available_balance)
        if withdrawer_name:
            self.fo_assert_value('Withdrawer name', withdrawer_name)
        # self.key_escape()
        self.fo_write_text('Description', 'AUTO TEST')
        if ifc_codes:
            self.add_fees(ifc_codes, values, total_fee)
        self.wait_loading()
        self.fo_click_checkbox('Caution!  There is no doubt that banks may be used as a means of Money Laundering/ Terrorist Financing/ Proliferation of Weapons of Mass Destruction.')
        self.wait_loading()
        # click 'Accept'
        self.click_button('Accept')
        # approve
        if approve_later=='Y':
            self.click_button('Later')
        if approve_on_form=='Y':
            self.fo_approve_in_popup(
                username=username,
                password=password,
                reason=reason
            )
        if list_error_message:
        # verify error
            self.assert_error_message()
            self.assert_list_error_message(list_error_message)
            print('Transaction failed!')
        else:
        # verify success
            self.assert_button_disable('Accept')
            self.assert_notification('Saved successfully!')
            self.close_voucher()
            if expected_posting:
                self.assert_posting_data(**expected_posting)
            transaction_references=self.fo_get_text('Transaction references')
            print(f'Transaction references DPT_CWC: {transaction_references}')
            cheque_no_mask=self.fo_get_value('Cheque no')
            print(f'Cheque no: {cheque_no_mask}')
            deposit_account_mask=self.fo_get_value_group('Account number')
            print(f'Account number: {deposit_account_mask}')
            return transaction_references, cheque_no_mask, deposit_account_mask

    # DPT_CWM: 1125: Misellaneous debit by cheque
    def dpt_cwm(self, cheque_no, cheque_amount, credit_accounting, account_number=None, account_holding_branch_name=None, current_balance=None, available_balance=None, accounting_amount=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.open_fo('DPT_CWM', '1125')
        self.wait_for_button_available('Accept')
        self.assert_form_title('1125: Misellaneous debit by cheque')
        # enter value
        self.fo_write('Cheque no', cheque_no)
        self.wait_loading()
        self.fo_write_number('Cheque amount', str(cheque_amount).replace(',', ''))
        if self.fo_get_value('Cheque amount')!= cheque_amount:
            self.fo_write_number('Cheque amount', str(cheque_amount).replace(',', ''))
        self.wait_loading()
        self.fo_write_group('Credit accounting', str(credit_accounting).replace('-', ''))
        self.wait_loading()
        if account_number:
            self.fo_assert_value_group('Account number', account_number)
        if account_holding_branch_name:
            self.fo_assert_text('Account holding branch name', account_holding_branch_name)
        if current_balance:
            self.fo_assert_value('Current balance', current_balance)
        if available_balance:
            self.fo_assert_value('Available balance', available_balance)
        if accounting_amount:
            self.fo_assert_value('Accounting amount', accounting_amount)
        # self.key_escape()
        self.fo_write_text('Description', 'AUTO TEST')
        if ifc_codes:
            self.add_fees(ifc_codes, values, total_fee)
        self.wait_loading()
        self.fo_click_checkbox('Caution!  There is no doubt that banks may be used as a means of Money Laundering/ Terrorist Financing/ Proliferation of Weapons of Mass Destruction.')
        self.wait_loading()
        # click 'Accept'
        self.click_button('Accept')
        # approve
        if approve_later=='Y':
            self.click_button('Later')
        if approve_on_form=='Y':
            self.fo_approve_in_popup(
                username=username,
                password=password,
                reason=reason
            )
        if list_error_message:
        # verify error
            self.assert_error_message()
            self.assert_list_error_message(list_error_message)
            print('Transaction failed!')
        else:
        # verify success
            self.assert_button_disable('Accept')
            self.assert_notification('Saved successfully!')
            self.close_voucher()
            if expected_posting:
                self.assert_posting_data(**expected_posting)
            transaction_references=self.fo_get_text('Transaction references')
            print(f'Transaction references DPT_CWM: {transaction_references}')
            cheque_no_mask=self.fo_get_value('Cheque no')
            print(f'Cheque no: {cheque_no_mask}')
            deposit_account_mask=self.fo_get_value_group('Account number')
            print(f'Account number: {deposit_account_mask}')
            credit_accounting_mask=self.fo_get_value_group('Credit accounting')
            print(f'Credit accounting: {credit_accounting_mask}')
            return transaction_references, cheque_no_mask, credit_accounting_mask

    # DPT_CTS: 11837: Change status of stock
    def dpt_cts(self, account_number, stock_type, from_serial, to_serial, status, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.open_fo('DPT_CTS', '11837')
        self.wait_for_button_available('Accept')
        self.assert_form_title('11837: Change status of stock')
        # enter data
        self.fo_write_group('Account number', str(account_number).replace('-', ''))
        self.wait_loading()
        self.fo_select('Stock type', stock_type)
        self.fo_write('From serial', str(from_serial).replace('-', ''))
        self.fo_write('To serial', str(to_serial).replace('-', ''))
        self.wait_loading()
        self.fo_select('Status', status)
        self.fo_write_text('Description', 'AUTO TEST')
        if ifc_codes:
            self.add_fees(ifc_codes, values, total_fee)
        self.wait_loading()
        self.fo_click_checkbox('Caution!  There is no doubt that banks may be used as a means of Money Laundering/ Terrorist Financing/ Proliferation of Weapons of Mass Destruction.')
        self.wait_loading()
        # click 'Accept'
        self.click_button('Accept')
        # approve
        if approve_later=='Y':
            self.click_button('Later')
        if approve_on_form=='Y':
            self.fo_approve_in_popup(
                username=username,
                password=password,
                reason=reason
            )
        if list_error_message:
        # verify error
            self.assert_error_message()
            self.assert_list_error_message(list_error_message)
            print('Transaction failed!')
        else:
        # verify success
            self.assert_button_disable('Accept')
            self.assert_notification('Saved successfully!')
            self.close_voucher()
            if expected_posting:
                self.assert_posting_data(**expected_posting)
            transaction_references=self.fo_get_text('Transaction references')
            print(f'Transaction references DPT_CTS: {transaction_references}')
            deposit_account_mask=self.fo_get_value_group('Account number')
            print(f'Account number: {deposit_account_mask}')
            from_serial_mask=self.fo_get_value('From serial')
            print(f'From serial: {from_serial_mask}')
            to_serial_mask=self.fo_get_value('To serial')
            print(f'To serial: {to_serial_mask}')
            return transaction_references, from_serial_mask, to_serial_mask

    # DPT_CIQ: 1167: Cheque inquiry
    def dpt_ciq(self, account_number, serial_number, serial_numbers=None, expected_values=None, expected_serial_number=None, expected_value=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.open_fo('DPT_CIQ', '1167')
        self.wait_for_button_available('Accept')
        self.assert_form_title('1167: Cheque inquiry')
        # enter value
        self.fo_write_group('Account number', str(account_number).replace('-', ''))
        self.wait_loading()
        self.fo_write('Serial number', serial_number)
        if ifc_codes:
            self.add_fees(ifc_codes, values, total_fee)
        self.wait_loading()
        # click 'Accept'
        self.click_button('Accept')
        # approve
        if approve_later=='Y':
            self.click_button('Later')
        if approve_on_form=='Y':
            self.fo_approve_in_popup(
                username=username,
                password=password,
                reason=reason
            )
        if list_error_message:
        # verify error
            self.assert_error_message()
            self.assert_list_error_message(list_error_message)
            print('Transaction failed!')
        else:
        # verify success
            self.assert_button_disable('Accept')
            self.assert_notification('Saved successfully!')
            # compare value
            if serial_numbers:
                for serial_no, expected in zip(serial_numbers, expected_values):
                    self.fo_assert_text_table('Serial No.', str(serial_no).replace('-',''), 'Status', expected)
            if expected_serial_number:
                self.fo_assert_text_table('Serial No.', str(expected_serial_number).replace('-',''), 'Status', expected_value)
            if expected_posting:
                self.assert_posting_data(**expected_posting)
            transaction_references=self.fo_get_text('Transaction references')
            print(f'Transaction references DPT_CIQ: {transaction_references}')
            deposit_account_mask=self.fo_get_value_group('Account number')
            print(f'Account number: {deposit_account_mask}')
            serial_number_mask=self.fo_get_value('Serial number')
            print(f'Serial number: {serial_number_mask}')
            return transaction_references, serial_number_mask

    # DPT_SLS: DPT-1162: Cheque Leaves Status Inquiry
    def dpt_sls(self, from_serial, to_serial, serial_numbers=None, expected_values=None, expected_serial_number=None, expected_value=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.open_fo('DPT_SLS', '1162')
        self.wait_for_button_available('Accept')
        self.assert_form_title('DPT-1162: Cheque Leaves Status Inquiry')
        # enter value
        self.fo_write('From serial', str(from_serial).replace('-', ''))
        self.wait_loading()
        self.fo_write('To serial', str(to_serial).replace('-', ''))
        if ifc_codes:
            self.add_fees(ifc_codes, values, total_fee)
        self.wait_loading()
        # click 'Accept'
        self.click_button('Accept')
        # approve
        if approve_later=='Y':
            self.click_button('Later')
        if approve_on_form=='Y':
            self.fo_approve_in_popup(
                username=username,
                password=password,
                reason=reason
            )
        if list_error_message:
        # verify error
            self.assert_error_message()
            self.assert_list_error_message(list_error_message)
            print('Transaction failed!')
        else:
        # verify success
            self.assert_button_disable('Accept')
            self.assert_notification('Saved successfully!')
            # compare value
            if serial_numbers:
                for serial_no, expected in zip(serial_numbers, expected_values):
                    self.fo_assert_text_table('Serrial No', str(serial_no).replace('-',''), 'Stock leave status', expected)
            if expected_serial_number:
                self.fo_assert_text_table('Serrial No', str(expected_serial_number).replace('-',''), 'Stock leave status', expected_value)
            if expected_posting:
                self.assert_posting_data(**expected_posting)
            transaction_references=self.fo_get_text('Transaction references')
            print(f'Transaction references DPT_SLS: {transaction_references}')
            from_serial_mask=self.fo_get_value('From serial')
            print(f'From serial: {from_serial_mask}')
            to_serial_mask=self.fo_get_value('To serial')
            print(f'To serial: {to_serial_mask}')
            return transaction_references, from_serial_mask, to_serial_mask

    # DPT_SBI: 11802: Deposit savings book issue
    def dpt_sbi(self, account_number, serial_no, account_holding_branch_name=None, fee_collect_method=None, account_number_for_fee=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.open_fo('DPT_SBI', '11802')
        self.wait_for_button_available('Accept')
        self.assert_form_title('11802: Deposit savings book issue')
        # enter value
        self.fo_write_group('Account number', str(account_number).replace('-', ''))
        self.wait_loading()
        self.fo_write('Serial no', str(serial_no).replace('-', ''))
        self.wait_loading()
        self.fo_write_text('Description', ' AUTO TEST')
        if account_holding_branch_name:
            self.fo_assert_text('Account holding branch name', account_holding_branch_name)
        if fee_collect_method:
            self.fo_select('Fee collect method', fee_collect_method)
        if account_number_for_fee:
            self.fo_write_text_group('Account number for fee', account_number_for_fee)
        if ifc_codes:
            self.add_fees(ifc_codes, values, total_fee=total_fee)
        self.wait_loading()
        self.fo_click_checkbox('Caution!  There is no doubt that banks may be used as a means of Money Laundering/ Terrorist Financing/ Proliferation of Weapons of Mass Destruction.')
        # click 'Accept'
        self.click_button('Accept')
        # approve
        if approve_later=='Y':
            self.click_button('Later')
        if approve_on_form=='Y':
            self.fo_approve_in_popup(
                username=username,
                password=password,
                reason=reason
            )
        if list_error_message:
        # verify error
            self.assert_error_message()
            self.assert_list_error_message(list_error_message)
            print('Transaction failed!')
        else:
        # verify success
            self.assert_button_disable('Accept')
            self.switch_to_core_banking()
            self.assert_notification('Saved successfully!')
            self.close_voucher()
            if expected_posting:
                self.assert_posting_data(**expected_posting)
            transaction_references=self.fo_get_text('Transaction references')
            print(f'Transaction references DPT_SBI: {transaction_references}')
            deposit_account_mask=self.fo_get_value_group('Account number')
            print(f'Account number: {deposit_account_mask}')
            serial_no_mask=self.fo_get_value('Serial no')
            print(f'Serial no: {serial_no_mask}')
            return transaction_references, serial_no_mask

    # DPT_FBI: 11804: Fixed deposit book issue
    def dpt_fbi(self, account_number, serial_no, account_holding_branch_name=None, fee_collect_method=None, account_number_for_fee=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.open_fo('DPT_FBI', '11804')
        self.wait_for_button_available('Accept')
        self.assert_form_title('11804: Fixed deposit book issue')
        # enter value
        self.fo_write_group('Account number', str(account_number).replace('-', ''))
        self.wait_loading()
        self.fo_write('Serial no',  str(serial_no).replace('-', ''))
        self.wait_loading()
        self.fo_write_text('Description', 'AUTO TEST')
        if account_holding_branch_name:
            self.fo_assert_text('Account holding branch name', account_holding_branch_name)
        if fee_collect_method:
            self.fo_select('Fee collect method', fee_collect_method)
        if account_number_for_fee:
            self.fo_write_text_group('Account number for fee', account_number_for_fee)
        if ifc_codes:
            self.add_fees(ifc_codes, values, total_fee=total_fee)
        self.wait_loading()
        self.fo_click_checkbox('Caution!  There is no doubt that banks may be used as a means of Money Laundering/ Terrorist Financing/ Proliferation of Weapons of Mass Destruction.')
        # click 'Accept'
        self.click_button('Accept')
        # approve
        if approve_later=='Y':
            self.click_button('Later')
        if approve_on_form=='Y':
            self.fo_approve_in_popup(
                username=username,
                password=password,
                reason=reason
            )
        if list_error_message:
        # verify error
            self.assert_error_message()
            self.assert_list_error_message(list_error_message)
            print('Transaction failed!')
        else:
        # verify success
            self.assert_button_disable('Accept')
            self.switch_to_core_banking()
            self.assert_notification('Saved successfully!')
            self.close_voucher()
            if expected_posting:
                self.assert_posting_data(**expected_posting)
            transaction_references=self.fo_get_text('Transaction references')
            print(f'Transaction references DPT_FBI: {transaction_references}')
            deposit_account_mask=self.fo_get_value_group('Account number')
            print(f'Account number: {deposit_account_mask}')
            serial_no_mask=self.fo_get_value('Serial no')
            print(f'Serial no: {serial_no_mask}')
            return transaction_references, serial_no_mask

    # DPT_CER: 11803: Fixed deposit receipt issued
    def dpt_cer(self, account_number, cerfiticate_serial, account_holding_branch_name=None, currency=None, fee_collect_method=None, account_number_for_fee=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.open_fo('DPT_CER', '11803')
        self.wait_for_button_available('Accept')
        self.assert_form_title('11803: Fixed deposit receipt issued')
        # enter value
        self.fo_write_group('Account number', str(account_number).replace('-', ''))
        self.wait_loading()
        self.fo_write('Cerfiticate serial',  str(cerfiticate_serial).replace('-', ''))
        self.wait_loading()
        self.fo_write_text('Description', 'AUTO TEST')
        if account_holding_branch_name:
            self.fo_assert_text('Account holding branch name', account_holding_branch_name)
        if currency:
            self.fo_assert_select('Currency', currency)
        if fee_collect_method:
            self.fo_select('Fee collect method', fee_collect_method)
        if account_number_for_fee:
            self.fo_write_text_group('Account number for fee', account_number_for_fee)
        if ifc_codes:
            self.add_fees(ifc_codes, values, total_fee=total_fee)
        self.wait_loading()
        self.fo_click_checkbox('Caution!  There is no doubt that banks may be used as a means of Money Laundering/ Terrorist Financing/ Proliferation of Weapons of Mass Destruction.')
        # click 'Accept'
        self.click_button('Accept')
        # approve
        if approve_later=='Y':
            self.click_button('Later')
        if approve_on_form=='Y':
            self.fo_approve_in_popup(
                username=username,
                password=password,
                reason=reason
            )
        if list_error_message:
        # verify error
            self.assert_error_message()
            self.assert_list_error_message(list_error_message)
            print('Transaction failed!')
        else:
        # verify success
            self.assert_button_disable('Accept')
            self.switch_to_core_banking()
            self.assert_notification('Saved successfully!')
            self.close_voucher()
            if expected_posting:
                self.assert_posting_data(**expected_posting)
            transaction_references=self.fo_get_text('Transaction references')
            print(f'Transaction references DPT_CER: {transaction_references}')
            deposit_account_mask=self.fo_get_value_group('Account number')
            print(f'Account number: {deposit_account_mask}')
            serial_no_mask=self.fo_get_value('Cerfiticate serial')
            print(f'Cerfiticate serial: {serial_no_mask}')
            return transaction_references, serial_no_mask

    # DPT_POI: 11816: Payment order issued
    def dpt_poi(self, serial_no, amount, issued_date=None, expired_date=None, issuing_name=None, issuer_id_number=None, issuer_contact_number=None, currency=None, beneficiary_name=None, beneficiary_id_number=None, beneficiary_contact_number=None, beneficiary_address=None, purpose=None, debit_method=None, debit_account=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.open_fo('DPT_POI', '11816')
        self.wait_for_button_available('Accept')
        self.assert_form_title('11816: Payment order issued')
        # enter value
        serial_no_value = str(serial_no).replace('-', '')
        self.fo_write('Serial no', serial_no_value)
        self.wait_loading()
        self.fo_write_number('Amount', amount)
        self.wait_loading()
        if issued_date:
            self.fo_assert_date('Issued date', issued_date)
        if expired_date:
            self.fo_write_date('Expired date', expired_date)
        if issuing_name:
            self.fo_write_text('Issuing name', issuing_name)
        if issuer_id_number:
            self.fo_write_text('Issuer ID number', issuer_id_number)
        if issuer_contact_number:
            self.fo_write_text('Issuer contact number', issuer_contact_number)
        if currency:
            self.fo_select('Currency', currency)
        if beneficiary_name:
            self.fo_write_text('Beneficiary name', beneficiary_name)
        if beneficiary_id_number:
            self.fo_write_text('Beneficiary ID number', beneficiary_id_number)
        if beneficiary_contact_number:
            self.fo_write_text('Beneficiary contact number', beneficiary_contact_number)
        if beneficiary_address:
            self.fo_write_text('Beneficiary address', beneficiary_address)
        if purpose:
            self.fo_write_text('Purpose', purpose)
        if debit_method:
            self.fo_select('Debit method', debit_method)
        if debit_account:
            self.fo_write_text_group('Debit account', debit_account)
        self.wait_loading()
        self.fo_write_text('Description', 'AUTO TEST')
        if ifc_codes:
            self.add_fees(ifc_codes, values, total_fee=total_fee)
        self.wait_loading()
        self.fo_click_checkbox('Caution!  There is no doubt that banks may be used as a means of Money Laundering/ Terrorist Financing/ Proliferation of Weapons of Mass Destruction.')
        # click 'Accept'
        self.click_button('Accept')
        # approve
        if approve_later=='Y':
            self.click_button('Later')
        if approve_on_form=='Y':
            self.fo_approve_in_popup(
                username=username,
                password=password,
                reason=reason
            )
        if list_error_message:
        # verify error
            self.assert_error_message()
            self.assert_list_error_message(list_error_message)
            print('Transaction failed!')
        else:
        # verify success
            self.assert_button_disable('Accept')
            self.switch_to_core_banking()
            self.assert_notification('Saved successfully!')
            self.close_voucher()
            if expected_posting:
                self.assert_posting_data(**expected_posting)
            transaction_references=self.fo_get_text('Transaction references')
            print(f'Transaction references DPT_POI: {transaction_references}')
            serial_no_mask=self.fo_get_value('Serial no')
            print(f'Serial no: {serial_no_mask}')
            return transaction_references, serial_no_mask

    # DPT_POW: 11817: Payment order withdrawal
    def dpt_pow(self, serial_no, expired_date=None, issuing_name=None, issuer_id_number=None, issuer_contact_number=None, beneficiary_name=None, beneficiary_id_number=None, beneficiary_contact_number=None, beneficiary_address=None, currency=None, stock_amount=None, withdrawal_amount=None, withdrawal_method=None, credit_account=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.open_fo('DPT_POW', '11817')
        self.wait_for_button_available('Accept')
        self.assert_form_title('11817: Payment order withdrawal')
        # enter value
        serial_no_value = str(serial_no).replace('-', '')
        self.fo_write('Serial no', serial_no_value)
        self.wait_loading()
        if expired_date:
            self.fo_assert_date('Expired date', expired_date)
        if issuing_name:
            self.fo_assert_text('Issuing name', issuing_name)
        if issuer_id_number:
            self.fo_assert_text('Issuer ID number', issuer_id_number)
        if issuer_contact_number:
            self.fo_assert_text('Issuer contact number', issuer_contact_number)
        if beneficiary_name:
            self.fo_assert_text('Beneficiary name', beneficiary_name)
        if beneficiary_id_number:
            self.fo_assert_text('Beneficiary ID number', beneficiary_id_number)
        if beneficiary_contact_number:
            self.fo_assert_text('Beneficiary contact number', beneficiary_contact_number)
        if beneficiary_address:
            self.fo_assert_text('Beneficiary address', beneficiary_address)
        if currency:
            self.fo_assert_select('Currency', currency)
        if stock_amount:
            self.fo_assert_value('Stock amount', stock_amount)
        if withdrawal_amount:
            self.fo_assert_value('Withdrawal amount', withdrawal_amount)
        if withdrawal_method:
            self.fo_select('Withdrawal method', withdrawal_method)
        if credit_account:
            self.fo_write_text_group('Credit account', credit_account)
        self.wait_loading()
        self.fo_write_text('Description', 'AUTO TEST')
        if ifc_codes:
            self.add_fees(ifc_codes, values, total_fee=total_fee)
        self.wait_loading()
        self.fo_click_checkbox('Caution!  There is no doubt that banks may be used as a means of Money Laundering/ Terrorist Financing/ Proliferation of Weapons of Mass Destruction.')
        # click 'Accept'
        self.click_button('Accept')
        # approve
        if approve_later=='Y':
            self.click_button('Later')
        if approve_on_form=='Y':
            self.fo_approve_in_popup(
                username=username,
                password=password,
                reason=reason
            )
        if list_error_message:
        # verify error
            self.assert_error_message()
            self.assert_list_error_message(list_error_message)
            print('Transaction failed!')
        else:
        # verify success
            self.assert_button_disable('Accept')
            self.switch_to_core_banking()
            self.assert_notification('Saved successfully!')
            self.close_voucher()
            if expected_posting:
                self.assert_posting_data(**expected_posting)
            transaction_references=self.fo_get_text('Transaction references')
            print(f'Transaction references DPT_POW: {transaction_references}')
            serial_no_mask=self.fo_get_value('Serial no')
            print(f'Serial no: {serial_no_mask}')
            return transaction_references, serial_no_mask

    # DPT_RPO: 11818: Payment order return
    def dpt_rpo(self, serial_no, expired_date=None, issuing_name=None, issuer_id_number=None, issuer_contact_number=None, beneficiary_name=None, beneficiary_id_number=None, beneficiary_contact_number=None, beneficiary_address=None, currency=None, stock_amount=None, return_amount=None, return_method=None, credit_account=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.open_fo('DPT_RPO', '11818')
        self.wait_for_button_available('Accept')
        self.assert_form_title('11818: Payment order return')
        # enter value
        serial_no_value = str(serial_no).replace('-', '')
        self.fo_write('Serial no', serial_no_value)
        self.wait_loading()
        if expired_date:
            self.fo_assert_date('Expired date', expired_date)
        if issuing_name:
            self.fo_assert_text('Issuing name', issuing_name)
        if issuer_id_number:
            self.fo_assert_text('Issuer ID number', issuer_id_number)
        if issuer_contact_number:
            self.fo_assert_text('Issuer contact number', issuer_contact_number)
        if beneficiary_name:
            self.fo_assert_text('Beneficiary name', beneficiary_name)
        if beneficiary_id_number:
            self.fo_assert_text('Beneficiary ID number', beneficiary_id_number)
        if beneficiary_contact_number:
            self.fo_assert_text('Beneficiary contact number', beneficiary_contact_number)
        if beneficiary_address:
            self.fo_assert_text('Beneficiary address', beneficiary_address)
        if currency:
            self.fo_assert_select('Currency', currency)
        if stock_amount:
            self.fo_assert_value('Stock amount', stock_amount)
        if return_amount:
            self.fo_assert_value('Return amount', return_amount)
        if return_method:
            self.fo_select('Return method', return_method)
        if credit_account:
            self.fo_write_text_group('Credit account', credit_account)
        self.wait_loading()
        self.fo_write_text('Description', 'AUTO TEST')
        if ifc_codes:
            self.add_fees(ifc_codes, values, total_fee=total_fee)
        self.wait_loading()
        self.fo_click_checkbox('Caution!  There is no doubt that banks may be used as a means of Money Laundering/ Terrorist Financing/ Proliferation of Weapons of Mass Destruction.')
        # click 'Accept'
        self.click_button('Accept')
        # approve
        if approve_later=='Y':
            self.click_button('Later')
        if approve_on_form=='Y':
            self.fo_approve_in_popup(
                username=username,
                password=password,
                reason=reason
            )
        if list_error_message:
        # verify error
            self.assert_error_message()
            self.assert_list_error_message(list_error_message)
            print('Transaction failed!')
        else:
        # verify success
            self.assert_button_disable('Accept')
            self.switch_to_core_banking()
            self.assert_notification('Saved successfully!')
            self.close_voucher()
            if expected_posting:
                self.assert_posting_data(**expected_posting)
            transaction_references=self.fo_get_text('Transaction references')
            print(f'Transaction references DPT_RPO: {transaction_references}')
            serial_no_mask=self.fo_get_value('Serial no')
            print(f'Serial no: {serial_no_mask}')
            return transaction_references, serial_no_mask

    # DPT_CCI: 11806: Gift cheque issued
    def dpt_cci(self, serial_no, amount, issued_date=None, expired_date=None, issuing_name=None, issuer_id_number=None, issuer_contact_number=None, currency=None, beneficiary_name=None, beneficiary_id_number=None, beneficiary_contact_number=None, beneficiary_address=None, purpose=None, debit_method=None, debit_account=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.open_fo('DPT_CCI', '11806')
        self.wait_for_button_available('Accept')
        self.assert_form_title('11806: Gift cheque issued')
        # enter value
        serial_no_value = str(serial_no).replace('-', '')
        self.fo_write('Serial no', serial_no_value)
        self.wait_loading()
        self.fo_write_number('Amount', amount)
        self.wait_loading()
        if issued_date:
            self.fo_assert_date('Issued date', issued_date)
        if expired_date:
            self.fo_write_date('Expired date', expired_date)
        if issuing_name:
            self.fo_write_text('Issuing name', issuing_name)
        if issuer_id_number:
            self.fo_write_text('Issuer ID number', issuer_id_number)
        if issuer_contact_number:
            self.fo_write_text('Issuer contact number', issuer_contact_number)
        if currency:
            self.fo_select('Currency', currency)
        if beneficiary_name:
            self.fo_write_text('Beneficiary name', beneficiary_name)
        if beneficiary_id_number:
            self.fo_write_text('Beneficiary ID number', beneficiary_id_number)
        if beneficiary_contact_number:
            self.fo_write_text('Beneficiary contact number', beneficiary_contact_number)
        if beneficiary_address:
            self.fo_write_text('Beneficiary address', beneficiary_address)
        if purpose:
            self.fo_write_text('Purpose', purpose)
        if debit_method:
            self.fo_select('Debit method', debit_method)
        if debit_account:
            self.fo_write_text_group('Debit account', debit_account)
        self.wait_loading()
        self.fo_write_text('Description', 'AUTO TEST')
        if ifc_codes:
            self.add_fees(ifc_codes, values, total_fee=total_fee)
        self.wait_loading()
        self.fo_click_checkbox('Caution!  There is no doubt that banks may be used as a means of Money Laundering/ Terrorist Financing/ Proliferation of Weapons of Mass Destruction.')
        # click 'Accept'
        self.click_button('Accept')
        # approve
        if approve_later=='Y':
            self.click_button('Later')
        if approve_on_form=='Y':
            self.fo_approve_in_popup(
                username=username,
                password=password,
                reason=reason
            )
        if list_error_message:
        # verify error
            self.assert_error_message()
            self.assert_list_error_message(list_error_message)
            print('Transaction failed!')
        else:
        # verify success
            self.assert_button_disable('Accept')
            self.switch_to_core_banking()
            self.assert_notification('Saved successfully!')
            self.close_voucher()
            if expected_posting:
                self.assert_posting_data(**expected_posting)
            transaction_references=self.fo_get_text('Transaction references')
            print(f'Transaction references DPT_CCI: {transaction_references}')
            serial_no_mask=self.fo_get_value('Serial no')
            print(f'Serial no: {serial_no_mask}')
            return transaction_references, serial_no_mask

    # DPT_CCW: 11807: Gift Cheque withdrawal
    def dpt_ccw(self, serial_no, expired_date=None, issuing_name=None, issuer_id_number=None, issuer_contact_number=None, beneficiary_name=None, beneficiary_id_number=None, beneficiary_contact_number=None, beneficiary_address=None, currency=None, stock_amount=None, withdrawal_amount=None, withdrawal_method=None, credit_account=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.open_fo('DPT_CCW', '11807')
        self.wait_for_button_available('Accept')
        self.assert_form_title('11807: Gift Cheque withdrawal')
        # enter value
        serial_no_value = str(serial_no).replace('-', '')
        self.fo_write('Serial no', serial_no_value)
        self.wait_loading()
        if expired_date:
            self.fo_assert_date('Expired date', expired_date)
        if issuing_name:
            self.fo_assert_text('Issuing name', issuing_name)
        if issuer_id_number:
            self.fo_assert_text('Issuer ID number', issuer_id_number)
        if issuer_contact_number:
            self.fo_assert_text('Issuer contact number', issuer_contact_number)
        if beneficiary_name:
            self.fo_assert_text('Beneficiary name', beneficiary_name)
        if beneficiary_id_number:
            self.fo_assert_text('Beneficiary ID number', beneficiary_id_number)
        if beneficiary_contact_number:
            self.fo_assert_text('Beneficiary contact number', beneficiary_contact_number)
        if beneficiary_address:
            self.fo_assert_text('Beneficiary address', beneficiary_address)
        if currency:
            self.fo_assert_select('Currency', currency)
        if stock_amount:
            self.fo_assert_value('Stock amount', stock_amount)
        if withdrawal_amount:
            self.fo_assert_value('Withdrawal amount', withdrawal_amount)
        if withdrawal_method:
            self.fo_select('Withdrawal method', withdrawal_method)
        if credit_account:
            self.fo_write_text_group('Credit account', credit_account)
        self.wait_loading()
        self.fo_write_text('Description', 'AUTO TEST')
        if ifc_codes:
            self.add_fees(ifc_codes, values, total_fee=total_fee)
        self.wait_loading()
        self.fo_click_checkbox('Caution!  There is no doubt that banks may be used as a means of Money Laundering/ Terrorist Financing/ Proliferation of Weapons of Mass Destruction.')
        # click 'Accept'
        self.click_button('Accept')
        # approve
        if approve_later=='Y':
            self.click_button('Later')
        if approve_on_form=='Y':
            self.fo_approve_in_popup(
                username=username,
                password=password,
                reason=reason
            )
        if list_error_message:
        # verify error
            self.assert_error_message()
            self.assert_list_error_message(list_error_message)
            print('Transaction failed!')
        else:
        # verify success
            self.assert_button_disable('Accept')
            self.switch_to_core_banking()
            self.assert_notification('Saved successfully!')
            self.close_voucher()
            if expected_posting:
                self.assert_posting_data(**expected_posting)
            transaction_references=self.fo_get_text('Transaction references')
            print(f'Transaction references DPT_CCW: {transaction_references}')
            serial_no_mask=self.fo_get_value('Serial no')
            print(f'Serial no: {serial_no_mask}')
            return transaction_references, serial_no_mask

    # DPT_RCC: 11808: Gift cheque return
    def dpt_rcc(self, serial_no, expired_date=None, issuing_name=None, issuer_id_number=None, issuer_contact_number=None, beneficiary_name=None, beneficiary_id_number=None, beneficiary_contact_number=None, beneficiary_address=None, currency=None, stock_amount=None, return_amount=None, return_method=None, credit_account=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.open_fo('DPT_RCC', '11808')
        self.wait_for_button_available('Accept')
        self.assert_form_title('11808: Gift cheque return')
        # enter value
        serial_no_value = str(serial_no).replace('-', '')
        self.fo_write('Serial no', serial_no_value)
        self.wait_loading()
        if expired_date:
            self.fo_assert_date('Expired date', expired_date)
        if issuing_name:
            self.fo_assert_text('Issuing name', issuing_name)
        if issuer_id_number:
            self.fo_assert_text('Issuer ID number', issuer_id_number)
        if issuer_contact_number:
            self.fo_assert_text('Issuer contact number', issuer_contact_number)
        if beneficiary_name:
            self.fo_assert_text('Beneficiary name', beneficiary_name)
        if beneficiary_id_number:
            self.fo_assert_text('Beneficiary ID number', beneficiary_id_number)
        if beneficiary_contact_number:
            self.fo_assert_text('Beneficiary contact number', beneficiary_contact_number)
        if beneficiary_address:
            self.fo_assert_text('Beneficiary address', beneficiary_address)
        if currency:
            self.fo_assert_select('Currency', currency)
        if stock_amount:
            self.fo_assert_value('Stock amount', stock_amount)
        if return_amount:
            self.fo_assert_value('Return amount', return_amount)
        if return_method:
            self.fo_select('Return method', return_method)
        if credit_account:
            self.fo_write_text_group('Credit account', credit_account)
        self.wait_loading()
        self.fo_write_text('Description', 'AUTO TEST')
        if ifc_codes:
            self.add_fees(ifc_codes, values, total_fee=total_fee)
        self.wait_loading()
        self.fo_click_checkbox('Caution!  There is no doubt that banks may be used as a means of Money Laundering/ Terrorist Financing/ Proliferation of Weapons of Mass Destruction.')
        # click 'Accept'
        self.click_button('Accept')
        # approve
        if approve_later=='Y':
            self.click_button('Later')
        if approve_on_form=='Y':
            self.fo_approve_in_popup(
                username=username,
                password=password,
                reason=reason
            )
        if list_error_message:
        # verify error
            self.assert_error_message()
            self.assert_list_error_message(list_error_message)
            print('Transaction failed!')
        else:
        # verify success
            self.assert_button_disable('Accept')
            self.switch_to_core_banking()
            self.assert_notification('Saved successfully!')
            self.close_voucher()
            if expected_posting:
                self.assert_posting_data(**expected_posting)
            transaction_references=self.fo_get_text('Transaction references')
            print(f'Transaction references DPT_RCC: {transaction_references}')
            serial_no_mask=self.fo_get_value('Serial no')
            print(f'Serial no: {serial_no_mask}')
            return transaction_references, serial_no_mask

# -------------------------- handle FO - TREASURY - FOREX --------------------------
    # TFX_OFO: FX - Outright (Spot, Forward)
    def tfx_ofo(self, counterparty_code, catalogue_code, contract_rate, account_name=None, value_date=None, reference_rate=None, swap_point=None, debit_currency=None, credit_currency=None, debit_by=None, debit_amount=None, debit_account_no_dpt=None, debit_account_no_act=None, debit_account_name=None, credit_by=None, credit_amount=None, credit_account_no_dpt=None, credit_account_no_act=None, credit_account_name=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.open_fo('TFX_OFO', 'Outright')
        self.wait_for_button_available('Accept')
        self.assert_form_title('FX - Outright (Spot, Forward)')
        # enter value
        self.lookup_data('Counterparty code', 'Code', str(counterparty_code).replace('-', ''))
        self.lookup_data('Catalogue code', 'Code', catalogue_code, "N")
        if self.fo_get_select('Trade type')=='Buy':
            if debit_currency:
                self.fo_select('Debit currency', debit_currency)
            if credit_currency:
                self.assertEqual(self.fo_get_select('Credit currency'), credit_currency)
        if self.fo_get_select('Trade type')=='Sell':
            if credit_currency:
                self.fo_select('Credit currency', credit_currency)
            if debit_currency:
                self.assertEqual(self.fo_get_select('Debit currency'), debit_currency)
        self.fo_write_number('Contract rate', str(contract_rate).replace(',', ''))
        if self.fo_get_value('Contract rate')!= contract_rate:
            self.fo_write_number('Contract rate', str(contract_rate).replace(',', ''))
        if value_date:
            self.assertEqual(self.fo_get_date('Value date'), value_date)
        if account_name:
            self.assertEqual(self.fo_get_text('Account name'), account_name)
        if reference_rate:
            self.assertEqual(self.fo_get_value('Reference rate'), reference_rate)
        if swap_point:
            self.assertEqual(self.fo_get_value('Swap point'), swap_point)
        # Debit info
        if debit_by:
            self.select('Debit by', debit_by)
        if self.fo_get_select('Trade type')=='Buy':
            if debit_amount:
                self.fo_write_number_border('Debit', 'Amount', debit_amount)
                if self.get_text_input_below_border('Debit', 'Amount')!= debit_amount:
                    self.fo_write_number_border('Debit', 'Amount', str(debit_amount).replace(',', ''))
            if credit_amount:
                self.assertEqual(self.get_text_input_below_border('Credit', 'Amount'), credit_amount)
        if debit_account_no_dpt:
            self.fo_write_border('Debit', 'Account No. DPT', debit_account_no_dpt)
        if debit_account_no_act:
            self.fo_write_border('Debit', 'Account No. ACT', debit_account_no_act)
        if debit_currency:
            self.assertEqual(self.get_text_input_below_border('Debit', 'Currency'), debit_currency)
        if debit_account_name:
            self.assertEqual(self.get_text_textarea_below_border('Debit', 'Account name'), debit_account_name)
        # Credit info
        if credit_by:
            self.select('Credit by', credit_by)
        if self.fo_get_select('Trade type')=='Sell':
            if credit_amount:
                self.fo_write_number_border('Credit', 'Amount', credit_amount)
                if self.get_text_input_below_border('Credit', 'Amount')!= credit_amount:
                    self.fo_write_number_border('Credit', 'Amount', str(credit_amount).replace(',', ''))
            if debit_amount:
                self.assertEqual(self.get_text_input_below_border('Debit', 'Amount'), debit_amount)
        if credit_account_no_dpt:
            self.fo_write_border('Credit', 'Account No. DPT', credit_account_no_dpt)
        if credit_account_no_act:
            self.fo_write_border('Credit', 'Account No. ACT', credit_account_no_act)
        if credit_currency:
            self.assertEqual(self.get_text_input_below_border('Credit', 'Currency'), credit_currency)
        if credit_account_name:
            self.assertEqual(self.get_text_textarea_below_border('Credit', 'Account name'), credit_account_name)
        self.fo_write_text('Description', 'AUTO TEST')
        if ifc_codes:
            self.add_fees(ifc_codes, values, total_fee)
        self.wait_loading()
        self.fo_click_checkbox('Caution!  There is no doubt that banks may be used as a means of Money Laundering/ Terrorist Financing/ Proliferation of Weapons of Mass Destruction.')
        # click 'Accept'
        self.click_button('Accept')
        # approve
        if approve_later=='Y':
            self.click_button('Later')
        if approve_on_form=='Y':
            self.fo_approve_in_popup(
                username=username,
                password=password,
                reason=reason
            )
        if list_error_message:
        # verify error
            self.assert_error_message()
            self.assert_list_error_message(list_error_message)
            print('Transaction failed!')
        else:
        # verify success
            self.assert_button_disable('Accept')
            self.switch_to_core_banking()
            self.assert_notification('Saved successfully!')
            self.close_voucher()
            if expected_posting:
                self.assert_posting_data(**expected_posting)
            transaction_references=self.fo_get_text('Transaction references')
            print(f'Transaction references TFX_OFO: {transaction_references}')
            forex_account_mask=self.fo_get_value('Account number')
            print(f'Account number: {forex_account_mask}')
            return transaction_references, forex_account_mask

    def tfx_ofo_view(self, transaction_references, account_number=None, counterparty_code=None, catalogue_code=None, trade_type=None, contract_rate=None, account_name=None, value_date=None, reference_rate=None, swap_point=None, debit_currency=None, credit_currency=None, debit_by=None, debit_amount=None, debit_account_no_dpt=None, debit_account_no_act=None, debit_account_name=None, credit_by=None, credit_amount=None, credit_account_no_dpt=None, credit_account_no_act=None, credit_account_name=None, expected_posting=None):
        self.transaction_view(transaction_references, 'FX - Outright (Spot, Forward)')
        # compare value
        if account_number:
            self.assertEqual(self.fo_get_value('Account number'), self.treasury_account_number_mask(account_number))
        if counterparty_code:
            self.assertEqual(self.fo_get_value_group('Counterparty code'), counterparty_code)
        if catalogue_code:
            self.assertEqual(self.fo_get_text_group('Catalogue code'), catalogue_code)
        if trade_type:
            self.assertEqual(self.fo_get_select('Trade type'), trade_type)
        if value_date:
            self.assertEqual(self.fo_get_date('Value date'), value_date)
        if account_name:
            self.assertEqual(self.fo_get_text('Account name'), account_name)
        if debit_currency:
            self.assertEqual(self.fo_get_select('Debit currency'), debit_currency)
        if credit_currency:
            self.assertEqual(self.fo_get_select('Credit currency'), credit_currency)
        if reference_rate:
            self.assertEqual(self.fo_get_value('Reference rate'), reference_rate)
        if swap_point:
            self.assertEqual(self.fo_get_value('Swap point'), swap_point)
        if contract_rate:
            self.assertEqual(self.fo_get_value('Contract rate'), contract_rate)
        # compare debit info
        if debit_by:
            self.assertEqual(self.get_text_input_below_border('Debit', 'Debit by'), debit_by)
        if debit_currency:
            self.assertEqual(self.get_text_input_below_border('Debit', 'Currency'), debit_currency)
        if debit_amount:
            self.assertEqual(self.get_text_input_below_border('Debit', 'Amount'), debit_amount)
        if debit_account_no_dpt:
            self.assertEqual(self.get_text_input_below_border('Debit', 'Account No. DPT'), debit_account_no_dpt)
        if debit_account_no_act:
            self.assertEqual(self.get_text_input_below_border('Debit', 'Account No. ACT'), debit_account_no_act)
        if debit_account_name:
            self.assertEqual(self.get_text_textarea_below_border('Debit', 'Account name'), debit_account_name)
        # compare credit info
        if credit_by:
            self.assertEqual(self.get_text_input_below_border('Credit', 'Credit by'), credit_by)
        if credit_currency:
            self.assertEqual(self.get_text_input_below_border('Credit', 'Currency'), credit_currency)
        if credit_amount:
            self.assertEqual(self.get_text_input_below_border('Credit', 'Amount'), credit_amount)
        if credit_account_no_dpt:
            self.assertEqual(self.get_text_input_below_border('Credit', 'Account No. DPT'), credit_account_no_dpt)
        if credit_account_no_act:
            self.assertEqual(self.get_text_input_below_border('Credit', 'Account No. ACT'), credit_account_no_act)
        if credit_account_name:
            self.assertEqual(self.get_text_textarea_below_border('Credit', 'Account name'), credit_account_name)
        if expected_posting:
            self.assert_posting_data(**expected_posting)

    # TFX_FAC: FX - Approve for FX Outright
    def tfx_fac(self, account_number, counterparty_code=None, catalogue_code=None, trade_type=None, contract_rate=None, account_name=None, value_date=None, reference_rate=None, swap_point=None, debit_currency=None, credit_currency=None, debit_by=None, debit_amount=None, debit_account_no_dpt=None, debit_account_no_act=None, debit_account_name=None, credit_by=None, credit_amount=None, credit_account_no_dpt=None, credit_account_no_act=None, credit_account_name=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.open_fo('TFX_FAC', 'Approve')
        self.wait_for_button_available('Accept')
        self.assert_form_title('FX - Approve for FX Outright')
        # enter value
        self.fo_write('Account number', str(account_number).replace('-', ''))
        self.wait_loading()
        self.fo_write_text('Description', 'AUTO TEST')
        if ifc_codes:
            self.add_fees(ifc_codes, values, total_fee)
        self.wait_loading()
        # compare value
        if counterparty_code:
            self.assertEqual(self.fo_get_value_group('Counterparty code'), counterparty_code)
        if catalogue_code:
            self.assertEqual(self.fo_get_text_group('Catalogue code'), catalogue_code)
        if trade_type:
            self.assertEqual(self.fo_get_select('Trade type'), trade_type)
        if value_date:
            self.assertEqual(self.fo_get_date('Value date'), value_date)
        if account_name:
            self.assertEqual(self.fo_get_text('Account name'), account_name)
        if debit_currency:
            self.assertEqual(self.fo_get_select('Debit currency'), debit_currency)
        if credit_currency:
            self.assertEqual(self.fo_get_select('Credit currency'), credit_currency)
        if reference_rate:
            self.assertEqual(self.fo_get_value('Reference rate'), reference_rate)
        if swap_point:
            self.assertEqual(self.fo_get_value('Swap point'), swap_point)
        if contract_rate:
            self.assertEqual(self.fo_get_value('Contract rate'), contract_rate)
        # compare debit info
        if debit_by:
            self.assertEqual(self.get_text_input_below_border('Debit', 'Debit by'), debit_by)
        if debit_currency:
            self.assertEqual(self.get_text_input_below_border('Debit', 'Currency'), debit_currency)
        if debit_amount:
            self.assertEqual(self.get_text_input_below_border('Debit', 'Amount'), debit_amount)
        if debit_account_no_dpt:
            self.assertEqual(self.get_text_input_below_border('Debit', 'Account No. DPT'), debit_account_no_dpt)
        if debit_account_no_act:
            self.assertEqual(self.get_text_input_below_border('Debit', 'Account No. ACT'), debit_account_no_act)
        if debit_account_name:
            self.assertEqual(self.get_text_textarea_below_border('Debit', 'Account name'), debit_account_name)
        # compare credit info
        if credit_by:
            self.assertEqual(self.get_text_input_below_border('Credit', 'Credit by'), credit_by)
        if credit_currency:
            self.assertEqual(self.get_text_input_below_border('Credit', 'Currency'), credit_currency)
        if credit_amount:
            self.assertEqual(self.get_text_input_below_border('Credit', 'Amount'), credit_amount)
        if credit_account_no_dpt:
            self.assertEqual(self.get_text_input_below_border('Credit', 'Account No. DPT'), credit_account_no_dpt)
        if credit_account_no_act:
            self.assertEqual(self.get_text_input_below_border('Credit', 'Account No. ACT'), credit_account_no_act)
        if credit_account_name:
            self.assertEqual(self.get_text_textarea_below_border('Credit', 'Account name'), credit_account_name)
        self.fo_click_checkbox('Caution!  There is no doubt that banks may be used as a means of Money Laundering/ Terrorist Financing/ Proliferation of Weapons of Mass Destruction.')
        # click 'Accept'
        self.click_button('Accept')
        # approve
        if approve_later=='Y':
            self.click_button('Later')
        if approve_on_form=='Y':
            self.fo_approve_in_popup(
                username=username,
                password=password,
                reason=reason
            )
        if list_error_message:
        # verify error
            self.assert_error_message()
            self.assert_list_error_message(list_error_message)
            print('Transaction failed!')
        else:
        # verify success
            self.assert_button_disable('Accept')
            self.switch_to_core_banking()
            self.assert_notification('Saved successfully!')
            self.close_voucher()
            if expected_posting:
                self.assert_posting_data(**expected_posting)
            transaction_references=self.fo_get_text('Transaction references')
            print(f'Transaction references TFX_FAC: {transaction_references}')
            forex_account_mask=self.fo_get_value('Account number')
            print(f'Account number: {forex_account_mask}')
            return transaction_references, forex_account_mask

    def tfx_fac_view(self, transaction_references, account_number=None, counterparty_code=None, catalogue_code=None, trade_type=None, contract_rate=None, account_name=None, value_date=None, reference_rate=None, swap_point=None, debit_currency=None, credit_currency=None, debit_by=None, debit_amount=None, debit_account_no_dpt=None, debit_account_no_act=None, debit_account_name=None, credit_by=None, credit_amount=None, credit_account_no_dpt=None, credit_account_no_act=None, credit_account_name=None, expected_posting=None):
        self.transaction_view(transaction_references, 'FX - Approve for FX Outright')
        # compare value
        if account_number:
            self.assertEqual(self.fo_get_value('Account number'), self.treasury_account_number_mask(account_number))
        if counterparty_code:
            self.assertEqual(self.fo_get_value_group('Counterparty code'), counterparty_code)
        if catalogue_code:
            self.assertEqual(self.fo_get_text_group('Catalogue code'), catalogue_code)
        if trade_type:
            self.assertEqual(self.fo_get_select('Trade type'), trade_type)
        if value_date:
            self.assertEqual(self.fo_get_date('Value date'), value_date)
        if account_name:
            self.assertEqual(self.fo_get_text('Account name'), account_name)
        if debit_currency:
            self.assertEqual(self.fo_get_select('Debit currency'), debit_currency)
        if credit_currency:
            self.assertEqual(self.fo_get_select('Credit currency'), credit_currency)
        if reference_rate:
            self.assertEqual(self.fo_get_value('Reference rate'), reference_rate)
        if swap_point:
            self.assertEqual(self.fo_get_value('Swap point'), swap_point)
        if contract_rate:
            self.assertEqual(self.fo_get_value('Contract rate'), contract_rate)
        # compare debit info
        if debit_by:
            self.assertEqual(self.get_text_input_below_border('Debit', 'Debit by'), debit_by)
        if debit_currency:
            self.assertEqual(self.get_text_input_below_border('Debit', 'Currency'), debit_currency)
        if debit_amount:
            self.assertEqual(self.get_text_input_below_border('Debit', 'Amount'), debit_amount)
        if debit_account_no_dpt:
            self.assertEqual(self.get_text_input_below_border('Debit', 'Account No. DPT'), debit_account_no_dpt)
        if debit_account_no_act:
            self.assertEqual(self.get_text_input_below_border('Debit', 'Account No. ACT'), debit_account_no_act)
        if debit_account_name:
            self.assertEqual(self.get_text_textarea_below_border('Debit', 'Account name'), debit_account_name)
        # compare credit info
        if credit_by:
            self.assertEqual(self.get_text_input_below_border('Credit', 'Credit by'), credit_by)
        if credit_currency:
            self.assertEqual(self.get_text_input_below_border('Credit', 'Currency'), credit_currency)
        if credit_amount:
            self.assertEqual(self.get_text_input_below_border('Credit', 'Amount'), credit_amount)
        if credit_account_no_dpt:
            self.assertEqual(self.get_text_input_below_border('Credit', 'Account No. DPT'), credit_account_no_dpt)
        if credit_account_no_act:
            self.assertEqual(self.get_text_input_below_border('Credit', 'Account No. ACT'), credit_account_no_act)
        if credit_account_name:
            self.assertEqual(self.get_text_textarea_below_border('Credit', 'Account name'), credit_account_name)
        if expected_posting:
            self.assert_posting_data(**expected_posting)

    # TFX_OAA: FX - Outright Account Amendment
    def tfx_oaa(self, account_number, counterparty_code=None, catalogue_code=None, trade_type=None, contract_rate=None, contract_rate_update=None, account_name=None, value_date=None, reference_rate=None, swap_point=None, swap_point_update=None, debit_currency=None, credit_currency=None, debit_by=None, debit_by_update=None, debit_amount=None, debit_amount_update=None, debit_account_no_dpt=None, debit_account_no_dpt_update=None, debit_account_no_act=None, debit_account_no_act_update=None, debit_account_name=None, debit_account_name_update=None, credit_by=None, credit_by_update=None, credit_amount=None, credit_amount_update=None, credit_account_no_dpt=None, credit_account_no_dpt_update=None, credit_account_no_act=None, credit_account_no_act_update=None, credit_account_name=None, credit_account_name_update=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.open_fo('TFX_OAA', 'Amendment')
        self.wait_for_button_available('Accept')
        self.assert_form_title('FX - Outright Account Amendment')
        # enter value
        self.fo_write('Account number', str(account_number).replace('-', ''))
        self.wait_loading()
        self.fo_write_text('Description', 'AUTO TEST')
        self.wait_loading()
        # compare value
        if counterparty_code:
            self.assertEqual(self.fo_get_value_group('Counterparty code'), counterparty_code)
        if catalogue_code:
            self.assertEqual(self.fo_get_text_group('Catalogue code'), catalogue_code)
        if trade_type:
            self.assertEqual(self.fo_get_select('Trade type'), trade_type)
        if value_date:
            self.assertEqual(self.fo_get_date('Value date'), value_date)
        if account_name:
            self.assertEqual(self.fo_get_text('Account name'), account_name)
        if debit_currency:
            self.assertEqual(self.fo_get_select('Debit currency'), debit_currency)
        if credit_currency:
            self.assertEqual(self.fo_get_select('Credit currency'), credit_currency)
        if reference_rate:
            self.assertEqual(self.fo_get_value('Reference rate'), reference_rate)
        if swap_point:
            self.assertEqual(self.fo_get_value('Swap point'), swap_point)
        if contract_rate:
            self.assertEqual(self.fo_get_value('Contract rate'), contract_rate)
        # compare debit info
        if debit_by:
            self.assertEqual(self.get_text_input_below_border('Debit', 'Debit by'), debit_by)
        if debit_currency:
            self.assertEqual(self.get_text_input_below_border('Debit', 'Currency'), debit_currency)
        if debit_amount:
            self.assertEqual(self.get_text_input_below_border('Debit', 'Amount'), debit_amount)
        if debit_account_no_dpt:
            self.assertEqual(self.get_text_input_below_border('Debit', 'Account No. DPT'), debit_account_no_dpt)
        if debit_account_no_act:
            self.assertEqual(self.get_text_input_below_border('Debit', 'Account No. ACT'), debit_account_no_act)
        if debit_account_name:
            self.assertEqual(self.get_text_textarea_below_border('Debit', 'Account name'), debit_account_name)
        # compare credit info
        if credit_by:
            self.assertEqual(self.get_text_input_below_border('Credit', 'Credit by'), credit_by)
        if credit_currency:
            self.assertEqual(self.get_text_input_below_border('Credit', 'Currency'), credit_currency)
        if credit_amount:
            self.assertEqual(self.get_text_input_below_border('Credit', 'Amount'), credit_amount)
        if credit_account_no_dpt:
            self.assertEqual(self.get_text_input_below_border('Credit', 'Account No. DPT'), credit_account_no_dpt)
        if credit_account_no_act:
            self.assertEqual(self.get_text_input_below_border('Credit', 'Account No. ACT'), credit_account_no_act)
        if credit_account_name:
            self.assertEqual(self.get_text_textarea_below_border('Credit', 'Account name'), credit_account_name)
        # enter value modify
        if contract_rate_update:
            self.fo_write_number('Contract rate', str(contract_rate_update).replace(',', ''))
            if self.fo_get_value('Contract rate')!= contract_rate_update:
                self.fo_write_number('Contract rate', str(contract_rate_update).replace(',', ''))
        if swap_point_update:
            self.assertEqual(self.fo_get_value('Swap point'), swap_point_update)
        # modify debit info
        if debit_by_update:
            self.select('Debit by', debit_by_update)
        if self.fo_get_select('Trade type')=='Buy':
            if debit_amount_update:
                self.fo_write_number_border('Debit', 'Amount', debit_amount_update)
                if self.get_text_input_below_border('Debit', 'Amount')!= debit_amount_update:
                    self.fo_write_number_border('Debit', 'Amount', str(debit_amount_update).replace(',', ''))
            if credit_amount_update:
                self.assertEqual(self.get_text_input_below_border('Credit', 'Amount'), credit_amount_update)
        if debit_account_no_dpt_update:
            self.fo_write_border('Debit', 'Account No. DPT', debit_account_no_dpt_update)
        if debit_account_no_act_update:
            self.fo_write_border('Debit', 'Account No. ACT', debit_account_no_act_update)
        if debit_currency:
            self.assertEqual(self.get_text_input_below_border('Debit', 'Currency'), debit_currency)
        if debit_account_name_update:
            self.assertEqual(self.get_text_textarea_below_border('Debit', 'Account name'), debit_account_name_update)
        # modify credit info
        if credit_by_update:
            self.select('Credit by', credit_by_update)
        if self.fo_get_select('Trade type')=='Sell':
            if credit_amount_update:
                self.fo_write_number_border('Credit', 'Amount', credit_amount_update)
                if self.get_text_input_below_border('Credit', 'Amount')!= credit_amount_update:
                    self.fo_write_number_border('Credit', 'Amount', str(credit_amount_update).replace(',', ''))
            if debit_amount_update:
                self.assertEqual(self.get_text_input_below_border('Debit', 'Amount'), debit_amount_update)
        if credit_account_no_dpt_update:
            self.fo_write_border('Credit', 'Account No. DPT', credit_account_no_dpt_update)
        if credit_account_no_act_update:
            self.fo_write_border('Credit', 'Account No. ACT', credit_account_no_act_update)
        if credit_currency:
            self.key_escape()
            self.assertEqual(self.get_text_input_below_border('Credit', 'Currency'), credit_currency)
        if credit_account_name_update:
            self.assertEqual(self.get_text_textarea_below_border('Credit', 'Account name'), credit_account_name_update)
        self.wait_loading()
        self.fo_write_text('Description', 'AUTO TEST')
        if ifc_codes:
            self.add_fees(ifc_codes, values, total_fee)
        self.wait_loading()
        self.fo_click_checkbox('Caution!  There is no doubt that banks may be used as a means of Money Laundering/ Terrorist Financing/ Proliferation of Weapons of Mass Destruction.')
        # click 'Accept'
        self.click_button('Accept')
        # approve
        if approve_later=='Y':
            self.click_button('Later')
        if approve_on_form=='Y':
            self.fo_approve_in_popup(
                username=username,
                password=password,
                reason=reason
            )
        if list_error_message:
        # verify error
            self.assert_error_message()
            self.assert_list_error_message(list_error_message)
            print('Transaction failed!')
        else:
        # verify success
            self.assert_button_disable('Accept')
            self.switch_to_core_banking()
            self.assert_notification('Saved successfully!')
            self.close_voucher()
            if expected_posting:
                self.assert_posting_data(**expected_posting)
            transaction_references=self.fo_get_text('Transaction references')
            print(f'Transaction references TFX_OAA: {transaction_references}')
            forex_account_mask=self.fo_get_value('Account number')
            print(f'Account number: {forex_account_mask}')
            return transaction_references, forex_account_mask

    def tfx_oaa_view(self, transaction_references, account_number=None, counterparty_code=None, catalogue_code=None, trade_type=None, contract_rate=None, account_name=None, value_date=None, reference_rate=None, swap_point=None, debit_currency=None, credit_currency=None, debit_by=None, debit_amount=None, debit_account_no_dpt=None, debit_account_no_act=None, debit_account_name=None, credit_by=None, credit_amount=None, credit_account_no_dpt=None, credit_account_no_act=None, credit_account_name=None, expected_posting=None):
        self.transaction_view(transaction_references, 'FX - Outright Account Amendment')
        # compare value
        if account_number:
            self.assertEqual(self.fo_get_value('Account number'), self.treasury_account_number_mask(account_number))
        if counterparty_code:
            self.assertEqual(self.fo_get_value_group('Counterparty code'), counterparty_code)
        if catalogue_code:
            self.assertEqual(self.fo_get_text_group('Catalogue code'), catalogue_code)
        if trade_type:
            self.assertEqual(self.fo_get_select('Trade type'), trade_type)
        if value_date:
            self.assertEqual(self.fo_get_date('Value date'), value_date)
        if account_name:
            self.assertEqual(self.fo_get_text('Account name'), account_name)
        if debit_currency:
            self.assertEqual(self.fo_get_select('Debit currency'), debit_currency)
        if credit_currency:
            self.assertEqual(self.fo_get_select('Credit currency'), credit_currency)
        if reference_rate:
            self.assertEqual(self.fo_get_value('Reference rate'), reference_rate)
        if swap_point:
            self.assertEqual(self.fo_get_value('Swap point'), swap_point)
        if contract_rate:
            self.assertEqual(self.fo_get_value('Contract rate'), contract_rate)
        # compare debit info
        if debit_by:
            self.assertEqual(self.get_text_input_below_border('Debit', 'Debit by'), debit_by)
        if debit_currency:
            self.assertEqual(self.get_text_input_below_border('Debit', 'Currency'), debit_currency)
        if debit_amount:
            self.assertEqual(self.get_text_input_below_border('Debit', 'Amount'), debit_amount)
        if debit_account_no_dpt:
            self.assertEqual(self.get_text_input_below_border('Debit', 'Account No. DPT'), debit_account_no_dpt)
        if debit_account_no_act:
            self.assertEqual(self.get_text_input_below_border('Debit', 'Account No. ACT'), debit_account_no_act)
        if debit_account_name:
            self.assertEqual(self.get_text_textarea_below_border('Debit', 'Account name'), debit_account_name)
        # compare credit info
        if credit_by:
            self.assertEqual(self.get_text_input_below_border('Credit', 'Credit by'), credit_by)
        if credit_currency:
            self.assertEqual(self.get_text_input_below_border('Credit', 'Currency'), credit_currency)
        if credit_amount:
            self.assertEqual(self.get_text_input_below_border('Credit', 'Amount'), credit_amount)
        if credit_account_no_dpt:
            self.assertEqual(self.get_text_input_below_border('Credit', 'Account No. DPT'), credit_account_no_dpt)
        if credit_account_no_act:
            self.assertEqual(self.get_text_input_below_border('Credit', 'Account No. ACT'), credit_account_no_act)
        if credit_account_name:
            self.assertEqual(self.get_text_textarea_below_border('Credit', 'Account name'), credit_account_name)
        if expected_posting:
            self.assert_posting_data(**expected_posting)

    # TFX_FCA: FX - Cancel Account
    def tfx_fca(self, account_number, counterparty_code=None, catalogue_code=None, trade_type=None, contract_rate=None, account_name=None, value_date=None, reference_rate=None, swap_point=None, debit_currency=None, credit_currency=None, debit_by=None, debit_amount=None, debit_account_no_dpt=None, debit_account_no_act=None, debit_account_name=None, credit_by=None, credit_amount=None, credit_account_no_dpt=None, credit_account_no_act=None, credit_account_name=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.open_fo('TFX_FCA', 'Cancel')
        self.wait_for_button_available('Accept')
        self.assert_form_title('FX - Cancel Account')
        # enter value
        self.fo_write('Account number', str(account_number).replace('-', ''))
        self.wait_loading()
        self.fo_write_text('Description', 'AUTO TEST')
        self.wait_loading()
        # compare value
        if counterparty_code:
            self.assertEqual(self.fo_get_value_group('Counterparty code'), counterparty_code)
        if catalogue_code:
            self.assertEqual(self.fo_get_text_group('Catalogue code'), catalogue_code)
        if trade_type:
            self.assertEqual(self.fo_get_select('Trade type'), trade_type)
        if value_date:
            self.assertEqual(self.fo_get_date('Value date'), value_date)
        if account_name:
            self.assertEqual(self.fo_get_text('Account name'), account_name)
        if debit_currency:
            self.assertEqual(self.fo_get_select('Debit currency'), debit_currency)
        if credit_currency:
            self.assertEqual(self.fo_get_select('Credit currency'), credit_currency)
        if reference_rate:
            self.assertEqual(self.fo_get_value('Reference rate'), reference_rate)
        if swap_point:
            self.assertEqual(self.fo_get_value('Swap point'), swap_point)
        if contract_rate:
            self.assertEqual(self.fo_get_value('Contract rate'), contract_rate)
        # compare debit info
        if debit_by:
            self.assertEqual(self.get_text_input_below_border('Debit', 'Debit by'), debit_by)
        if debit_currency:
            self.assertEqual(self.get_text_input_below_border('Debit', 'Currency'), debit_currency)
        if debit_amount:
            self.assertEqual(self.get_text_input_below_border('Debit', 'Amount'), debit_amount)
        if debit_account_no_dpt:
            self.assertEqual(self.get_text_input_below_border('Debit', 'Account No. DPT'), debit_account_no_dpt)
        if debit_account_no_act:
            self.assertEqual(self.get_text_input_below_border('Debit', 'Account No. ACT'), debit_account_no_act)
        if debit_account_name:
            self.assertEqual(self.get_text_textarea_below_border('Debit', 'Account name'), debit_account_name)
        # compare credit info
        if credit_by:
            self.assertEqual(self.get_text_input_below_border('Credit', 'Credit by'), credit_by)
        if credit_currency:
            self.assertEqual(self.get_text_input_below_border('Credit', 'Currency'), credit_currency)
        if credit_amount:
            self.assertEqual(self.get_text_input_below_border('Credit', 'Amount'), credit_amount)
        if credit_account_no_dpt:
            self.assertEqual(self.get_text_input_below_border('Credit', 'Account No. DPT'), credit_account_no_dpt)
        if credit_account_no_act:
            self.assertEqual(self.get_text_input_below_border('Credit', 'Account No. ACT'), credit_account_no_act)
        if credit_account_name:
            self.assertEqual(self.get_text_textarea_below_border('Credit', 'Account name'), credit_account_name)
        if ifc_codes:
            self.add_fees(ifc_codes, values, total_fee)
        self.fo_click_checkbox('Caution!  There is no doubt that banks may be used as a means of Money Laundering/ Terrorist Financing/ Proliferation of Weapons of Mass Destruction.')
        # click 'Accept'
        self.click_button('Accept')
        # approve
        if approve_later=='Y':
            self.click_button('Later')
        if approve_on_form=='Y':
            self.fo_approve_in_popup(
                username=username,
                password=password,
                reason=reason
            )
        if list_error_message:
        # verify error
            self.assert_error_message()
            self.assert_list_error_message(list_error_message)
            print('Transaction failed!')
        else:
        # verify success
            self.assert_button_disable('Accept')
            self.switch_to_core_banking()
            self.assert_notification('Saved successfully!')
            self.close_voucher()
            if expected_posting:
                self.assert_posting_data(**expected_posting)
            transaction_references=self.fo_get_text('Transaction references')
            print(f'Transaction references TFX_FCA: {transaction_references}')
            forex_account_mask=self.fo_get_value('Account number')
            print(f'Account number: {forex_account_mask}')
            return transaction_references, forex_account_mask

    def tfx_fca_view(self, transaction_references, account_number=None, counterparty_code=None, catalogue_code=None, trade_type=None, contract_rate=None, account_name=None, value_date=None, reference_rate=None, swap_point=None, debit_currency=None, credit_currency=None, debit_by=None, debit_amount=None, debit_account_no_dpt=None, debit_account_no_act=None, debit_account_name=None, credit_by=None, credit_amount=None, credit_account_no_dpt=None, credit_account_no_act=None, credit_account_name=None, expected_posting=None):
        self.transaction_view(transaction_references, 'FX - Cancel Account')
        # compare value
        if account_number:
            self.assertEqual(self.fo_get_value('Account number'), self.treasury_account_number_mask(account_number))
        if counterparty_code:
            self.assertEqual(self.fo_get_value_group('Counterparty code'), counterparty_code)
        if catalogue_code:
            self.assertEqual(self.fo_get_text_group('Catalogue code'), catalogue_code)
        if trade_type:
            self.assertEqual(self.fo_get_select('Trade type'), trade_type)
        if value_date:
            self.assertEqual(self.fo_get_date('Value date'), value_date)
        if account_name:
            self.assertEqual(self.fo_get_text('Account name'), account_name)
        if debit_currency:
            self.assertEqual(self.fo_get_select('Debit currency'), debit_currency)
        if credit_currency:
            self.assertEqual(self.fo_get_select('Credit currency'), credit_currency)
        if reference_rate:
            self.assertEqual(self.fo_get_value('Reference rate'), reference_rate)
        if swap_point:
            self.assertEqual(self.fo_get_value('Swap point'), swap_point)
        if contract_rate:
            self.assertEqual(self.fo_get_value('Contract rate'), contract_rate)
        # compare debit info
        if debit_by:
            self.assertEqual(self.get_text_input_below_border('Debit', 'Debit by'), debit_by)
        if debit_currency:
            self.assertEqual(self.get_text_input_below_border('Debit', 'Currency'), debit_currency)
        if debit_amount:
            self.assertEqual(self.get_text_input_below_border('Debit', 'Amount'), debit_amount)
        if debit_account_no_dpt:
            self.assertEqual(self.get_text_input_below_border('Debit', 'Account No. DPT'), debit_account_no_dpt)
        if debit_account_no_act:
            self.assertEqual(self.get_text_input_below_border('Debit', 'Account No. ACT'), debit_account_no_act)
        if debit_account_name:
            self.assertEqual(self.get_text_textarea_below_border('Debit', 'Account name'), debit_account_name)
        # compare credit info
        if credit_by:
            self.assertEqual(self.get_text_input_below_border('Credit', 'Credit by'), credit_by)
        if credit_currency:
            self.assertEqual(self.get_text_input_below_border('Credit', 'Currency'), credit_currency)
        if credit_amount:
            self.assertEqual(self.get_text_input_below_border('Credit', 'Amount'), credit_amount)
        if credit_account_no_dpt:
            self.assertEqual(self.get_text_input_below_border('Credit', 'Account No. DPT'), credit_account_no_dpt)
        if credit_account_no_act:
            self.assertEqual(self.get_text_input_below_border('Credit', 'Account No. ACT'), credit_account_no_act)
        if credit_account_name:
            self.assertEqual(self.get_text_textarea_below_border('Credit', 'Account name'), credit_account_name)
        if expected_posting:
            self.assert_posting_data(**expected_posting)

# -------------------------- handle FO - TRADE FINANCE --------------------------
    # TRD_SNI: SG/BG - Issue SG/BG for collection
    def trd_sni(self, category_code, account_holder_code, applicant, beneficiary, currency_code, issued_date, effect_date, guarantee_period, guarantee_period_unit, sg_bg_amount, project_name, bg_number, send_to, maturity_date=None, addition_margin_rate=None, margin_amount=None, guarantee_amount=None, secured_amount=None, country_code=None, beneficiary_address=None, account_holder_type=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.open_fo('TRD_SNI', '7738')
        self.wait_for_button_available('Accept')
        self.assert_form_title('7738: SG/BG - Issue SG/BG for collection')
        # enter value
        if account_holder_type:
            self.fo_select('Account holder type', account_holder_type)
        self.fo_write_group('Category code', category_code)
        self.fo_write_group('Account holder code', account_holder_code)
        self.fo_write_text('Applicant', applicant)
        self.fo_write_text('Beneficiary', beneficiary)
        if beneficiary_address:
            self.fo_write_text('Beneficiary address', beneficiary_address)
        self.fo_select('Currency code', currency_code)
        if country_code:
            self.fo_select('Country code', country_code)
        self.fo_write_date('Issued date', issued_date)
        self.fo_write_date('Effect date', effect_date)
        self.fo_select('Guarantee period', guarantee_period)
        self.fo_select('Guarantee period unit', guarantee_period_unit)
        if maturity_date:
            self.fo_assert_date('Maturity date', maturity_date)
        self.fo_write_number('SG/BG amount', str(sg_bg_amount).replace(',', ''))
        if self.fo_get_value('SG/BG amount')!= sg_bg_amount:
            self.fo_write_number('SG/BG amount', str(sg_bg_amount).replace(',', ''))
        if addition_margin_rate:
            self.fo_write_number('Addition margin rate', str(addition_margin_rate).replace('.00', ''))
            if self.fo_get_value('Addition margin rate')!= str(addition_margin_rate).replace('.00', ''):
                self.fo_write_number('Addition margin rate', str(addition_margin_rate).replace('.00', ''))
        if margin_amount:
            self.fo_assert_value('Margin amount', margin_amount)
        if guarantee_amount:
            self.fo_assert_value('Guarantee amount', guarantee_amount)
        if secured_amount:
            self.fo_write_number('Secured amount', str(secured_amount).replace(',', ''))
            if self.fo_get_value('Secured amount')!= secured_amount:
                self.fo_write_number('Secured amount', str(secured_amount).replace(',', ''))
            self.key_escape()
        self.fo_write_text('Project name', project_name)
        self.fo_write_text('BG number', bg_number)
        self.fo_write_text_multi_line('Send to', send_to)
        self.fo_write_text('Description', 'AUTO TEST')
        if ifc_codes:
            self.add_fees(ifc_codes, values, total_fee)
        self.wait_loading()
        self.fo_click_checkbox('Caution!  There is no doubt that banks may be used as a means of Money Laundering/ Terrorist Financing/ Proliferation of Weapons of Mass Destruction.')
        # click 'Accept'
        self.click_button('Accept')
        # approve
        if approve_later=='Y':
            self.click_button('Later')
        if approve_on_form=='Y':
            self.fo_approve_in_popup(
                username=username,
                password=password,
                reason=reason
            )
        if list_error_message:
        # verify error
            self.assert_error_message()
            self.assert_list_error_message(list_error_message)
            print('Transaction failed!')
        else:
        # verify success
            self.assert_button_disable('Accept')
            self.switch_to_core_banking()
            self.assert_notification('Saved successfully!')
            self.close_voucher()
            if expected_posting:
                self.assert_posting_data(**expected_posting)
            transaction_references=self.fo_get_text('Transaction references')
            print(f'Transaction references TRD_SNI: {transaction_references}')
            trade_account_mask=self.fo_get_value('Account number')
            print(f'Account number: {trade_account_mask}')
            return transaction_references, trade_account_mask

    def trd_sni_view(self, transaction_references, account_number=None, category_code=None, account_holder_code=None, applicant=None, beneficiary=None, currency_code=None, issued_date=None, effect_date=None, guarantee_period=None, guarantee_period_unit=None, sg_bg_amount=None, project_name=None, bg_number=None, send_to=None, maturity_date=None, addition_margin_rate=None, margin_amount=None, guarantee_amount=None, secured_amount=None, country_code=None, beneficiary_address=None, account_holder_type=None, description=None, expected_posting=None):
        self.transaction_view(transaction_references, '7738: SG/BG - Issue SG/BG for collection')
        # compare value
        if account_number:
            self.fo_assert_value('Account number', self.trade_account_number_mask(account_number))
        if account_holder_type:
            self.fo_assert_select('Account holder type', account_holder_type)
        if category_code:
            self.fo_assert_value_group('Category code', category_code)
        if account_holder_code:
            self.fo_assert_value_group('Account holder code', account_holder_code)
        if applicant:
            self.fo_assert_text('Applicant', applicant)
        if beneficiary:
            self.fo_assert_text('Beneficiary', beneficiary)
        if beneficiary_address:
            self.fo_assert_text('Beneficiary address', beneficiary_address)
        if currency_code:
            self.fo_assert_select('Currency code', currency_code)
        if country_code:
            self.fo_assert_select('Country code', country_code)
        if issued_date:
            self.fo_assert_date('Issued date', issued_date)
        if effect_date:
            self.fo_assert_date('Effect date', effect_date)
        if guarantee_period:
            self.fo_assert_select('Guarantee period', guarantee_period)
        if guarantee_period_unit:
            self.fo_assert_select('Guarantee period unit', guarantee_period_unit)
        if maturity_date:
            self.fo_assert_date('Maturity date', maturity_date)
        if sg_bg_amount:
            self.fo_assert_value('SG/BG amount', sg_bg_amount)
        if addition_margin_rate:
            self.fo_assert_value('Addition margin rate', str(addition_margin_rate).replace('.00', ''))
        if margin_amount:
            self.fo_assert_value('Margin amount', margin_amount)
        if guarantee_amount:
            self.fo_assert_value('Guarantee amount', guarantee_amount)
        if secured_amount:
            self.fo_assert_value('Secured amount', secured_amount)
        if description:
            self.fo_assert_text('Description', description)
        if project_name:
            self.fo_assert_text('Project name', project_name)
        if bg_number:
            self.fo_assert_text('BG number', bg_number)
        if send_to:
            self.fo_assert_text_multi_line('Send to', send_to)
        if expected_posting:
            self.assert_posting_data(**expected_posting)
        trade_account_mask=self.fo_get_value('Account number')
        print(f'Account number: {trade_account_mask}')
        return transaction_references, trade_account_mask

    # TRD_GSC: 7734: OLC - Guarantee by secure collateral
    def trd_gsc(self, mortgage_account_number, trade_finance_account_number, amount_secure_from_this_asset, mortgage_account_currency=None, asset_booking_value=None, total_secured_amount_of_mortgage=None, trade_finance_account_currency=None, secure_required=None, secured_amount_for_tf_account=None, total_secured_amount_of_tf_account=None, amount_secured_for_tf_account=None, exchange_rate=None, customer_code=None, customer_name=None, customer_address=None, customer_description=None, base_amount=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.open_fo('TRD_GSC', '7734')
        self.wait_for_button_available('Accept')
        self.assert_form_title('7734: OLC - Guarantee by secure collateral')
        # enter value
        self.fo_write_group('Mortgage account number', mortgage_account_number)
        self.wait_loading()
        if mortgage_account_currency:
            self.fo_assert_select('Mortgage account currency', mortgage_account_currency)
        if asset_booking_value:
            self.fo_assert_value('Asset booking value', asset_booking_value)
        if total_secured_amount_of_mortgage:
            self.fo_assert_value('Total secured amount of Mortgage', total_secured_amount_of_mortgage)
        self.fo_write_group('Trade finance account number', trade_finance_account_number)
        self.wait_loading()
        if trade_finance_account_currency:
            self.fo_assert_select('Trade finance account currency', trade_finance_account_currency)
        if secure_required:
            self.fo_assert_value('Secure required', secure_required)
        if secured_amount_for_tf_account:
            self.fo_assert_value('Secured amount for TF account', secured_amount_for_tf_account)
        if total_secured_amount_of_tf_account:
            self.fo_assert_value('Total secured amount of TF account', total_secured_amount_of_tf_account)
        if amount_secure_from_this_asset:
            self.fo_write_number('Amount secure from this asset', str(amount_secure_from_this_asset).replace(',', ''))
            if self.fo_get_value('Amount secure from this asset') != amount_secure_from_this_asset:
                self.fo_write_number('Amount secure from this asset', str(amount_secure_from_this_asset).replace(',', ''))
            self.fo_assert_value_group('Amount secured for TF account', amount_secure_from_this_asset)
        if amount_secured_for_tf_account:
            self.fo_write_number_group('Amount secured for TF account', str(amount_secured_for_tf_account).replace(',', ''))
            if self.fo_get_value_group('Amount secured for TF account') != amount_secured_for_tf_account:
                self.fo_write_number_group('Amount secured for TF account', str(amount_secured_for_tf_account).replace(',', ''))
        if exchange_rate:
            self.fo_assert_value('Exchange rate', exchange_rate)
        if customer_code:
            self.fo_assert_value('Customer code', customer_code)
        if customer_name:
            self.fo_assert_text('Customer name', customer_name)
        if customer_address:
            self.fo_assert_text('Customer address', customer_address)
        if customer_description:
            self.fo_write_text('Customer description', customer_description)
        if base_amount:
            self.fo_assert_value('Base amount', base_amount)
        self.fo_write_text('Description', 'AUTO TEST')
        if ifc_codes:
            self.add_fees(ifc_codes, values, total_fee)
        self.wait_loading()
        self.fo_click_checkbox('Caution!  There is no doubt that banks may be used as a means of Money Laundering/ Terrorist Financing/ Proliferation of Weapons of Mass Destruction.')
        # click 'Accept'
        self.click_button('Accept')
        if approve_later=='Y':
            self.click_button('Later')
        if approve_on_form=='Y':
            self.fo_approve_in_popup(
                username=username,
                password=password,
                reason=reason
            )
        if list_error_message:
        # verify error
            self.assert_error_message()
            self.assert_list_error_message(list_error_message)
            print('Transaction failed!')
        else:
        # verify success
            self.assert_button_disable('Accept')
            self.switch_to_core_banking()
            self.assert_notification('Saved successfully!')
            self.close_voucher()
            if expected_posting:
                self.assert_posting_data(**expected_posting)
            transaction_references=self.fo_get_text('Transaction references')
            print(f'Transaction references TRD_GSC: {transaction_references}')
            mortgage_account_mask=self.fo_get_value_group('Mortgage account number')
            print(f'Mortgage account number: {mortgage_account_mask}')
            trade_account_mask=self.fo_get_value_group('Trade finance account number')
            print(f'Trade finance account number: {trade_account_mask}')
            return transaction_references, mortgage_account_mask, trade_account_mask

    def trd_gsc_view(self, transaction_references, mortgage_account_number=None, mortgage_account_currency=None, asset_booking_value=None, total_secured_amount_of_mortgage=None, trade_finance_account_number=None, trade_finance_account_currency=None, secure_required=None, secured_amount_for_tf_account=None, total_secured_amount_of_tf_account=None, amount_secure_from_this_asset=None, amount_secured_for_tf_account=None, exchange_rate=None, customer_code=None, customer_name=None, customer_address=None, customer_description=None, base_amount=None, description=None, expected_posting=None):
        self.transaction_view(transaction_references, '7734: OLC - Guarantee by secure collateral')
        # compare value
        if mortgage_account_number:
            self.fo_assert_value_group('Mortgage account number', mortgage_account_number)
        if mortgage_account_currency:
            self.fo_assert_select('Mortgage account currency', mortgage_account_currency)
        if asset_booking_value:
            self.fo_assert_value('Asset booking value', asset_booking_value)
        if total_secured_amount_of_mortgage:
            self.fo_assert_value('Total secured amount of Mortgage', total_secured_amount_of_mortgage)
        if trade_finance_account_number:
            self.fo_assert_value_group('Trade finance account number', trade_finance_account_number)
        if trade_finance_account_currency:
            self.fo_assert_select('Trade finance account currency', trade_finance_account_currency)
        if secure_required:
            self.fo_assert_value('Secure required', secure_required)
        if secured_amount_for_tf_account:
            self.fo_assert_value('Secured amount for TF account', secured_amount_for_tf_account)
        if total_secured_amount_of_tf_account:
            self.fo_assert_value('Total secured amount of TF account', total_secured_amount_of_tf_account)
        if amount_secure_from_this_asset:
            self.fo_assert_value('Amount secure from this asset', amount_secure_from_this_asset)
        if amount_secured_for_tf_account:
            self.fo_assert_value_group('Amount secured for TF account', amount_secured_for_tf_account)
        if exchange_rate:
            self.fo_assert_value('Exchange rate', exchange_rate)
        if customer_code:
            self.fo_assert_value('Customer code', customer_code)
        if customer_name:
            self.fo_assert_text('Customer name', customer_name)
        if customer_address:
            self.fo_assert_text('Customer address', customer_address)
        if customer_description:
            self.fo_assert_text('Customer description', customer_description)
        if base_amount:
            self.fo_assert_value('Base amount', base_amount)
        if description:
            self.fo_assert_text('Description', description)
        if expected_posting:
            self.assert_posting_data(**expected_posting)
        mortgage_account_mask=self.fo_get_value_group('Mortgage account number')
        print(f'Mortgage account number: {mortgage_account_mask}')
        trade_account_mask=self.fo_get_value_group('Trade finance account number')
        print(f'Trade finance account number: {trade_account_mask}')
        return transaction_references, mortgage_account_mask, trade_account_mask

    # TRD_SIV: SG - Insurance verify
    def trd_siv(self, account_number, sg_bg_amount=None, margin_rate=None, margin_amount=None, guarantee_amount=None, secured_amount=None, margin_method=None, margin_deposit_account=None, cheque_no=None, applicant=None, applicant_address=None, applicant_more_description=None, beneficiary=None, beneficiary_address=None, total_fee_amount=None, fee_collect_method=None, account_number_for_fee=None, ifc_code=None, value=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.open_fo('TRD_SIV', 'Issurance verify')
        self.wait_for_button_available('Accept')
        self.assert_form_title('SG - Issurance verify')
        # enter value
        self.fo_write_group('Account number', account_number)
        if ifc_code:
            # add fee
            self.click_button('Add')
            self.wait_loading()
            self.fo_write_text_group('Interest/fee/charge code', ifc_code)
            self.wait_loading()
            self.fo_write_number('Value', str(value).replace(',', ''))
            self.wait_loading()
            self.click_button('Apply')
            self.wait_loading()
            if total_fee:
                self.assert_total_fee_table_data(total_fee)
            if total_fee_amount:
                self.fo_assert_value('Total fee amount', total_fee_amount)
        if sg_bg_amount:
            self.fo_assert_value('SG/BG amount', sg_bg_amount)
        if margin_rate:
            self.fo_assert_value('Margin rate', margin_rate)
        if margin_amount:
            self.fo_assert_value('Margin amount', margin_amount)
        if guarantee_amount:
            self.fo_assert_value('Guarantee amount', guarantee_amount)
        if secured_amount:
            self.fo_assert_value('Secured amount', secured_amount)
        if margin_method:
            self.fo_select('Margin method', margin_method)
        if cheque_no:
            self.fo_write('Cheque no', cheque_no)
            self.wait_loading()
            self.fo_assert_value_group('Margin deposit account', margin_deposit_account)
        if margin_deposit_account:
            self.fo_write_group('Margin deposit account', margin_deposit_account)
        if applicant:
            self.fo_assert_text('Applicant', applicant)
        if applicant_address:
            self.fo_assert_text('Applicant address', applicant_address)
        if applicant_more_description:
            self.fo_assert_text('Applicant more description', applicant_more_description)
        if beneficiary:
            self.fo_assert_text('Beneficiary', beneficiary)
        if beneficiary_address:
            self.fo_assert_text('Beneficiary address', beneficiary_address)
        if fee_collect_method:
            self.fo_select('Fee collect method', fee_collect_method)
        if account_number_for_fee:
            self.fo_write_group('Account number for fee', str(account_number_for_fee).replace('-', ''))
        self.fo_write_text('Description', 'AUTO TEST')
        self.key_escape()
        self.wait_loading()
        self.fo_click_checkbox('Caution!  There is no doubt that banks may be used as a means of Money Laundering/ Terrorist Financing/ Proliferation of Weapons of Mass Destruction.')
        # click 'Accept'
        self.click_button('Accept')
        # approve
        if approve_later=='Y':
            self.click_button('Later')
        if approve_on_form=='Y':
            self.fo_approve_in_popup(
                username=username,
                password=password,
                reason=reason
            )
        if list_error_message:
        # verify error
            self.assert_error_message()
            self.assert_list_error_message(list_error_message)
            print('Transaction failed!')
        else:
        # verify success
            self.assert_button_disable('Accept')
            self.switch_to_core_banking()
            self.assert_notification('Saved successfully!')
            self.close_voucher()
            if expected_posting:
                self.assert_posting_data(**expected_posting)
            transaction_references=self.fo_get_text('Transaction references')
            print(f'Transaction references TRD_SIV: {transaction_references}')
            trade_account_mask=self.fo_get_value_group('Account number')
            print(f'Account number: {trade_account_mask}')
            return transaction_references, trade_account_mask

    def trd_siv_view(self, transaction_references, account_number=None, sg_bg_amount=None, margin_rate=None, margin_amount=None, guarantee_amount=None, secured_amount=None, margin_method=None, margin_deposit_account=None, cheque_no=None, applicant=None, applicant_address=None, applicant_more_description=None, beneficiary=None, beneficiary_address=None, total_fee_amount=None, fee_collect_method=None, account_number_for_fee=None, ifc_code=None, value=None, total_fee=None, description=None, expected_posting=None):
        self.transaction_view(transaction_references, 'SG - Issurance verify')
        # compare value
        if account_number:
            self.fo_assert_value_group('Account number', self.trade_account_number_mask(account_number))
        if sg_bg_amount:
            self.fo_assert_value('SG/BG amount', sg_bg_amount)
        if margin_rate:
            self.fo_assert_value('Margin rate', margin_rate)
        if margin_amount:
            self.fo_assert_value('Margin amount', margin_amount)
        if guarantee_amount:
            self.fo_assert_value('Guarantee amount', guarantee_amount)
        if secured_amount:
            self.fo_assert_value('Secured amount', secured_amount)
        if margin_method:
            self.fo_assert_select('Margin method', margin_method)
        if margin_deposit_account:
            self.fo_assert_value_group('Margin deposit account', margin_deposit_account)
        if cheque_no:
            self.fo_assert_value('Cheque no', cheque_no)
        if applicant:
            self.fo_assert_text('Applicant', applicant)
        if applicant_address:
            self.fo_assert_text('Applicant address', applicant_address)
        if applicant_more_description:
            self.fo_assert_text('Applicant more description', applicant_more_description)
        if beneficiary:
            self.fo_assert_text('Beneficiary', beneficiary)
        if beneficiary_address:
            self.fo_assert_text('Beneficiary address', beneficiary_address)
        if total_fee_amount:
            self.fo_assert_value('Total fee amount', total_fee_amount)
        if description:
            self.fo_assert_text('Description', description)
        if fee_collect_method:
            self.fo_assert_select('Fee collect method', fee_collect_method)
        if account_number_for_fee:
            self.fo_assert_value_group('Account number for fee', account_number_for_fee)
        if ifc_code:
            self.assert_table_data('IFC code', 1, ifc_code)
            self.assert_table_data('Value type', 1, 'Percentage')
            self.assert_table_data('Fee', 1, total_fee_amount)
        if value:
            self.assert_table_data('Value', 1, value)
        if total_fee:
            self.assert_total_fee_table_data(total_fee)
        if expected_posting:
            self.assert_posting_data(**expected_posting)
        trade_account_mask=self.fo_get_value_group('Account number')
        print(f'Account number: {trade_account_mask}')
        return transaction_references, trade_account_mask

    # TRD_RSC: 7757: OLC - Release secure collateral
    def trd_rsc(self, mortgage_account_number, trade_finance_account_number, release_amount_in_mortgage_currency, asset_booking_value=None, mortgage_account_currency=None, trade_finance_account_currency=None, exchange_rate=None, release_amount_in_tf_currency=None, customer_code=None, customer_name=None, customer_address=None, customer_description=None, base_amount=None, secured_amount_for_tf_account=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.open_fo('TRD_RSC', 'Release')
        self.wait_for_button_available('Accept')
        self.assert_form_title('7757: OLC - Release secure collateral')
        # enter value
        self.fo_write_group('Mortgage account number', mortgage_account_number)
        self.wait_loading()
        if asset_booking_value:
            self.fo_assert_value('Asset booking value', asset_booking_value)
        if mortgage_account_currency:
            self.fo_assert_select('Mortgate account currency', mortgage_account_currency)
        self.fo_write_group('Trade finance account number', trade_finance_account_number)
        self.wait_loading()
        if trade_finance_account_currency:
            self.fo_assert_select('Trade finance account currency', trade_finance_account_currency)
        if secured_amount_for_tf_account:
            self.fo_assert_value('Secured amount for TF account', secured_amount_for_tf_account)
        if exchange_rate:
            self.fo_assert_value('Exchange rate', exchange_rate)
        if release_amount_in_mortgage_currency:
            self.fo_write_number('Release amount in mortgage currency', str(release_amount_in_mortgage_currency).replace(',', ''))
            if self.fo_get_value('Release amount in mortgage currency') != release_amount_in_mortgage_currency:
                self.fo_write_number('Release amount in mortgage currency', str(release_amount_in_mortgage_currency).replace(',', ''))
            self.fo_assert_value_group('Release amount in TF currency', release_amount_in_mortgage_currency)
        if release_amount_in_tf_currency:
            self.fo_write_number_group('Release amount in TF currency', str(release_amount_in_tf_currency).replace(',', ''))
            if self.fo_get_value_group('Release amount in TF currency') != release_amount_in_tf_currency:
                self.fo_write_number_group('Release amount in TF currency', str(release_amount_in_tf_currency).replace(',', ''))
        if customer_code:
            self.fo_assert_value('Customer code', customer_code)
        if customer_name:
            self.fo_assert_text('Customer name', customer_name)
        if customer_address:
            self.fo_assert_text('Customer address', customer_address)
        if customer_description:
            self.fo_assert_text('Customer description', customer_description)
        if base_amount:
            self.fo_assert_value('Base amount', base_amount)
        self.fo_write_text('Description', 'AUTO TEST')
        if ifc_codes:
            self.add_fees(ifc_codes, values, total_fee)
        self.wait_loading()
        self.fo_click_checkbox('Caution!  There is no doubt that banks may be used as a means of Money Laundering/ Terrorist Financing/ Proliferation of Weapons of Mass Destruction.')
        # click 'Accept'
        self.click_button('Accept')
        # approve
        if approve_later=='Y':
            self.click_button('Later')
        if approve_on_form=='Y':
            self.fo_approve_in_popup(
                username=username,
                password=password,
                reason=reason
            )
        if list_error_message:
        # verify error
            self.assert_error_message()
            self.assert_list_error_message(list_error_message)
            print('Transaction failed!')
        else:
        # verify success
            self.assert_button_disable('Accept')
            self.switch_to_core_banking()
            self.assert_notification('Saved successfully!')
            self.close_voucher()
            if expected_posting:
                self.assert_posting_data(**expected_posting)
            transaction_references=self.fo_get_text('Transaction references')
            print(f'Transaction references TRD_RSC: {transaction_references}')
            mortgage_account_mask=self.fo_get_value_group('Mortgage account number')
            print(f'Mortgage account number: {mortgage_account_mask}')
            trade_account_mask=self.fo_get_value_group('Trade finance account number')
            print(f'Trade finance account number: {trade_account_mask}')
            return transaction_references, mortgage_account_mask, trade_account_mask

    def trd_rsc_view(self, transaction_references, mortgage_account_number=None, asset_booking_value=None, mortgage_account_currency=None, trade_finance_account_number=None, trade_finance_account_currency=None, exchange_rate=None, release_amount_in_mortgage_currency=None, release_amount_in_tf_currency=None, customer_code=None, customer_name=None, customer_address=None, customer_description=None, base_amount=None, description=None, secured_amount_for_tf_account=None, expected_posting=None):
        self.transaction_view(transaction_references, '7757: OLC - Release secure collateral')
        # compare value
        if mortgage_account_number:
            self.fo_assert_value_group('Mortgage account number', mortgage_account_number)
        if asset_booking_value:
            self.fo_assert_value('Asset booking value', asset_booking_value)
        if mortgage_account_currency:
            self.fo_assert_select('Mortgate account currency', mortgage_account_currency)
        if trade_finance_account_number:
            self.fo_assert_value_group('Trade finance account number', trade_finance_account_number)
        if trade_finance_account_currency:
            self.fo_assert_select('Trade finance account currency', trade_finance_account_currency)
        if secured_amount_for_tf_account:
            self.fo_assert_value('Secured amount for TF account', secured_amount_for_tf_account)
        if exchange_rate:
            self.fo_assert_value('Exchange rate', exchange_rate)
        if release_amount_in_mortgage_currency:
            self.fo_assert_value('Release amount in mortgage currency', release_amount_in_mortgage_currency)
        if release_amount_in_tf_currency:
            self.fo_assert_value_group('Release amount in TF currency', release_amount_in_tf_currency)
        if customer_code:
            self.fo_assert_value('Customer code', customer_code)
        if customer_name:
            self.fo_assert_text('Customer name', customer_name)
        if customer_address:
            self.fo_assert_text('Customer address', customer_address)
        if customer_description:
            self.fo_assert_text('Customer description', customer_description)
        if base_amount:
            self.fo_assert_value('Base amount', base_amount)
        if description:
            self.fo_assert_text('Description', description)
        if expected_posting:
            self.assert_posting_data(**expected_posting)
        mortgage_account_mask=self.fo_get_value_group('Mortgage account number')
        print(f'Mortgage account number: {mortgage_account_mask}')
        trade_account_mask=self.fo_get_value_group('Trade finance account number')
        print(f'Trade finance account number: {trade_account_mask}')
        return transaction_references, mortgage_account_mask, trade_account_mask

    # TRD_SBX: SG/BG - Extension
    def trd_sbx(self, account_number, beneficiary=None, maturity_date=None, extend_period=None, bg_number=None, fee_collect_method=None, total_fee_amount=None, applicant=None, sg_bg_amount=None, extend_to_date=None, extend_period_unit=None, extension_time=None, extension_date=None, account_number_for_fee=None, ifc_code=None, value=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.open_fo('TRD_SBX', 'Extension')
        self.wait_for_button_available('Accept')
        self.assert_form_title('SG/BG - Extension')
        # enter value
        self.fo_write_group('Account number', str(account_number).replace('-', ''))
        self.wait_loading()
        self.key_escape()
        if applicant:
            self.fo_assert_text_group('Applicant', applicant)
        if beneficiary:
            self.fo_assert_text('Beneficiary', beneficiary)
        if sg_bg_amount:
            self.fo_assert_value('SG/BG Amount', sg_bg_amount)
        if maturity_date:
            self.fo_assert_date('Maturity date', maturity_date)
        if extension_date:
            self.fo_write_date('Extension date', extension_date)
        if extend_period:
            self.fo_select('Extend period', extend_period)
        if extend_period_unit:
            self.fo_select('Extend period unit', extend_period_unit)
        if extend_to_date:
            self.fo_assert_date('Extend to date', extend_to_date)
        if bg_number:
            self.fo_assert_text('BG number', bg_number)
        if extension_time:
            self.fo_assert_value('Extension time', extension_time)
            self.fo_assert_text('Extension BG number', f'{bg_number} Ex-{extension_time}')
        # add fee
        if ifc_code:
            self.click_button('Add')
            self.wait_loading()
            self.fo_write_text_group('Interest/fee/charge code', ifc_code)
            self.wait_loading()
            self.fo_write_number('Value', str(value).replace(',', ''))
            self.wait_loading()
            self.click_button('Apply')
            self.wait_loading()
            if total_fee:
                self.assert_total_fee_table_data(total_fee)
            if total_fee_amount:
                self.fo_assert_value('Total fee amount', total_fee_amount)
        if fee_collect_method:
            self.fo_select('Fee collect method', fee_collect_method)
        if account_number_for_fee:
            self.fo_write_text_group('Account number for fee', str(account_number_for_fee).replace('-', ''))
        self.fo_write_text('Description', 'AUTO TEST')
        self.key_escape()
        self.wait_loading()
        self.fo_click_checkbox('Caution!  There is no doubt that banks may be used as a means of Money Laundering/ Terrorist Financing/ Proliferation of Weapons of Mass Destruction.')
        # click 'Accept'
        self.click_button('Accept')
        # approve
        if approve_later=='Y':
            self.click_button('Later')
        if approve_on_form=='Y':
            self.fo_approve_in_popup(
                username=username,
                password=password,
                reason=reason
            )
        if list_error_message:
        # verify error
            self.assert_error_message()
            self.assert_list_error_message(list_error_message)
            print('Transaction failed!')
        else:
        # verify success
            self.assert_button_disable('Accept')
            self.switch_to_core_banking()
            self.assert_notification('Saved successfully!')
            self.close_voucher()
            if expected_posting:
                self.assert_posting_data(**expected_posting)
            transaction_references=self.fo_get_text('Transaction references')
            print(f'Transaction references TRD_SBX: {transaction_references}')
            trade_account_mask=self.fo_get_value_group('Account number')
            print(f'Account number: {trade_account_mask}')
            return transaction_references, trade_account_mask

    def trd_sbx_view(self, transaction_references, account_number=None, beneficiary=None, maturity_date=None, extend_period=None, bg_number=None, fee_collect_method=None, total_fee_amount=None, applicant=None, sg_bg_amount=None, extend_to_date=None, extend_period_unit=None, extension_time=None, extension_date=None, account_number_for_fee=None, ifc_code=None, value=None, total_fee=None, description=None, expected_posting=None):
        self.transaction_view(transaction_references, 'SG/BG - Extension')
        # compare value
        if account_number:
            self.fo_assert_value_group('Account number', self.trade_account_number_mask(account_number))
        if applicant:
            self.fo_assert_text_group('Applicant', applicant)
        if beneficiary:
            self.fo_assert_text('Beneficiary', beneficiary)
        if sg_bg_amount:
            self.fo_assert_value('SG/BG Amount', sg_bg_amount)
        if maturity_date:
            self.fo_assert_date('Maturity date', maturity_date)
        if extend_to_date:
            self.fo_assert_date('Extend to date', extend_to_date)
        if extend_period:
            self.fo_assert_select('Extend period', extend_period)
        if extend_period_unit:
            self.fo_assert_select('Extend period unit', extend_period_unit)
        if bg_number:
            self.fo_assert_text('BG number', bg_number)
        if extension_time:
            self.fo_assert_value('Extension time', extension_time)
            self.fo_assert_text('Extension BG number', f'{bg_number} Ex-{extension_time}')
        if extension_date:
            self.fo_assert_date('Extension date', extension_date)
        if fee_collect_method:
            self.fo_assert_select('Fee collect method', fee_collect_method)
        if account_number_for_fee:
            self.fo_assert_text_group('Account number for fee', account_number_for_fee)
        if total_fee_amount:
            self.fo_assert_value('Total fee amount', total_fee_amount)
        if description:
            self.fo_assert_text('Description', description)
        if ifc_code:
            self.assert_table_data('IFC code', 1, ifc_code)
            self.assert_table_data('Value type', 1, 'Percentage')
            self.assert_table_data('Fee', 1, total_fee_amount)
        if value:
            self.assert_table_data('Value', 1, value)
        if total_fee:
            self.assert_total_fee_table_data(total_fee)
        if expected_posting:
            self.assert_posting_data(**expected_posting)
        trade_account_mask=self.fo_get_value_group('Account number')
        print(f'Account number: {trade_account_mask}')
        return transaction_references, trade_account_mask

    # TRD_FCC: 7728: IFC - Fee collection
    def trd_fcc(self, account_number, account_holder_type=None, account_holder_code=None, country_code=None, currency_code=None, applicant=None, beneficiary=None, total_fee_amount=None, fee_collect_method=None, account_number_for_fee=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.open_fo('TRD_FCC', '7728')
        self.wait_for_button_available('Accept')
        self.assert_form_title('7728: IFC - Fee collection')
        # enter value
        account_number_value = str(account_number).replace('-', '')
        self.fo_write_group('Account number', account_number_value)
        self.wait_loading()
        self.key_escape()
        if account_holder_type:
            self.fo_assert_select('Account holder type', account_holder_type)
        if account_holder_code:
            self.fo_assert_value('Account holder code', account_holder_code)
        if country_code:
            self.fo_assert_text_group('Country code', country_code)
        if currency_code:
            self.fo_assert_select('Currency code', currency_code)
        if applicant:
            self.fo_assert_text('Applicant', applicant)
        if beneficiary:
            self.fo_assert_text('Beneficiary', beneficiary)
        if ifc_codes:
            self.add_fees(ifc_codes, values, total_fee=total_fee)
            if total_fee_amount:
                self.fo_assert_value('Total fee amount', total_fee_amount)
        if fee_collect_method:
            self.fo_select('Fee collect method', fee_collect_method)
        if account_number_for_fee:
            account_number_for_fee_value = str(account_number_for_fee).replace('-', '')
            self.fo_write_text_group('Account number for fee', account_number_for_fee_value)
        self.fo_write_text('Description', 'AUTO TEST')
        self.key_escape()
        self.wait_loading()
        self.fo_click_checkbox('Caution!  There is no doubt that banks may be used as a means of Money Laundering/ Terrorist Financing/ Proliferation of Weapons of Mass Destruction.')
        # click 'Accept'
        self.click_button('Accept')
        # approve
        if approve_later=='Y':
            self.click_button('Later')
        if approve_on_form=='Y':
            self.fo_approve_in_popup(
                username=username,
                password=password,
                reason=reason
            )
        if list_error_message:
        # verify error
            self.assert_error_message()
            self.assert_list_error_message(list_error_message)
            print('Transaction failed!')
        else:
        # verify success
            self.assert_button_disable('Accept')
            self.switch_to_core_banking()
            self.assert_notification('Saved successfully!')
            self.close_voucher()
            if expected_posting:
                self.assert_posting_data(**expected_posting)
            transaction_references=self.fo_get_text('Transaction references')
            print(f'Transaction references TRD_FCC: {transaction_references}')
            trade_account_mask=self.fo_get_value_group('Account number')
            print(f'Account number: {trade_account_mask}')
            return transaction_references, trade_account_mask

    def trd_fcc_view(self, transaction_references, account_number=None, account_holder_type=None, account_holder_code=None, country_code=None, currency_code=None, applicant=None, beneficiary=None, total_fee_amount=None, fee_collect_method=None, account_number_for_fee=None, ifc_code=None, value=None, total_fee=None, description=None, expected_posting=None):
        self.transaction_view(transaction_references, '7728: IFC - Fee collection')
        # compare value
        if account_number:
            self.fo_assert_value_group('Account number', self.trade_account_number_mask(account_number))
        if account_holder_type:
            self.fo_assert_select('Account holder type', account_holder_type)
        if account_holder_code:
            self.fo_assert_value('Account holder code', account_holder_code)
        if country_code:
            self.fo_assert_text_group('Country code', country_code)
        if currency_code:
            self.fo_assert_select('Currency code', currency_code)
        if applicant:
            self.fo_assert_text('Applicant', applicant)
        if beneficiary:
            self.fo_assert_text('Beneficiary', beneficiary)
        if total_fee_amount:
            self.fo_assert_value('Total fee amount', total_fee_amount)
        if fee_collect_method:
            self.fo_assert_select('Fee collect method', fee_collect_method)
        if account_number_for_fee:
            self.fo_assert_text_group('Account number for fee', account_number_for_fee)
        if description:
            self.fo_assert_text('Description', description)
        if ifc_code:
            self.assert_table_data('IFC code', 1, ifc_code)
            self.assert_table_data('Value type', 1, 'Flat amount')
            self.assert_table_data('Fee', 1, total_fee_amount)
        if value:
            self.assert_table_data('Value', 1, value)
        if total_fee:
            self.assert_total_fee_table_data(total_fee)
        if expected_posting:
            self.assert_posting_data(**expected_posting)
        trade_account_mask=self.fo_get_value_group('Account number')
        print(f'Account number: {trade_account_mask}')
        return transaction_references, trade_account_mask

    # TRD_SCL: 7758: SG - Close
    def trd_scl(self, account_number, sg_bg_amount=None, margin_rate=None, margin_amount=None, guarantee_amount=None, secured_amount=None, margin_method=None, margin_deposit_account=None, applicant=None, bg_number=None, beneficiary=None, beneficiary_address=None, maturity_date=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.open_fo('TRD_SCL', 'Close')
        self.wait_for_button_available('Accept')
        self.assert_form_title('7758: SG - Close')
        # enter value
        self.fo_write_group('Account number', str(account_number).replace('-', ''))
        self.wait_loading()
        self.key_escape()
        self.fo_select('Margin method', 'Cash')
        if sg_bg_amount:
            self.fo_assert_value('SG/BG amount', sg_bg_amount)
        if margin_rate:
            self.fo_assert_value('Margin rate', margin_rate)
        if margin_amount:
            self.fo_assert_value('Margin amount', margin_amount)
        if guarantee_amount:
            self.fo_assert_value('Guarantee amount', guarantee_amount)
        if secured_amount:
            self.fo_assert_value('Secured amount', secured_amount)
        if margin_method:
            self.fo_select('Margin method', margin_method)
        if margin_deposit_account:
            self.fo_write_group('Margin deposit account', margin_deposit_account)
        if applicant:
            self.fo_assert_text_group('Applicant', applicant)
        if bg_number:
            self.fo_assert_text('BG number', bg_number)
        if beneficiary:
            self.fo_assert_text('Beneficiary', beneficiary)
        if beneficiary_address:
            self.fo_assert_text('Beneficiary address', beneficiary_address)
        if maturity_date:
            self.fo_assert_date('Maturity date', maturity_date)
        self.fo_write_text('Description', 'AUTO TEST')
        self.key_escape()
        if ifc_codes:
            self.add_fees(ifc_codes, values, total_fee)
        self.wait_loading()
        self.fo_click_checkbox('Caution!  There is no doubt that banks may be used as a means of Money Laundering/ Terrorist Financing/ Proliferation of Weapons of Mass Destruction.')
        # click 'Accept'
        self.click_button('Accept')
        # approve
        if approve_later=='Y':
            self.click_button('Later')
        if approve_on_form=='Y':
            self.fo_approve_in_popup(
                username=username,
                password=password,
                reason=reason
            )
        if list_error_message:
        # verify error
            self.assert_error_message()
            self.assert_list_error_message(list_error_message)
            print('Transaction failed!')
        else:
        # verify success
            self.assert_button_disable('Accept')
            self.switch_to_core_banking()
            self.assert_notification('Saved successfully!')
            self.close_voucher()
            if expected_posting:
                self.assert_posting_data(**expected_posting)
            transaction_references=self.fo_get_text('Transaction references')
            print(f'Transaction references TRD_SCL: {transaction_references}')
            trade_account_mask=self.fo_get_value_group('Account number')
            print(f'Account number: {trade_account_mask}')
            return transaction_references, trade_account_mask

    def trd_scl_view(self, transaction_references, account_number=None, sg_bg_amount=None, margin_rate=None, margin_amount=None, guarantee_amount=None, secured_amount=None, margin_method=None, margin_deposit_account=None, applicant=None, bg_number=None, beneficiary=None, beneficiary_address=None, maturity_date=None, description=None, expected_posting=None):
        self.transaction_view(transaction_references, '7758: SG - Close')
        # compare value
        if account_number:
            self.fo_assert_value_group('Account number', self.trade_account_number_mask(account_number))
        if sg_bg_amount:
            self.fo_assert_value('SG/BG amount', sg_bg_amount)
        if margin_rate:
            self.fo_assert_value('Margin rate', margin_rate)
        if margin_amount:
            self.fo_assert_value('Margin amount', margin_amount)
        if guarantee_amount:
            self.fo_assert_value('Guarantee amount', guarantee_amount)
        if secured_amount:
            self.fo_assert_value('Secured amount', secured_amount)
        if margin_method:
            self.fo_assert_select('Margin method', margin_method)
        if margin_deposit_account:
            self.fo_assert_value_group('Margin deposit account', margin_deposit_account)
        if applicant:
            self.fo_assert_text_group('Applicant', applicant)
        if bg_number:
            self.fo_assert_text('BG number', bg_number)
        if beneficiary:
            self.fo_assert_text('Beneficiary', beneficiary)
        if beneficiary_address:
            self.fo_assert_text('Beneficiary address', beneficiary_address)
        if maturity_date:
            self.fo_assert_date('Maturity date', maturity_date)
        if description:
            self.fo_assert_text('Description', description)
        if expected_posting:
            self.assert_posting_data(**expected_posting)
        trade_account_mask=self.fo_get_value_group('Account number')
        print(f'Account number: {trade_account_mask}')
        return transaction_references, trade_account_mask

# -------------------------- handle FO - MORTGAGE --------------------------

    # MTG_OPN: 4400: Open new collateral account
    def mtg_opn(self, customer_code, catalogue_code, collateral_asset_value, reference_number, evaluate_by, account_name=None, customer_type=None, catalogue_name=None, collateral_asset_type=None, collateral_asset_class=None, sercurity_paper_type=None, currency_code=None, collateral_rate=None, risk_allocation_rate=None, market_value=None, forced_sale_value=None, cc_contract=None, cc_amount=None, seq_number=None, name_of_title=None, house_no=None, plot_no=None, holding_no=None, ward_no=None, block_no=None, area_acre=None, street=None, township=None, division_city=None, location=None, legal_address=None, legal_local_address=None, expiry_date=None, policy_amount=None, company_issues_policy=None, policy_number=None, evaluate_method=None, evaluate_date=None, new_evaluate_date=None, insurance_name=None, insurance_expiry_date=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.open_fo('MTG_OPN', '4400')
        self.wait_for_button_available('Accept')
        self.assert_form_title('4400: Open new collateral account')
        # enter value
        if customer_type:
            self.fo_select('Customer type', customer_type)
        if customer_code:
            self.fo_write_group('Customer code', customer_code)
        if account_name:
            self.fo_write_text('Account name', account_name)
        if catalogue_code:
            self.fo_write('Catalogue code', catalogue_code)
        if catalogue_name:
            self.fo_assert_text('Catalogue name', catalogue_name)
        if collateral_asset_type:
            self.key_escape()
            self.fo_select('Collateral asset type', collateral_asset_type)
        if collateral_asset_class:
            self.key_escape()
            self.fo_select('Collateral asset class', collateral_asset_class)
        if sercurity_paper_type:
            self.key_escape()
            self.fo_select('Sercurity paper type', sercurity_paper_type)
        if currency_code:
            self.fo_assert_select('Currency code', currency_code)
        self.key_escape()
        if collateral_rate:
            self.fo_write_number_group('Collateral rate', str(collateral_rate).replace(',', ''))
            if self.fo_get_value_group('Collateral rate') != collateral_rate:
                self.fo_write_number_group('Collateral rate', str(collateral_rate).replace(',', ''))
        if risk_allocation_rate:
            self.fo_write_number('Risk allocation rate', str(risk_allocation_rate).replace(',', ''))
            if self.fo_get_value('Risk allocation rate') != risk_allocation_rate:
                self.fo_write_number('Risk allocation rate', str(risk_allocation_rate).replace(',', ''))
        if collateral_asset_value:
            self.fo_write_number('Collateral asset value', str(collateral_asset_value).replace(',', ''))
            if self.fo_get_value('Collateral asset value') != collateral_asset_value:
                self.fo_write_number('Collateral asset value', str(collateral_asset_value).replace(',', ''))
            self.fo_assert_value('Forced sale value', collateral_asset_value)
        if market_value:
            self.fo_write_number('Market value', str(market_value).replace(',', ''))
            if self.fo_get_value('Market value') != market_value:
                self.fo_write_number('Market value', str(market_value).replace(',', ''))
        if forced_sale_value:
            self.fo_write_number('Forced sale value', str(forced_sale_value).replace(',', ''))
            if self.fo_get_value('Forced sale value') != forced_sale_value:
                self.fo_write_number('Forced sale value', str(forced_sale_value).replace(',', ''))
        if cc_contract:
            self.fo_write_text('CC contract', cc_contract)
        if cc_amount:
            self.fo_write_number('CC amount', str(cc_amount).replace(',', ''))
            if self.fo_get_value('CC amount') != cc_amount:
                self.fo_write_number('CC amount', str(cc_amount).replace(',', ''))
        if seq_number:
            self.fo_write('Seq number', seq_number)
        if reference_number:
            self.fo_write_text('Reference number', reference_number)
        self.fo_click_collap('Other address')
        if name_of_title:
            self.fo_write_text_multi('Name of title', name_of_title)
        if house_no:
            self.fo_write_text_multi('House no', house_no)
        if plot_no:
            self.fo_write_text_multi('Plot no', plot_no)
        if holding_no:
            self.fo_write_text_multi('Holding no', holding_no)
        if ward_no:
            self.fo_write_text_multi('Ward no', ward_no)
        if block_no:
            self.fo_write_text_multi('Block no', block_no)
        if area_acre:
            self.fo_write_text_multi('Area (acre)', area_acre)
        if street:
            self.fo_write_text_multi('Street', street)
        if township:
            self.fo_write_text_multi('Township', township)
        if division_city:
            self.fo_write_text_multi('Division, city', division_city)
        if location:
            self.fo_select('Location', location)
        if legal_address:
            self.fo_write_text('Legal address', legal_address)
        if legal_local_address:
            self.fo_write_text('Legal local address', legal_local_address)
        if expiry_date:
            self.fo_write_date('Expiry date', expiry_date)
        if policy_amount:
            self.fo_write_number('Policy Amount', str(policy_amount).replace(',', ''))
            if self.fo_get_value('Policy Amount') != policy_amount:
                self.fo_write_number('Policy Amount', str(policy_amount).replace(',', ''))
        if company_issues_policy:
            self.fo_write_text('Company issues policy', company_issues_policy)
        if policy_number:
            self.fo_write_text('Policy Number', policy_number)
        if evaluate_by:
            self.fo_write_text('Evaluate by', evaluate_by)
        if evaluate_method:
            self.fo_select('Evaluate method', evaluate_method)
        if evaluate_date:
            self.fo_write_date('Evaluate date', evaluate_date)
        if new_evaluate_date:
            self.fo_write_date('New Evaluate date', new_evaluate_date)
        if insurance_name:
            self.fo_write_text('Insurance Name', insurance_name)
        if insurance_expiry_date:
            self.fo_write_text('Insurance Expiry Date', insurance_expiry_date)
        self.fo_write_text('Description', 'AUTO TEST')
        if ifc_codes:
            self.add_fees(ifc_codes, values, total_fee)
        self.wait_loading()
        self.fo_click_checkbox('Caution!  There is no doubt that banks may be used as a means of Money Laundering/ Terrorist Financing/ Proliferation of Weapons of Mass Destruction.')
        # click 'Accept'
        self.click_button('Accept')
        # approve
        if approve_later=='Y':
            self.click_button('Later')
        if approve_on_form=='Y':
            self.fo_approve_in_popup(
                username=username,
                password=password,
                reason=reason
            )
        if list_error_message:
        # verify error
            self.assert_error_message()
            self.assert_list_error_message(list_error_message)
            print('Transaction failed!')
        else:
        # verify success
            self.assert_button_disable('Accept')
            self.switch_to_core_banking()
            self.assert_notification('Saved successfully!')
            self.close_voucher()
            if expected_posting:
                self.assert_posting_data(**expected_posting)
            transaction_references=self.fo_get_text('Transaction references')
            print(f'Transaction references MTG_OPN: {transaction_references}')
            mortgage_account_mask=self.fo_get_value_group('Account number')
            print(f'Account number: {mortgage_account_mask}')
            return transaction_references, mortgage_account_mask

    def mtg_opn_view(self, transaction_references, account_number=None, account_name=None, customer_type=None, customer_code=None, catalogue_name=None, catalogue_code=None, collateral_asset_type=None, collateral_asset_class=None, sercurity_paper_type=None, currency_code=None, collateral_rate=None, risk_allocation_rate=None, collateral_asset_value=None, market_value=None, forced_sale_value=None, cc_contract=None, cc_amount=None, seq_number=None, reference_number=None, name_of_title=None, house_no=None, plot_no=None, holding_no=None, ward_no=None, block_no=None, area_acre=None, street=None, township=None, division_city=None, location=None, legal_address=None, legal_local_address=None, expiry_date=None, policy_amount=None, company_issues_policy=None, policy_number=None, evaluate_by=None, evaluate_method=None, evaluate_date=None, new_evaluate_date=None, insurance_name=None, insurance_expiry_date=None, description=None, expected_posting=None):
        self.transaction_view(transaction_references, '4400: Open new collateral account')
        # compare value
        if account_number:
            self.fo_assert_value_group('Account number', account_number)
        if account_name:
            self.fo_assert_text('Account name', account_name)
        if customer_type:
            self.fo_assert_select('Customer type', customer_type)
        if customer_code:
            self.fo_assert_value_group('Customer code', customer_code)
        if catalogue_name:
            self.fo_assert_text('Catalogue name', catalogue_name)
        if catalogue_code:
            self.fo_assert_value('Catalogue code', catalogue_code)
        if collateral_asset_type:
            self.fo_assert_select('Collateral asset type', collateral_asset_type)
        if collateral_asset_class:
            self.fo_assert_select('Collateral asset class', collateral_asset_class)
        if sercurity_paper_type:
            self.fo_assert_select('Sercurity paper type', sercurity_paper_type)
        if currency_code:
            self.fo_assert_select('Currency code', currency_code)
        if collateral_rate:
            self.fo_assert_value_group('Collateral rate', collateral_rate)
        if risk_allocation_rate:
            self.fo_assert_value('Risk allocation rate', risk_allocation_rate)
        if collateral_asset_value:
            self.fo_assert_value('Collateral asset value', collateral_asset_value)
        if market_value:
            self.fo_assert_value('Market value', market_value)
        if forced_sale_value:
            self.fo_assert_value('Forced sale value', forced_sale_value)
        if cc_contract:
            self.fo_assert_text('CC contract', cc_contract)
        if cc_amount:
            self.fo_assert_value('CC amount', cc_amount)
        if seq_number:
            self.fo_assert_value('Seq number', seq_number)
        if reference_number:
            self.fo_assert_text('Reference number', reference_number)
        # self.fo_click_collap('Other address')
        # if name_of_title:
        #     self.fo_assert_('Name of title', name_of_title)
        # if house_no:
        #     self.fo_assert_('House no', house_no)
        # if plot_no:
        #     self.fo_assert_('Plot no', plot_no)
        # if holding_no:
        #     self.fo_assert_('Holding no', holding_no)
        # if ward_no:
        #     self.fo_assert_('Ward no', ward_no)
        # if block_no:
        #     self.fo_assert_('Block no', block_no)
        # if area_acre:
        #     self.fo_assert_('Area (acre)', area_acre)
        # if street:
        #     self.fo_assert_('Street', street)
        # if township:
        #     self.fo_assert_('Township', township)
        # if division_city:
        #     self.fo_assert_('Division, city', division_city)
        if location:
            self.fo_assert_select('Location', location)
        if legal_address:
            self.fo_assert_text('Legal address', legal_address)
        if legal_local_address:
            self.fo_assert_text('Legal local address', legal_local_address)
        if expiry_date:
            self.fo_assert_date('Expiry date', expiry_date)
        if policy_amount:
            self.fo_assert_value('Policy Amount', policy_amount)
        if company_issues_policy:
            self.fo_assert_text('Company issues policy', company_issues_policy)
        if policy_number:
            self.fo_assert_text('Policy Number', policy_number)
        if evaluate_by:
            self.fo_assert_text('Evaluate by', evaluate_by)
        if evaluate_method:
            self.fo_assert_select('Evaluate method', evaluate_method)
        if evaluate_date:
            self.fo_assert_date('Evaluate date', evaluate_date)
        if new_evaluate_date:
            self.fo_assert_date('New Evaluate date', new_evaluate_date)
        if insurance_name:
            self.fo_assert_text('Insurance Name', insurance_name)
        if insurance_expiry_date:
            self.fo_assert_text('Insurance Expiry Date', insurance_expiry_date)
        if description:
            self.fo_assert_text('Description', description)
        if expected_posting:
            self.assert_posting_data(**expected_posting)
        mortgage_account_mask=self.fo_get_value_group('Account number')
        print(f'Account number: {mortgage_account_mask}')
        return transaction_references, mortgage_account_mask

    # MTG_APR: 4450: Approve collateral account
    def mtg_apr(self, account_number, account_holder_name=None, forced_sale_value=None, customer_code=None, customer_name=None, customer_address=None, home_address=None, office_address=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.open_fo('MTG_APR', '4450')
        self.wait_for_button_available('Accept')
        self.assert_form_title('4450: Approve collateral account')
        # enter value
        self.fo_write_group('Account number', account_number)
        self.wait_loading()
        if account_holder_name:
            self.fo_assert_text('Account holder name', account_holder_name)
        if forced_sale_value:
            self.fo_assert_value('Forced sale value', forced_sale_value)
        if customer_code:
            self.fo_write('Customer code', customer_code)
        if customer_name:
            self.fo_write_text('Customer name', customer_name)
        if customer_address:
            self.fo_write_text('Customer address', customer_address)
        self.fo_click_collap('Customer description')
        if home_address:
            self.fo_write_text_multi('Home', home_address)
        if office_address:
            self.fo_write_text_multi('Office', office_address)
        self.fo_write_text_group('Description', 'AUTO TEST')
        if ifc_codes:
            self.add_fees(ifc_codes, values, total_fee)
        self.wait_loading()
        # click 'Accept'
        self.click_button('Accept')
        # approve
        if approve_later=='Y':
            self.click_button('Later')
        if approve_on_form=='Y':
            self.fo_approve_in_popup(
                username=username,
                password=password,
                reason=reason
            )
        if list_error_message:
        # verify error
            self.assert_error_message()
            self.assert_list_error_message(list_error_message)
            print('Transaction failed!')
        else:
        # verify success
            self.assert_button_disable('Accept')
            self.switch_to_core_banking()
            self.assert_notification('Saved successfully!')
            self.close_voucher()
            if expected_posting:
                self.assert_posting_data(**expected_posting)
            transaction_references=self.fo_get_text('Transaction references')
            print(f'Transaction references MTG_APR: {transaction_references}')
            mortgage_account_mask=self.fo_get_value_group('Account number')
            print(f'Account number: {mortgage_account_mask}')
            return transaction_references, mortgage_account_mask

    def mtg_apr_view(self, transaction_references, account_number=None, account_holder_name=None, forced_sale_value=None, customer_code=None, customer_name=None, customer_address=None, home_address=None, office_address=None, description=None, expected_posting=None):
        self.transaction_view(transaction_references, '4450: Approve collateral account')
        # compare value
        if account_number:
            self.fo_assert_value_group('Account number', account_number)
        if account_holder_name:
            self.fo_assert_text('Account holder name', account_holder_name)
        if forced_sale_value:
            self.fo_assert_value('Forced sale value', forced_sale_value)
        if customer_code:
            self.fo_assert_value('Customer code', customer_code)
        if customer_name:
            self.fo_assert_text('Customer name', customer_name)
        if customer_address:
            self.fo_assert_text('Customer address', customer_address)
        self.fo_click_collap('Customer description')
        # if home_address:
        #     self.fo_assert_('Home', home_address)
        # if office_address:
        #     self.fo_assert_('Office', office_address)
        if description:
            self.fo_assert_text_group('Description', description)
        if expected_posting:
            self.assert_posting_data(**expected_posting)
        mortgage_account_mask=self.fo_get_value_group('Account number')
        print(f'Account number: {mortgage_account_mask}')
        return transaction_references, mortgage_account_mask

# -------------------------- handle BO - TRANSACTION JOURNAL --------------------------
    # FOF-Transaction Journal
    def transaction_search(self, transaction_references):
        # search f8
        self.close_all_form()
        self.open_transaction_journal()
        self.wait_for_button_available('Search')
        self.assert_form_title('FOF-Transaction Journal')
        self.simple_search_f8(transaction_references)
        self.wait_loading()
        self.assert_table_data('Tran Number', 1, transaction_references)

    def transaction_search_advanced(self, transaction_references):
        # search f8
        self.close_all_form()
        self.open_transaction_journal()
        self.assert_form_title('FOF-Transaction Journal')
        self.advanced_search_f8('Tran number', transaction_references, field_type='A')
        self.click_button_search_advanced_f8()
        self.wait_loading()
        self.assert_table_data('Tran Number', 1, transaction_references)

    def transaction_view(self, transaction_references, form_title=None, mode=F8Config.view_mode):
        # search f8
        if mode=='S':
            self.transaction_search_advanced(transaction_references)
        if mode=='N':
            self.transaction_search(transaction_references)
        #  view f8
        self.click_table_menu('View', 1)
        self.wait_loading()
        self.assert_notification('Get info successfully')
        self.wait_for_button_available('Accept')
        if form_title:
            self.assert_form_title(form_title)
        self.fo_assert_text('Transaction references', transaction_references)

    def transaction_reverse(self, transaction_references, username, password, reason=None, allow_reverse=None, list_error_message=None, mode=F8Config.view_mode):
        # search f8
        if mode=='S':
            self.transaction_search_advanced(transaction_references)
        if mode=='N':
            self.transaction_search(transaction_references)
        self.click_table_menu('Delete', 1)
        self.approve_in_popup(
            username=username,
            password=password,
            reason=reason
        )
        self.wait_loading()
        # reversed transaction: N: not allow
        if allow_reverse=='N':
            self.assert_notification('Deleted error')
            self.assert_error_message()
            if list_error_message:
                self.assert_list_error_message(list_error_message)
            # search and compare status
            if mode=='S':
                self.transaction_search_advanced(transaction_references)
            if mode=='N':
                self.transaction_search(transaction_references)
            self.assert_status_table_data('Status', 1, 'Completed')
            print(f'Transaction references is NOT reversed: {transaction_references}')
        else:
            self.assert_notification('Deleted successfully')
            # search and compare status
            if mode=='S':
                self.transaction_search_advanced(transaction_references)
            if mode=='N':
                self.transaction_search(transaction_references)
            self.assert_status_table_data('Status', 1, 'Reversed')
            print(f'Transaction references has been reversed: {transaction_references}')

    def transaction_approve(self, transaction_references, username, password, reason=None, allow_approve=None, list_error_message=None, mode=F8Config.view_mode):
        # search f8
        if mode=='S':
            self.transaction_search_advanced(transaction_references)
        if mode=='N':
            self.transaction_search(transaction_references)
        self.click_table_menu('Approve', 1)
        self.approve_in_popup(
            username=username,
            password=password,
            reason=reason
        )
        self.wait_loading()
        # approve transaction: N: not allow
        if allow_approve=='N':
            self.assert_notification('Approve error')
            self.assert_error_message()
            if list_error_message:
                self.assert_list_error_message(list_error_message)
            # search and compare status
            if mode=='S':
                self.transaction_search_advanced(transaction_references)
            if mode=='N':
                self.transaction_search(transaction_references)
            self.assert_status_table_data('Status', 1, 'Pending to approve')
        else:
            self.assert_notification('Approve successfully')
            # search and compare status
            if mode=='S':
                self.transaction_search_advanced(transaction_references)
            if mode=='N':
                self.transaction_search(transaction_references)
            self.assert_status_table_data('Status', 1, 'Completed')

    def transaction_reject(self, transaction_references, username, password, reason=None, mode=F8Config.view_mode):
        # search f8
        if mode=='S':
            self.transaction_search_advanced(transaction_references)
        if mode=='N':
            self.transaction_search(transaction_references)
        self.click_table_menu('Reject', 1)
        self.approve_in_popup(
            username=username,
            password=password,
            reason=reason
        )
        self.wait_loading()
        self.assert_notification('Reject successfully')
        # search and compare status
        if mode=='S':
            self.transaction_search_advanced(transaction_references)
        if mode=='N':
            self.transaction_search(transaction_references)
        self.assert_status_table_data('Status', 1, 'Rejected')
        print(f'Transaction references has been rejected: {transaction_references}')

# # -------------------------- handle FO - FX TRANSACTION --------------------------
    def act_act(self, accounting_type_debit=None, account_number_debit=None, account_name_debit=None, currency_debit=None, type_debit=None, accounting_type_credit=None, account_number_credit=None, account_name_credit=None, currency_credit=None, type_credit=None, enter_side=None, market_dr_rate=None, cross_rate=None, market_cr_rate=None, debit_amount=None, reverse_rate=None, credit_amount=None, fee_amount=None, receive_amount=None, customer_type=None, customer_code=None, full_name=None, paper_type=None, paper_number=None, telephone=None, address=None, nationality=None, description=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.click_menu('Front Office', 'FX Transaction')
        self.wait_for_button_available('Accept')
        self.assert_form_title('FOF-FX Transaction')
        # enter value
        if accounting_type_debit is None or accounting_type_debit == '':
            accounting_type_debit = 'Accounting'
        if accounting_type_debit:
            self.fo_select_border('Debit', 'Accounting Type', accounting_type_debit)
        if account_number_debit:
            account_number_debit_value = str(account_number_debit).replace('-', '')
            self.fo_write_border('Debit', 'Account number', account_number_debit_value)
            self.wait_loading()
        if account_name_debit:
            self.fo_assert_text_border('Debit', 'Account name debit', account_name_debit)
        if currency_debit:
            self.fo_assert_value_border('Debit', 'Currency', currency_debit)
        if type_debit:
            self.fo_select_border('Debit', 'Type', type_debit)
        if accounting_type_credit is None or accounting_type_credit == '':
            accounting_type_credit = 'Accounting'
        if accounting_type_credit:
            self.fo_select_border('Credit', 'Accounting Type', accounting_type_credit)
        if account_number_credit:
            account_number_credit_value = str(account_number_credit).replace('-', '')
            self.fo_write_border('Credit', 'Account number', account_number_credit_value)
            self.wait_loading()
        if account_name_credit:
            self.fo_assert_text_border('Credit', 'Account name credit', account_name_credit)
        if currency_credit:
            self.fo_assert_value_border('Credit', 'Currency', currency_credit)
        if type_credit:
            self.fo_select_border('Credit', 'Type', type_credit)
        if customer_type:
            self.fo_select_border('Customer Information', 'Customer type', customer_type)
        if customer_code:
            self.fo_write_border('Customer Information', 'Customer code', customer_code)
        if full_name:
            self.fo_write_text_border('Customer Information', 'Full name', full_name)
        if paper_type:
            self.fo_select_border('Customer Information', 'Paper type', paper_type)
        if paper_number:
            self.fo_write_text_border('Customer Information', 'Paper number', paper_number)
        if telephone:
            self.fo_write_text_border('Customer Information', 'Telephone', telephone)
        if address:
            self.fo_write_text_border('Customer Information', 'Address', address)
        if nationality:
            self.fo_select_border('Customer Information', 'Nationality', nationality)
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_write_text_border('Customer Information', 'Description', description)
        if enter_side=='D':
            if debit_amount:
                self.fo_write_number_border('Rate', 'Debit Amount', debit_amount)
            if market_dr_rate:
                self.fo_assert_value_border('Rate', 'Market DR Rate', market_dr_rate)
            if cross_rate:
                self.fo_assert_value_border('Rate', 'Cross Rate', cross_rate)
            if market_cr_rate:
                self.fo_assert_value_border('Rate', 'Market CR Rate', market_cr_rate)
            if reverse_rate:
                self.fo_assert_value_border('Rate', 'Reverse Rate', reverse_rate)
            if credit_amount:
                self.fo_assert_value_border('Rate', 'Credit Amount', credit_amount)
        if enter_side=='C':
            if credit_amount:
                self.fo_write_number_border('Rate', 'Credit Amount', credit_amount)
            if debit_amount:
                self.fo_assert_value_border('Rate', 'Debit Amount', debit_amount)
            if market_dr_rate:
                self.fo_assert_value_border('Rate', 'Market DR Rate', market_dr_rate)
            if cross_rate:
                self.fo_assert_value_border('Rate', 'Cross Rate', cross_rate)
            if market_cr_rate:
                self.fo_assert_value_border('Rate', 'Market CR Rate', market_cr_rate)
            if reverse_rate:
                self.fo_assert_value_border('Rate', 'Reverse Rate', reverse_rate)
        if credit_amount:
            self.fo_assert_value_border('Rate', 'Receive Amount', credit_amount)
        self.fo_assert_value_border('Rate', 'Fee Amount', '0.00')
        if ifc_codes:
            self.add_fees(ifc_codes, values, total_fee)
            self.wait_loading()
            if market_dr_rate:
                self.fo_assert_value_border('Rate', 'Market DR Rate', market_dr_rate)
            if cross_rate:
                self.fo_assert_value_border('Rate', 'Cross Rate', cross_rate)
            if market_cr_rate:
                self.fo_assert_value_border('Rate', 'Market CR Rate', market_cr_rate)
            if debit_amount:
                self.fo_assert_value_border('Rate', 'Debit Amount', debit_amount)
            if reverse_rate:
                self.fo_assert_value_border('Rate', 'Reverse Rate', reverse_rate)
            if credit_amount:
                self.fo_assert_value_border('Rate', 'Credit Amount', credit_amount)
            if fee_amount:
                self.fo_assert_value_border('Rate', 'Fee Amount', fee_amount)
            if receive_amount:
                self.fo_assert_value_border('Rate', 'Receive Amount', receive_amount)
        self.wait_loading()
        self.fo_click_checkbox('Caution!  There is no doubt that banks may be used as a means of Money Laundering/ Terrorist Financing/ Proliferation of Weapons of Mass Destruction.')
        self.wait_loading()
        # click 'Accept'
        self.click_button('Accept')
        # approve
        if approve_later=='Y':
            self.click_button('Later')
        if approve_on_form=='Y':
            self.fo_approve_in_popup(
                username=username,
                password=password,
                reason=reason
            )
        if list_error_message:
        # verify error
            self.assert_error_message()
            self.assert_list_error_message(list_error_message)
            print('Transaction failed!')
        else:
        # verify success
            self.assert_button_disable('Accept')
            self.switch_to_core_banking()
            self.assert_notification('Saved successfully!')
            self.close_voucher()
            if expected_posting:
                self.assert_posting_data(**expected_posting)
            transaction_references=self.fo_get_text('Transaction references')
            print(f'Transaction references ACT_ACT: {transaction_references}')
            return transaction_references

    def act_act_view(self, transaction_references, accounting_type_debit=None, accounting_type_credit=None, account_number_debit=None, account_name_debit=None, currency_debit=None, type_debit=None, account_number_credit=None, account_name_credit=None, currency_credit=None, type_credit=None, market_dr_rate=None, cross_rate=None, market_cr_rate=None, debit_amount=None, reverse_rate=None, credit_amount=None, fee_amount=None, receive_amount=None, customer_type=None, customer_code=None, full_name=None, paper_type=None, paper_number=None, telephone=None, address=None, nationality=None, description=None, ifc_codes=None, values=None, total_fee=None, expected_posting=None):
        self.transaction_view(transaction_references, 'FOF-FX Transaction')
        # compare value
        if expected_posting:
            self.assert_posting_data(**expected_posting)
        return transaction_references

    def act_dpt(self, accounting_type_debit=None, account_number_debit=None, account_name_debit=None, currency_debit=None, type_debit=None, accounting_type_credit=None, account_number_credit=None, account_name_credit=None, currency_credit=None, type_credit=None, enter_side=None, market_dr_rate=None, cross_rate=None, market_cr_rate=None, debit_amount=None, reverse_rate=None, credit_amount=None, fee_amount=None, receive_amount=None, customer_type=None, customer_code=None, full_name=None, paper_type=None, paper_number=None, telephone=None, address=None, nationality=None, description=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.click_menu('Front Office', 'FX Transaction')
        self.wait_for_button_available('Accept')
        self.assert_form_title('FOF-FX Transaction')
        # enter value
        if accounting_type_debit is None or accounting_type_debit == '':
            accounting_type_debit = 'Accounting'
        if accounting_type_debit:
            self.fo_select_border('Debit', 'Accounting Type', accounting_type_debit)
        if account_number_debit:
            account_number_debit_value = str(account_number_debit).replace('-', '')
            self.fo_write_border('Debit', 'Account number', account_number_debit_value)
            self.wait_loading()
        if account_name_debit:
            self.fo_assert_text_border('Debit', 'Account name debit', account_name_debit)
        if currency_debit:
            self.fo_assert_value_border('Debit', 'Currency', currency_debit)
        if type_debit:
            self.fo_select_border('Debit', 'Type', type_debit)
        if accounting_type_credit is None or accounting_type_credit == '':
            accounting_type_credit = 'Deposit'
        if accounting_type_credit:
            self.fo_select_border('Credit', 'Accounting Type', accounting_type_credit)
        if account_number_credit:
            account_number_credit_value = str(account_number_credit).replace('-', '')
            self.fo_write_border('Credit', 'Account numer', account_number_credit_value)
            self.wait_loading()
        if account_name_credit:
            self.fo_assert_text_border('Credit', 'Account name credit', account_name_credit)
        if currency_credit:
            self.fo_assert_value_border('Credit', 'Currency', currency_credit)
        if type_credit:
            self.fo_select_border('Credit', 'Type', type_credit)
        if customer_type:
            self.fo_select_border('Customer Information', 'Customer type', customer_type)
        if customer_code:
            self.fo_write_border('Customer Information', 'Customer code', customer_code)
        if full_name:
            self.fo_write_text_border('Customer Information', 'Full name', full_name)
        if paper_type:
            self.fo_select_border('Customer Information', 'Paper type', paper_type)
        if paper_number:
            self.fo_write_text_border('Customer Information', 'Paper number', paper_number)
        if telephone:
            self.fo_write_text_border('Customer Information', 'Telephone', telephone)
        if address:
            self.fo_write_text_border('Customer Information', 'Address', address)
        if nationality:
            self.fo_select_border('Customer Information', 'Nationality', nationality)
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_write_text_border('Customer Information', 'Description', description)
        if enter_side=='D':
            if debit_amount:
                self.fo_write_number_border('Rate', 'Debit Amount', debit_amount)
            if market_dr_rate:
                self.fo_assert_value_border('Rate', 'Market DR Rate', market_dr_rate)
            if cross_rate:
                self.fo_assert_value_border('Rate', 'Cross Rate', cross_rate)
            if market_cr_rate:
                self.fo_assert_value_border('Rate', 'Market CR Rate', market_cr_rate)
            if reverse_rate:
                self.fo_assert_value_border('Rate', 'Reverse Rate', reverse_rate)
            if credit_amount:
                self.fo_assert_value_border('Rate', 'Credit Amount', credit_amount)
        if enter_side=='C':
            if credit_amount:
                self.fo_write_number_border('Rate', 'Credit Amount', credit_amount)
            if debit_amount:
                self.fo_assert_value_border('Rate', 'Debit Amount', debit_amount)
            if market_dr_rate:
                self.fo_assert_value_border('Rate', 'Market DR Rate', market_dr_rate)
            if cross_rate:
                self.fo_assert_value_border('Rate', 'Cross Rate', cross_rate)
            if market_cr_rate:
                self.fo_assert_value_border('Rate', 'Market CR Rate', market_cr_rate)
            if reverse_rate:
                self.fo_assert_value_border('Rate', 'Reverse Rate', reverse_rate)
        if credit_amount:
            self.fo_assert_value_border('Rate', 'Receive Amount', credit_amount)
        self.fo_assert_value_border('Rate', 'Fee Amount', '0.00')
        if ifc_codes:
            self.add_fees(ifc_codes, values, total_fee)
            self.wait_loading()
            if market_dr_rate:
                self.fo_assert_value_border('Rate', 'Market DR Rate', market_dr_rate)
            if cross_rate:
                self.fo_assert_value_border('Rate', 'Cross Rate', cross_rate)
            if market_cr_rate:
                self.fo_assert_value_border('Rate', 'Market CR Rate', market_cr_rate)
            if debit_amount:
                self.fo_assert_value_border('Rate', 'Debit Amount', debit_amount)
            if reverse_rate:
                self.fo_assert_value_border('Rate', 'Reverse Rate', reverse_rate)
            if credit_amount:
                self.fo_assert_value_border('Rate', 'Credit Amount', credit_amount)
            if fee_amount:
                self.fo_assert_value_border('Rate', 'Fee Amount', fee_amount)
            if receive_amount:
                self.fo_assert_value_border('Rate', 'Receive Amount', receive_amount)
        self.wait_loading()
        self.fo_click_checkbox('Caution!  There is no doubt that banks may be used as a means of Money Laundering/ Terrorist Financing/ Proliferation of Weapons of Mass Destruction.')
        self.wait_loading()
        # click 'Accept'
        self.click_button('Accept')
        # approve
        if approve_later=='Y':
            self.click_button('Later')
        if approve_on_form=='Y':
            self.fo_approve_in_popup(
                username=username,
                password=password,
                reason=reason
            )
        if list_error_message:
        # verify error
            self.assert_error_message()
            self.assert_list_error_message(list_error_message)
            print('Transaction failed!')
        else:
        # verify success
            self.assert_button_disable('Accept')
            self.switch_to_core_banking()
            self.assert_notification('Saved successfully!')
            self.close_voucher()
            if expected_posting:
                self.assert_posting_data(**expected_posting)
            transaction_references=self.fo_get_text('Transaction references')
            print(f'Transaction references ACT_DPT: {transaction_references}')
            return transaction_references

    def act_dpt_view(self, transaction_references, accounting_type_debit=None, account_number_debit=None, account_name_debit=None, currency_debit=None, type_debit=None, accounting_type_credit=None, account_number_credit=None, account_name_credit=None, currency_credit=None, type_credit=None, enter_side=None, market_dr_rate=None, cross_rate=None, market_cr_rate=None, debit_amount=None, reverse_rate=None, credit_amount=None, fee_amount=None, receive_amount=None, customer_type=None, customer_code=None, full_name=None, paper_type=None, paper_number=None, telephone=None, address=None, nationality=None, description=None, ifc_codes=None, values=None, total_fee=None, expected_posting=None):
        self.transaction_view(transaction_references, 'FOF-FX Transaction')
        # compare value
        if expected_posting:
            self.assert_posting_data(**expected_posting)
        return transaction_references

    def act_csh(self, accounting_type_debit=None, account_number_debit=None, account_name_debit=None, currency_debit=None, type_debit=None, accounting_type_credit=None, account_name_credit=None, currency_credit=None, type_credit=None, enter_side=None, market_dr_rate=None, cross_rate=None, market_cr_rate=None, debit_amount=None, reverse_rate=None, credit_amount=None, fee_amount=None, receive_amount=None, customer_type=None, customer_code=None, full_name=None, paper_type=None, paper_number=None, telephone=None, address=None, nationality=None, description=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.click_menu('Front Office', 'FX Transaction')
        self.wait_for_button_available('Accept')
        self.assert_form_title('FOF-FX Transaction')
        # enter value
        if accounting_type_debit is None or accounting_type_debit == '':
            accounting_type_debit = 'Accounting'
        if accounting_type_debit:
            self.fo_select_border('Debit', 'Accounting Type', accounting_type_debit)
        if account_number_debit:
            account_number_debit_value = str(account_number_debit).replace('-', '')
            self.fo_write_border('Debit', 'Account number', account_number_debit_value)
            self.wait_loading()
        if account_name_debit:
            self.fo_assert_text_border('Debit', 'Account name debit', account_name_debit)
        if currency_debit:
            self.fo_assert_value_border('Debit', 'Currency', currency_debit)
        if type_debit:
            self.fo_select_border('Debit', 'Type', type_debit)
        if accounting_type_credit is None or accounting_type_credit == '':
            accounting_type_credit = 'Cash'
        if accounting_type_credit:
            self.fo_select_border('Credit', 'Accounting Type', accounting_type_credit)
        if account_name_credit:
            self.fo_write_text_border('Credit', 'Account name credit', account_name_credit)
        if currency_credit:
            self.fo_select_border('Credit', 'Currency', currency_credit)
        if type_credit:
            self.fo_select_border('Credit', 'Type', type_credit)
        if customer_type:
            self.fo_select_border('Customer Information', 'Customer type', customer_type)
        if customer_code:
            self.fo_write_border('Customer Information', 'Customer code', customer_code)
        if full_name:
            self.fo_write_text_border('Customer Information', 'Full name', full_name)
        if paper_type:
            self.fo_select_border('Customer Information', 'Paper type', paper_type)
        if paper_number:
            self.fo_write_text_border('Customer Information', 'Paper number', paper_number)
        if telephone:
            self.fo_write_text_border('Customer Information', 'Telephone', telephone)
        if address:
            self.fo_write_text_border('Customer Information', 'Address', address)
        if nationality:
            self.fo_select_border('Customer Information', 'Nationality', nationality)
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_write_text_border('Customer Information', 'Description', description)
        if enter_side=='D':
            if debit_amount:
                self.fo_write_number_border('Rate', 'Debit Amount', debit_amount)
            if market_dr_rate:
                self.fo_assert_value_border('Rate', 'Market DR Rate', market_dr_rate)
            if cross_rate:
                self.fo_assert_value_border('Rate', 'Cross Rate', cross_rate)
            if market_cr_rate:
                self.fo_assert_value_border('Rate', 'Market CR Rate', market_cr_rate)
            if reverse_rate:
                self.fo_assert_value_border('Rate', 'Reverse Rate', reverse_rate)
            if credit_amount:
                self.fo_assert_value_border('Rate', 'Credit Amount', credit_amount)
        if enter_side=='C':
            if credit_amount:
                self.fo_write_number_border('Rate', 'Credit Amount', credit_amount)
            if debit_amount:
                self.fo_assert_value_border('Rate', 'Debit Amount', debit_amount)
            if market_dr_rate:
                self.fo_assert_value_border('Rate', 'Market DR Rate', market_dr_rate)
            if cross_rate:
                self.fo_assert_value_border('Rate', 'Cross Rate', cross_rate)
            if market_cr_rate:
                self.fo_assert_value_border('Rate', 'Market CR Rate', market_cr_rate)
            if reverse_rate:
                self.fo_assert_value_border('Rate', 'Reverse Rate', reverse_rate)
        if credit_amount:
            self.fo_assert_value_border('Rate', 'Receive Amount', credit_amount)
        self.fo_assert_value_border('Rate', 'Fee Amount', '0.00')
        if ifc_codes:
            self.add_fees(ifc_codes, values, total_fee)
            self.wait_loading()
            if market_dr_rate:
                self.fo_assert_value_border('Rate', 'Market DR Rate', market_dr_rate)
            if cross_rate:
                self.fo_assert_value_border('Rate', 'Cross Rate', cross_rate)
            if market_cr_rate:
                self.fo_assert_value_border('Rate', 'Market CR Rate', market_cr_rate)
            if debit_amount:
                self.fo_assert_value_border('Rate', 'Debit Amount', debit_amount)
            if reverse_rate:
                self.fo_assert_value_border('Rate', 'Reverse Rate', reverse_rate)
            if credit_amount:
                self.fo_assert_value_border('Rate', 'Credit Amount', credit_amount)
            if fee_amount:
                self.fo_assert_value_border('Rate', 'Fee Amount', fee_amount)
            if receive_amount:
                self.fo_assert_value_border('Rate', 'Receive Amount', receive_amount)
        self.wait_loading()
        self.fo_click_checkbox('Caution!  There is no doubt that banks may be used as a means of Money Laundering/ Terrorist Financing/ Proliferation of Weapons of Mass Destruction.')
        self.wait_loading()
        # click 'Accept'
        self.click_button('Accept')
        # approve
        if approve_later=='Y':
            self.click_button('Later')
        if approve_on_form=='Y':
            self.fo_approve_in_popup(
                username=username,
                password=password,
                reason=reason
            )
        if list_error_message:
        # verify error
            self.assert_error_message()
            self.assert_list_error_message(list_error_message)
            print('Transaction failed!')
        else:
        # verify success
            self.assert_button_disable('Accept')
            self.switch_to_core_banking()
            self.assert_notification('Saved successfully!')
            self.close_voucher()
            if expected_posting:
                self.assert_posting_data(**expected_posting)
            transaction_references=self.fo_get_text('Transaction references')
            print(f'Transaction references ACT_CSH: {transaction_references}')
            return transaction_references

    def act_csh_view(self, transaction_references, accounting_type_debit=None, account_number_debit=None, account_name_debit=None, currency_debit=None, type_debit=None, accounting_type_credit=None, account_name_credit=None, currency_credit=None, type_credit=None, enter_side=None, market_dr_rate=None, cross_rate=None, market_cr_rate=None, debit_amount=None, reverse_rate=None, credit_amount=None, fee_amount=None, receive_amount=None, customer_type=None, customer_code=None, full_name=None, paper_type=None, paper_number=None, telephone=None, address=None, nationality=None, description=None, ifc_codes=None, values=None, total_fee=None, expected_posting=None):
        self.transaction_view(transaction_references, 'FOF-FX Transaction')
        # compare value
        if expected_posting:
            self.assert_posting_data(**expected_posting)
        return transaction_references

    def csh_csh(self, accounting_type_debit=None, account_name_debit=None, currency_debit=None, type_debit=None, accounting_type_credit=None, account_name_credit=None, currency_credit=None, type_credit=None, enter_side=None, market_dr_rate=None, cross_rate=None, market_cr_rate=None, debit_amount=None, reverse_rate=None, credit_amount=None, fee_amount=None, receive_amount=None, customer_type=None, customer_code=None, full_name=None, paper_type=None, paper_number=None, telephone=None, address=None, nationality=None, description=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.click_menu('Front Office', 'FX Transaction')
        self.wait_for_button_available('Accept')
        self.assert_form_title('FOF-FX Transaction')
        # enter value
        if accounting_type_debit is None or accounting_type_debit == '':
            accounting_type_debit = 'Cash'
        if accounting_type_debit:
            self.fo_select_border('Debit', 'Accounting Type', accounting_type_debit)
        if account_name_debit:
            self.fo_write_text_border('Debit', 'Account name debit', account_name_debit)
        if currency_debit:
            self.fo_select_border('Debit', 'Currency', currency_debit)
        if type_debit:
            self.fo_select_border('Debit', 'Type', type_debit)
        if accounting_type_credit is None or accounting_type_credit == '':
            accounting_type_credit = 'Cash'
        if accounting_type_credit:
            self.fo_select_border('Credit', 'Accounting Type', accounting_type_credit)
        if account_name_credit:
            self.fo_write_text_border('Credit', 'Account name credit', account_name_credit)
        if currency_credit:
            self.fo_assert_value_border('Credit', 'Currency', currency_credit)
        if type_credit:
            self.fo_select_border('Credit', 'Type', type_credit)
        if customer_type:
            self.fo_select_border('Customer Information', 'Customer type', customer_type)
        if customer_code:
            self.fo_write_border('Customer Information', 'Customer code', customer_code)
        if full_name:
            self.fo_write_text_border('Customer Information', 'Full name', full_name)
        if paper_type:
            self.fo_select_border('Customer Information', 'Paper type', paper_type)
        if paper_number:
            self.fo_write_text_border('Customer Information', 'Paper number', paper_number)
        if telephone:
            self.fo_write_text_border('Customer Information', 'Telephone', telephone)
        if address:
            self.fo_write_text_border('Customer Information', 'Address', address)
        if nationality:
            self.fo_select_border('Customer Information', 'Nationality', nationality)
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_write_text_border('Customer Information', 'Description', description)
        if enter_side=='D':
            if debit_amount:
                self.fo_write_number_border('Rate', 'Debit Amount', debit_amount)
            if market_dr_rate:
                self.fo_assert_value_border('Rate', 'Market DR Rate', market_dr_rate)
            if cross_rate:
                self.fo_assert_value_border('Rate', 'Cross Rate', cross_rate)
            if market_cr_rate:
                self.fo_assert_value_border('Rate', 'Market CR Rate', market_cr_rate)
            if reverse_rate:
                self.fo_assert_value_border('Rate', 'Reverse Rate', reverse_rate)
            if credit_amount:
                self.fo_assert_value_border('Rate', 'Credit Amount', credit_amount)
        if enter_side=='C':
            if credit_amount:
                self.fo_write_number_border('Rate', 'Credit Amount', credit_amount)
            if debit_amount:
                self.fo_assert_value_border('Rate', 'Debit Amount', debit_amount)
            if market_dr_rate:
                self.fo_assert_value_border('Rate', 'Market DR Rate', market_dr_rate)
            if cross_rate:
                self.fo_assert_value_border('Rate', 'Cross Rate', cross_rate)
            if market_cr_rate:
                self.fo_assert_value_border('Rate', 'Market CR Rate', market_cr_rate)
            if reverse_rate:
                self.fo_assert_value_border('Rate', 'Reverse Rate', reverse_rate)
        if credit_amount:
            self.fo_assert_value_border('Rate', 'Receive Amount', credit_amount)
        self.fo_assert_value_border('Rate', 'Fee Amount', '0.00')
        if ifc_codes:
            self.add_fees(ifc_codes, values, total_fee)
            self.wait_loading()
            if market_dr_rate:
                self.fo_assert_value_border('Rate', 'Market DR Rate', market_dr_rate)
            if cross_rate:
                self.fo_assert_value_border('Rate', 'Cross Rate', cross_rate)
            if market_cr_rate:
                self.fo_assert_value_border('Rate', 'Market CR Rate', market_cr_rate)
            if debit_amount:
                self.fo_assert_value_border('Rate', 'Debit Amount', debit_amount)
            if reverse_rate:
                self.fo_assert_value_border('Rate', 'Reverse Rate', reverse_rate)
            if credit_amount:
                self.fo_assert_value_border('Rate', 'Credit Amount', credit_amount)
            if fee_amount:
                self.fo_assert_value_border('Rate', 'Fee Amount', fee_amount)
            if receive_amount:
                self.fo_assert_value_border('Rate', 'Receive Amount', receive_amount)
        self.wait_loading()
        self.fo_click_checkbox('Caution!  There is no doubt that banks may be used as a means of Money Laundering/ Terrorist Financing/ Proliferation of Weapons of Mass Destruction.')
        self.wait_loading()
        # click 'Accept'
        self.click_button('Accept')
        # approve
        if approve_later=='Y':
            self.click_button('Later')
        if approve_on_form=='Y':
            self.fo_approve_in_popup(
                username=username,
                password=password,
                reason=reason
            )
        if list_error_message:
        # verify error
            self.assert_error_message()
            self.assert_list_error_message(list_error_message)
            print('Transaction failed!')
        else:
        # verify success
            self.assert_button_disable('Accept')
            self.switch_to_core_banking()
            self.assert_notification('Saved successfully!')
            self.close_voucher()
            if expected_posting:
                self.assert_posting_data(**expected_posting)
            transaction_references=self.fo_get_text('Transaction references')
            print(f'Transaction references CSH_CSH: {transaction_references}')
            return transaction_references

    def csh_csh_view(self, transaction_references, accounting_type_debit=None, accounting_type_credit=None, account_number_debit=None, account_name_debit=None, currency_debit=None, type_debit=None, account_number_credit=None, account_name_credit=None, currency_credit=None, type_credit=None, market_dr_rate=None, cross_rate=None, market_cr_rate=None, debit_amount=None, reverse_rate=None, credit_amount=None, fee_amount=None, receive_amount=None, customer_type=None, customer_code=None, full_name=None, paper_type=None, paper_number=None, telephone=None, address=None, nationality=None, description=None, ifc_codes=None, values=None, total_fee=None, expected_posting=None):
        self.transaction_view(transaction_references, 'FOF-FX Transaction')
        # compare value
        if expected_posting:
            self.assert_posting_data(**expected_posting)
        return transaction_references

    def csh_act(self, accounting_type_debit=None, account_name_debit=None, currency_debit=None, type_debit=None, accounting_type_credit=None, account_number_credit=None, account_name_credit=None, currency_credit=None, type_credit=None, enter_side=None, market_dr_rate=None, cross_rate=None, market_cr_rate=None, debit_amount=None, reverse_rate=None, credit_amount=None, fee_amount=None, receive_amount=None, customer_type=None, customer_code=None, full_name=None, paper_type=None, paper_number=None, telephone=None, address=None, nationality=None, description=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.click_menu('Front Office', 'FX Transaction')
        self.wait_for_button_available('Accept')
        self.assert_form_title('FOF-FX Transaction')
        # enter value
        if accounting_type_debit is None or accounting_type_debit == '':
            accounting_type_debit = 'Cash'
        if accounting_type_debit:
            self.fo_select_border('Debit', 'Accounting Type', accounting_type_debit)
        if account_name_debit:
            self.fo_write_text_border('Debit', 'Account name debit', account_name_debit)
        if currency_debit:
            self.fo_select_border('Debit', 'Currency', currency_debit)
        if type_debit:
            self.fo_select_border('Debit', 'Type', type_debit)
        if accounting_type_credit is None or accounting_type_credit == '':
            accounting_type_credit = 'Accounting'
        if accounting_type_credit:
            self.fo_select_border('Credit', 'Accounting Type', accounting_type_credit)
        if account_number_credit:
            account_number_credit_value = str(account_number_credit).replace('-', '')
            self.fo_write_border('Credit', 'Account number', account_number_credit_value)
            self.wait_loading()
        if account_name_credit:
            self.fo_assert_text_border('Credit', 'Account name credit', account_name_credit)
        if currency_credit:
            self.fo_assert_value_border('Credit', 'Currency', currency_credit)
        if type_credit:
            self.fo_select_border('Credit', 'Type', type_credit)
        if customer_type:
            self.fo_select_border('Customer Information', 'Customer type', customer_type)
        if customer_code:
            self.fo_write_border('Customer Information', 'Customer code', customer_code)
        if full_name:
            self.fo_write_text_border('Customer Information', 'Full name', full_name)
        if paper_type:
            self.fo_select_border('Customer Information', 'Paper type', paper_type)
        if paper_number:
            self.fo_write_text_border('Customer Information', 'Paper number', paper_number)
        if telephone:
            self.fo_write_text_border('Customer Information', 'Telephone', telephone)
        if address:
            self.fo_write_text_border('Customer Information', 'Address', address)
        if nationality:
            self.fo_select_border('Customer Information', 'Nationality', nationality)
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_write_text_border('Customer Information', 'Description', description)
        if enter_side=='D':
            if debit_amount:
                self.fo_write_number_border('Rate', 'Debit Amount', debit_amount)
            if market_dr_rate:
                self.fo_assert_value_border('Rate', 'Market DR Rate', market_dr_rate)
            if cross_rate:
                self.fo_assert_value_border('Rate', 'Cross Rate', cross_rate)
            if market_cr_rate:
                self.fo_assert_value_border('Rate', 'Market CR Rate', market_cr_rate)
            if reverse_rate:
                self.fo_assert_value_border('Rate', 'Reverse Rate', reverse_rate)
            if credit_amount:
                self.fo_assert_value_border('Rate', 'Credit Amount', credit_amount)
        if enter_side=='C':
            if credit_amount:
                self.fo_write_number_border('Rate', 'Credit Amount', credit_amount)
            if debit_amount:
                self.fo_assert_value_border('Rate', 'Debit Amount', debit_amount)
            if market_dr_rate:
                self.fo_assert_value_border('Rate', 'Market DR Rate', market_dr_rate)
            if cross_rate:
                self.fo_assert_value_border('Rate', 'Cross Rate', cross_rate)
            if market_cr_rate:
                self.fo_assert_value_border('Rate', 'Market CR Rate', market_cr_rate)
            if reverse_rate:
                self.fo_assert_value_border('Rate', 'Reverse Rate', reverse_rate)
        if credit_amount:
            self.fo_assert_value_border('Rate', 'Receive Amount', credit_amount)
        self.fo_assert_value_border('Rate', 'Fee Amount', '0.00')
        if ifc_codes:
            self.add_fees(ifc_codes, values, total_fee)
            self.wait_loading()
            if market_dr_rate:
                self.fo_assert_value_border('Rate', 'Market DR Rate', market_dr_rate)
            if cross_rate:
                self.fo_assert_value_border('Rate', 'Cross Rate', cross_rate)
            if market_cr_rate:
                self.fo_assert_value_border('Rate', 'Market CR Rate', market_cr_rate)
            if debit_amount:
                self.fo_assert_value_border('Rate', 'Debit Amount', debit_amount)
            if reverse_rate:
                self.fo_assert_value_border('Rate', 'Reverse Rate', reverse_rate)
            if credit_amount:
                self.fo_assert_value_border('Rate', 'Credit Amount', credit_amount)
            if fee_amount:
                self.fo_assert_value_border('Rate', 'Fee Amount', fee_amount)
            if receive_amount:
                self.fo_assert_value_border('Rate', 'Receive Amount', receive_amount)
        self.wait_loading()
        self.fo_click_checkbox('Caution!  There is no doubt that banks may be used as a means of Money Laundering/ Terrorist Financing/ Proliferation of Weapons of Mass Destruction.')
        self.wait_loading()
        # click 'Accept'
        self.click_button('Accept')
        # approve
        if approve_later=='Y':
            self.click_button('Later')
        if approve_on_form=='Y':
            self.fo_approve_in_popup(
                username=username,
                password=password,
                reason=reason
            )
        if list_error_message:
        # verify error
            self.assert_error_message()
            self.assert_list_error_message(list_error_message)
            print('Transaction failed!')
        else:
        # verify success
            self.assert_button_disable('Accept')
            self.switch_to_core_banking()
            self.assert_notification('Saved successfully!')
            self.close_voucher()
            if expected_posting:
                self.assert_posting_data(**expected_posting)
            transaction_references=self.fo_get_text('Transaction references')
            print(f'Transaction references CSH_ACT: {transaction_references}')
            return transaction_references

    def csh_act_view(self, transaction_references, accounting_type_debit=None, account_name_debit=None, currency_debit=None, type_debit=None, accounting_type_credit=None, account_number_credit=None, account_name_credit=None, currency_credit=None, type_credit=None, enter_side=None, market_dr_rate=None, cross_rate=None, market_cr_rate=None, debit_amount=None, reverse_rate=None, credit_amount=None, fee_amount=None, receive_amount=None, customer_type=None, customer_code=None, full_name=None, paper_type=None, paper_number=None, telephone=None, address=None, nationality=None, description=None, ifc_codes=None, values=None, total_fee=None, expected_posting=None):
        self.transaction_view(transaction_references, 'FOF-FX Transaction')
        # compare value
        if expected_posting:
            self.assert_posting_data(**expected_posting)
        return transaction_references

    def csh_dpt(self, accounting_type_debit=None, account_name_debit=None, currency_debit=None, type_debit=None, accounting_type_credit=None, account_number_credit=None, account_name_credit=None, currency_credit=None, type_credit=None, enter_side=None, market_dr_rate=None, cross_rate=None, market_cr_rate=None, debit_amount=None, reverse_rate=None, credit_amount=None, fee_amount=None, receive_amount=None, customer_type=None, customer_code=None, full_name=None, paper_type=None, paper_number=None, telephone=None, address=None, nationality=None, description=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.click_menu('Front Office', 'FX Transaction')
        self.wait_for_button_available('Accept')
        self.assert_form_title('FOF-FX Transaction')
        # enter value
        if accounting_type_debit is None or accounting_type_debit == '':
            accounting_type_debit = 'Cash'
        if accounting_type_debit:
            self.fo_select_border('Debit', 'Accounting Type', accounting_type_debit)
        if account_name_debit:
            self.fo_write_text_border('Debit', 'Account name debit', account_name_debit)
        if currency_debit:
            self.fo_select_border('Debit', 'Currency', currency_debit)
        if type_debit:
            self.fo_select_border('Debit', 'Type', type_debit)
        if accounting_type_credit is None or accounting_type_credit == '':
            accounting_type_credit = 'Deposit'
        if accounting_type_credit:
            self.fo_select_border('Credit', 'Accounting Type', accounting_type_credit)
        if account_number_credit:
            account_number_credit_value = str(account_number_credit).replace('-', '')
            self.fo_write_border('Credit', 'Account numer', account_number_credit_value)
            self.wait_loading()
        if account_name_credit:
            self.fo_assert_text_border('Credit', 'Account name credit', account_name_credit)
        if currency_credit:
            self.fo_assert_value_border('Credit', 'Currency', currency_credit)
        if type_credit:
            self.fo_select_border('Credit', 'Type', type_credit)
        if customer_type:
            self.fo_select_border('Customer Information', 'Customer type', customer_type)
        if customer_code:
            self.fo_write_border('Customer Information', 'Customer code', customer_code)
        if full_name:
            self.fo_write_text_border('Customer Information', 'Full name', full_name)
        if paper_type:
            self.fo_select_border('Customer Information', 'Paper type', paper_type)
        if paper_number:
            self.fo_write_text_border('Customer Information', 'Paper number', paper_number)
        if telephone:
            self.fo_write_text_border('Customer Information', 'Telephone', telephone)
        if address:
            self.fo_write_text_border('Customer Information', 'Address', address)
        if nationality:
            self.fo_select_border('Customer Information', 'Nationality', nationality)
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_write_text_border('Customer Information', 'Description', description)
        if enter_side=='D':
            if debit_amount:
                self.fo_write_number_border('Rate', 'Debit Amount', debit_amount)
            if market_dr_rate:
                self.fo_assert_value_border('Rate', 'Market DR Rate', market_dr_rate)
            if cross_rate:
                self.fo_assert_value_border('Rate', 'Cross Rate', cross_rate)
            if market_cr_rate:
                self.fo_assert_value_border('Rate', 'Market CR Rate', market_cr_rate)
            if reverse_rate:
                self.fo_assert_value_border('Rate', 'Reverse Rate', reverse_rate)
            if credit_amount:
                self.fo_assert_value_border('Rate', 'Credit Amount', credit_amount)
        if enter_side=='C':
            if credit_amount:
                self.fo_write_number_border('Rate', 'Credit Amount', credit_amount)
            if debit_amount:
                self.fo_assert_value_border('Rate', 'Debit Amount', debit_amount)
            if market_dr_rate:
                self.fo_assert_value_border('Rate', 'Market DR Rate', market_dr_rate)
            if cross_rate:
                self.fo_assert_value_border('Rate', 'Cross Rate', cross_rate)
            if market_cr_rate:
                self.fo_assert_value_border('Rate', 'Market CR Rate', market_cr_rate)
            if reverse_rate:
                self.fo_assert_value_border('Rate', 'Reverse Rate', reverse_rate)
        if credit_amount:
            self.fo_assert_value_border('Rate', 'Receive Amount', credit_amount)
        self.fo_assert_value_border('Rate', 'Fee Amount', '0.00')
        if ifc_codes:
            self.add_fees(ifc_codes, values, total_fee)
            self.wait_loading()
            if market_dr_rate:
                self.fo_assert_value_border('Rate', 'Market DR Rate', market_dr_rate)
            if cross_rate:
                self.fo_assert_value_border('Rate', 'Cross Rate', cross_rate)
            if market_cr_rate:
                self.fo_assert_value_border('Rate', 'Market CR Rate', market_cr_rate)
            if debit_amount:
                self.fo_assert_value_border('Rate', 'Debit Amount', debit_amount)
            if reverse_rate:
                self.fo_assert_value_border('Rate', 'Reverse Rate', reverse_rate)
            if credit_amount:
                self.fo_assert_value_border('Rate', 'Credit Amount', credit_amount)
            if fee_amount:
                self.fo_assert_value_border('Rate', 'Fee Amount', fee_amount)
            if receive_amount:
                self.fo_assert_value_border('Rate', 'Receive Amount', receive_amount)
        self.wait_loading()
        self.fo_click_checkbox('Caution!  There is no doubt that banks may be used as a means of Money Laundering/ Terrorist Financing/ Proliferation of Weapons of Mass Destruction.')
        self.wait_loading()
        # click 'Accept'
        self.click_button('Accept')
        # approve
        if approve_later=='Y':
            self.click_button('Later')
        if approve_on_form=='Y':
            self.fo_approve_in_popup(
                username=username,
                password=password,
                reason=reason
            )
        if list_error_message:
        # verify error
            self.assert_error_message()
            self.assert_list_error_message(list_error_message)
            print('Transaction failed!')
        else:
        # verify success
            self.assert_button_disable('Accept')
            self.switch_to_core_banking()
            self.assert_notification('Saved successfully!')
            self.close_voucher()
            if expected_posting:
                self.assert_posting_data(**expected_posting)
            transaction_references=self.fo_get_text('Transaction references')
            print(f'Transaction references CSH_DPT: {transaction_references}')
            return transaction_references

    def csh_dpt_view(self, transaction_references, accounting_type_debit=None, account_name_debit=None, currency_debit=None, type_debit=None, accounting_type_credit=None, account_number_credit=None, account_name_credit=None, currency_credit=None, type_credit=None, enter_side=None, market_dr_rate=None, cross_rate=None, market_cr_rate=None, debit_amount=None, reverse_rate=None, credit_amount=None, fee_amount=None, receive_amount=None, customer_type=None, customer_code=None, full_name=None, paper_type=None, paper_number=None, telephone=None, address=None, nationality=None, description=None, ifc_codes=None, values=None, total_fee=None, expected_posting=None):
        self.transaction_view(transaction_references, 'FOF-FX Transaction')
        # compare value
        if expected_posting:
            self.assert_posting_data(**expected_posting)
        return transaction_references

    def dpt_dpt(self, accounting_type_debit=None, account_number_debit=None, account_name_debit=None, currency_debit=None, type_debit=None, accounting_type_credit=None, account_number_credit=None, account_name_credit=None, currency_credit=None, type_credit=None, enter_side=None, market_dr_rate=None, cross_rate=None, market_cr_rate=None, debit_amount=None, reverse_rate=None, credit_amount=None, fee_amount=None, receive_amount=None, customer_type=None, customer_code=None, full_name=None, paper_type=None, paper_number=None, telephone=None, address=None, nationality=None, description=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.click_menu('Front Office', 'FX Transaction')
        self.wait_for_button_available('Accept')
        self.assert_form_title('FOF-FX Transaction')
        # enter value
        if accounting_type_debit is None or accounting_type_debit == '':
            accounting_type_debit = 'Deposit'
        if accounting_type_debit:
            self.fo_select_border('Debit', 'Accounting Type', accounting_type_debit)
        if account_number_debit:
            account_number_debit_value = str(account_number_debit).replace('-', '')
            self.fo_write_border('Debit', 'Account number', account_number_debit_value)
            self.wait_loading()
        if account_name_debit:
            self.fo_assert_text_border('Debit', 'Account name debit', account_name_debit)
        if currency_debit:
            self.fo_assert_value_border('Debit', 'Currency', currency_debit)
        if type_debit:
            self.fo_select_border('Debit', 'Type', type_debit)
        if accounting_type_credit is None or accounting_type_credit == '':
            accounting_type_credit = 'Deposit'
        if accounting_type_credit:
            self.fo_select_border('Credit', 'Accounting Type', accounting_type_credit)
        if account_number_credit:
            account_number_credit_value = str(account_number_credit).replace('-', '')
            self.fo_write_border('Credit', 'Account numer', account_number_credit_value)
            self.wait_loading()
        if account_name_credit:
            self.fo_assert_text_border('Credit', 'Account name credit', account_name_credit)
        if currency_credit:
            self.fo_assert_value_border('Credit', 'Currency', currency_credit)
        if type_credit:
            self.fo_select_border('Credit', 'Type', type_credit)
        if customer_type:
            self.fo_select_border('Customer Information', 'Customer type', customer_type)
        if customer_code:
            self.fo_write_border('Customer Information', 'Customer code', customer_code)
        if full_name:
            self.fo_write_text_border('Customer Information', 'Full name', full_name)
        if paper_type:
            self.fo_select_border('Customer Information', 'Paper type', paper_type)
        if paper_number:
            self.fo_write_text_border('Customer Information', 'Paper number', paper_number)
        if telephone:
            self.fo_write_text_border('Customer Information', 'Telephone', telephone)
        if address:
            self.fo_write_text_border('Customer Information', 'Address', address)
        if nationality:
            self.fo_select_border('Customer Information', 'Nationality', nationality)
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_write_text_border('Customer Information', 'Description', description)
        if enter_side=='D':
            if debit_amount:
                self.fo_write_number_border('Rate', 'Debit Amount', debit_amount)
            if market_dr_rate:
                self.fo_assert_value_border('Rate', 'Market DR Rate', market_dr_rate)
            if cross_rate:
                self.fo_assert_value_border('Rate', 'Cross Rate', cross_rate)
            if market_cr_rate:
                self.fo_assert_value_border('Rate', 'Market CR Rate', market_cr_rate)
            if reverse_rate:
                self.fo_assert_value_border('Rate', 'Reverse Rate', reverse_rate)
            if credit_amount:
                self.fo_assert_value_border('Rate', 'Credit Amount', credit_amount)
        if enter_side=='C':
            if credit_amount:
                self.fo_write_number_border('Rate', 'Credit Amount', credit_amount)
            if debit_amount:
                self.fo_assert_value_border('Rate', 'Debit Amount', debit_amount)
            if market_dr_rate:
                self.fo_assert_value_border('Rate', 'Market DR Rate', market_dr_rate)
            if cross_rate:
                self.fo_assert_value_border('Rate', 'Cross Rate', cross_rate)
            if market_cr_rate:
                self.fo_assert_value_border('Rate', 'Market CR Rate', market_cr_rate)
            if reverse_rate:
                self.fo_assert_value_border('Rate', 'Reverse Rate', reverse_rate)
        if credit_amount:
            self.fo_assert_value_border('Rate', 'Receive Amount', credit_amount)
        self.fo_assert_value_border('Rate', 'Fee Amount', '0.00')
        if ifc_codes:
            self.add_fees(ifc_codes, values, total_fee)
            self.wait_loading()
            if market_dr_rate:
                self.fo_assert_value_border('Rate', 'Market DR Rate', market_dr_rate)
            if cross_rate:
                self.fo_assert_value_border('Rate', 'Cross Rate', cross_rate)
            if market_cr_rate:
                self.fo_assert_value_border('Rate', 'Market CR Rate', market_cr_rate)
            if debit_amount:
                self.fo_assert_value_border('Rate', 'Debit Amount', debit_amount)
            if reverse_rate:
                self.fo_assert_value_border('Rate', 'Reverse Rate', reverse_rate)
            if credit_amount:
                self.fo_assert_value_border('Rate', 'Credit Amount', credit_amount)
            if fee_amount:
                self.fo_assert_value_border('Rate', 'Fee Amount', fee_amount)
            if receive_amount:
                self.fo_assert_value_border('Rate', 'Receive Amount', receive_amount)
        self.wait_loading()
        self.fo_click_checkbox('Caution!  There is no doubt that banks may be used as a means of Money Laundering/ Terrorist Financing/ Proliferation of Weapons of Mass Destruction.')
        self.wait_loading()
        # click 'Accept'
        self.click_button('Accept')
        # approve
        if approve_later=='Y':
            self.click_button('Later')
        if approve_on_form=='Y':
            self.fo_approve_in_popup(
                username=username,
                password=password,
                reason=reason
            )
        if list_error_message:
        # verify error
            self.assert_error_message()
            self.assert_list_error_message(list_error_message)
            print('Transaction failed!')
        else:
        # verify success
            self.assert_button_disable('Accept')
            self.switch_to_core_banking()
            self.assert_notification('Saved successfully!')
            self.close_voucher()
            if expected_posting:
                self.assert_posting_data(**expected_posting)
            transaction_references=self.fo_get_text('Transaction references')
            print(f'Transaction references DPT_DPT: {transaction_references}')
            return transaction_references

    def dpt_dpt_view(self, transaction_references, accounting_type_debit=None, accounting_type_credit=None, account_number_debit=None, account_name_debit=None, currency_debit=None, type_debit=None, account_number_credit=None, account_name_credit=None, currency_credit=None, type_credit=None, market_dr_rate=None, cross_rate=None, market_cr_rate=None, debit_amount=None, reverse_rate=None, credit_amount=None, fee_amount=None, receive_amount=None, customer_type=None, customer_code=None, full_name=None, paper_type=None, paper_number=None, telephone=None, address=None, nationality=None, description=None, ifc_codes=None, values=None, total_fee=None, expected_posting=None):
        self.transaction_view(transaction_references, 'FOF-FX Transaction')
        # compare value
        if expected_posting:
            self.assert_posting_data(**expected_posting)
        return transaction_references

    def dpt_act(self, accounting_type_debit=None, account_number_debit=None, account_name_debit=None, currency_debit=None, type_debit=None, accounting_type_credit=None, account_number_credit=None, account_name_credit=None, currency_credit=None, type_credit=None, enter_side=None, market_dr_rate=None, cross_rate=None, market_cr_rate=None, debit_amount=None, reverse_rate=None, credit_amount=None, fee_amount=None, receive_amount=None, customer_type=None, customer_code=None, full_name=None, paper_type=None, paper_number=None, telephone=None, address=None, nationality=None, description=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.click_menu('Front Office', 'FX Transaction')
        self.wait_for_button_available('Accept')
        self.assert_form_title('FOF-FX Transaction')
        # enter value
        if accounting_type_debit is None or accounting_type_debit == '':
            accounting_type_debit = 'Deposit'
        if accounting_type_debit:
            self.fo_select_border('Debit', 'Accounting Type', accounting_type_debit)
        if account_number_debit:
            account_number_debit_value = str(account_number_debit).replace('-', '')
            self.fo_write_border('Debit', 'Account number', account_number_debit_value)
            self.wait_loading()
        if account_name_debit:
            self.fo_assert_text_border('Debit', 'Account name debit', account_name_debit)
        if currency_debit:
            self.fo_assert_value_border('Debit', 'Currency', currency_debit)
        if type_debit:
            self.fo_select_border('Debit', 'Type', type_debit)
        if accounting_type_credit is None or accounting_type_credit == '':
            accounting_type_credit = 'Accounting'
        if accounting_type_credit:
            self.fo_select_border('Credit', 'Accounting Type', accounting_type_credit)
        if account_number_credit:
            account_number_credit_value = str(account_number_credit).replace('-', '')
            self.fo_write_border('Credit', 'Account number', account_number_credit_value)
            self.wait_loading()
        if account_name_credit:
            self.fo_assert_text_border('Credit', 'Account name credit', account_name_credit)
        if currency_credit:
            self.fo_assert_value_border('Credit', 'Currency', currency_credit)
        if type_credit:
            self.fo_select_border('Credit', 'Type', type_credit)
        if customer_type:
            self.fo_select_border('Customer Information', 'Customer type', customer_type)
        if customer_code:
            self.fo_write_border('Customer Information', 'Customer code', customer_code)
        if full_name:
            self.fo_write_text_border('Customer Information', 'Full name', full_name)
        if paper_type:
            self.fo_select_border('Customer Information', 'Paper type', paper_type)
        if paper_number:
            self.fo_write_text_border('Customer Information', 'Paper number', paper_number)
        if telephone:
            self.fo_write_text_border('Customer Information', 'Telephone', telephone)
        if address:
            self.fo_write_text_border('Customer Information', 'Address', address)
        if nationality:
            self.fo_select_border('Customer Information', 'Nationality', nationality)
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_write_text_border('Customer Information', 'Description', description)
        if enter_side=='D':
            if debit_amount:
                self.fo_write_number_border('Rate', 'Debit Amount', debit_amount)
            if market_dr_rate:
                self.fo_assert_value_border('Rate', 'Market DR Rate', market_dr_rate)
            if cross_rate:
                self.fo_assert_value_border('Rate', 'Cross Rate', cross_rate)
            if market_cr_rate:
                self.fo_assert_value_border('Rate', 'Market CR Rate', market_cr_rate)
            if reverse_rate:
                self.fo_assert_value_border('Rate', 'Reverse Rate', reverse_rate)
            if credit_amount:
                self.fo_assert_value_border('Rate', 'Credit Amount', credit_amount)
        if enter_side=='C':
            if credit_amount:
                self.fo_write_number_border('Rate', 'Credit Amount', credit_amount)
            if debit_amount:
                self.fo_assert_value_border('Rate', 'Debit Amount', debit_amount)
            if market_dr_rate:
                self.fo_assert_value_border('Rate', 'Market DR Rate', market_dr_rate)
            if cross_rate:
                self.fo_assert_value_border('Rate', 'Cross Rate', cross_rate)
            if market_cr_rate:
                self.fo_assert_value_border('Rate', 'Market CR Rate', market_cr_rate)
            if reverse_rate:
                self.fo_assert_value_border('Rate', 'Reverse Rate', reverse_rate)
        if credit_amount:
            self.fo_assert_value_border('Rate', 'Receive Amount', credit_amount)
        self.fo_assert_value_border('Rate', 'Fee Amount', '0.00')
        if ifc_codes:
            self.add_fees(ifc_codes, values, total_fee)
            self.wait_loading()
            if market_dr_rate:
                self.fo_assert_value_border('Rate', 'Market DR Rate', market_dr_rate)
            if cross_rate:
                self.fo_assert_value_border('Rate', 'Cross Rate', cross_rate)
            if market_cr_rate:
                self.fo_assert_value_border('Rate', 'Market CR Rate', market_cr_rate)
            if debit_amount:
                self.fo_assert_value_border('Rate', 'Debit Amount', debit_amount)
            if reverse_rate:
                self.fo_assert_value_border('Rate', 'Reverse Rate', reverse_rate)
            if credit_amount:
                self.fo_assert_value_border('Rate', 'Credit Amount', credit_amount)
            if fee_amount:
                self.fo_assert_value_border('Rate', 'Fee Amount', fee_amount)
            if receive_amount:
                self.fo_assert_value_border('Rate', 'Receive Amount', receive_amount)
        self.wait_loading()
        self.fo_click_checkbox('Caution!  There is no doubt that banks may be used as a means of Money Laundering/ Terrorist Financing/ Proliferation of Weapons of Mass Destruction.')
        self.wait_loading()
        # click 'Accept'
        self.click_button('Accept')
        # approve
        if approve_later=='Y':
            self.click_button('Later')
        if approve_on_form=='Y':
            self.fo_approve_in_popup(
                username=username,
                password=password,
                reason=reason
            )
        if list_error_message:
        # verify error
            self.assert_error_message()
            self.assert_list_error_message(list_error_message)
            print('Transaction failed!')
        else:
        # verify success
            self.assert_button_disable('Accept')
            self.switch_to_core_banking()
            self.assert_notification('Saved successfully!')
            self.close_voucher()
            if expected_posting:
                self.assert_posting_data(**expected_posting)
            transaction_references=self.fo_get_text('Transaction references')
            print(f'Transaction references DPT_ACT: {transaction_references}')
            return transaction_references

    def dpt_act_view(self, transaction_references, accounting_type_debit=None, account_number_debit=None, account_name_debit=None, currency_debit=None, type_debit=None, accounting_type_credit=None, account_number_credit=None, account_name_credit=None, currency_credit=None, type_credit=None, enter_side=None, market_dr_rate=None, cross_rate=None, market_cr_rate=None, debit_amount=None, reverse_rate=None, credit_amount=None, fee_amount=None, receive_amount=None, customer_type=None, customer_code=None, full_name=None, paper_type=None, paper_number=None, telephone=None, address=None, nationality=None, description=None, ifc_codes=None, values=None, total_fee=None, expected_posting=None):
        self.transaction_view(transaction_references, 'FOF-FX Transaction')
        # compare value
        if expected_posting:
            self.assert_posting_data(**expected_posting)
        return transaction_references

    def dpt_csh(self, accounting_type_debit=None, account_number_debit=None, account_name_debit=None, currency_debit=None, type_debit=None, accounting_type_credit=None, account_name_credit=None, currency_credit=None, type_credit=None, enter_side=None, market_dr_rate=None, cross_rate=None, market_cr_rate=None, debit_amount=None, reverse_rate=None, credit_amount=None, fee_amount=None, receive_amount=None, customer_type=None, customer_code=None, full_name=None, paper_type=None, paper_number=None, telephone=None, address=None, nationality=None, description=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.click_menu('Front Office', 'FX Transaction')
        self.wait_for_button_available('Accept')
        self.assert_form_title('FOF-FX Transaction')
        # enter value
        if accounting_type_debit is None or accounting_type_debit == '':
            accounting_type_debit = 'Deposit'
        if accounting_type_debit:
            self.fo_select_border('Debit', 'Accounting Type', accounting_type_debit)
        if account_number_debit:
            account_number_debit_value = str(account_number_debit).replace('-', '')
            self.fo_write_border('Debit', 'Account number', account_number_debit_value)
            self.wait_loading()
        if account_name_debit:
            self.fo_assert_text_border('Debit', 'Account name debit', account_name_debit)
        if currency_debit:
            self.fo_assert_value_border('Debit', 'Currency', currency_debit)
        if type_debit:
            self.fo_select_border('Debit', 'Type', type_debit)
        if accounting_type_credit is None or accounting_type_credit == '':
            accounting_type_credit = 'Cash'
        if accounting_type_credit:
            self.fo_select_border('Credit', 'Accounting Type', accounting_type_credit)
        if account_name_credit:
            self.fo_write_text_border('Credit', 'Account name credit', account_name_credit)
        if currency_credit:
            self.fo_select_border('Credit', 'Currency', currency_credit)
        if type_credit:
            self.fo_select_border('Credit', 'Type', type_credit)
        if customer_type:
            self.fo_select_border('Customer Information', 'Customer type', customer_type)
        if customer_code:
            self.fo_write_border('Customer Information', 'Customer code', customer_code)
        if full_name:
            self.fo_write_text_border('Customer Information', 'Full name', full_name)
        if paper_type:
            self.fo_select_border('Customer Information', 'Paper type', paper_type)
        if paper_number:
            self.fo_write_text_border('Customer Information', 'Paper number', paper_number)
        if telephone:
            self.fo_write_text_border('Customer Information', 'Telephone', telephone)
        if address:
            self.fo_write_text_border('Customer Information', 'Address', address)
        if nationality:
            self.fo_select_border('Customer Information', 'Nationality', nationality)
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_write_text_border('Customer Information', 'Description', description)
        if enter_side=='D':
            if debit_amount:
                self.fo_write_number_border('Rate', 'Debit Amount', debit_amount)
            if market_dr_rate:
                self.fo_assert_value_border('Rate', 'Market DR Rate', market_dr_rate)
            if cross_rate:
                self.fo_assert_value_border('Rate', 'Cross Rate', cross_rate)
            if market_cr_rate:
                self.fo_assert_value_border('Rate', 'Market CR Rate', market_cr_rate)
            if reverse_rate:
                self.fo_assert_value_border('Rate', 'Reverse Rate', reverse_rate)
            if credit_amount:
                self.fo_assert_value_border('Rate', 'Credit Amount', credit_amount)
        if enter_side=='C':
            if credit_amount:
                self.fo_write_number_border('Rate', 'Credit Amount', credit_amount)
            if debit_amount:
                self.fo_assert_value_border('Rate', 'Debit Amount', debit_amount)
            if market_dr_rate:
                self.fo_assert_value_border('Rate', 'Market DR Rate', market_dr_rate)
            if cross_rate:
                self.fo_assert_value_border('Rate', 'Cross Rate', cross_rate)
            if market_cr_rate:
                self.fo_assert_value_border('Rate', 'Market CR Rate', market_cr_rate)
            if reverse_rate:
                self.fo_assert_value_border('Rate', 'Reverse Rate', reverse_rate)
        if credit_amount:
            self.fo_assert_value_border('Rate', 'Receive Amount', credit_amount)
        self.fo_assert_value_border('Rate', 'Fee Amount', '0.00')
        if ifc_codes:
            self.add_fees(ifc_codes, values, total_fee)
            self.wait_loading()
            if market_dr_rate:
                self.fo_assert_value_border('Rate', 'Market DR Rate', market_dr_rate)
            if cross_rate:
                self.fo_assert_value_border('Rate', 'Cross Rate', cross_rate)
            if market_cr_rate:
                self.fo_assert_value_border('Rate', 'Market CR Rate', market_cr_rate)
            if debit_amount:
                self.fo_assert_value_border('Rate', 'Debit Amount', debit_amount)
            if reverse_rate:
                self.fo_assert_value_border('Rate', 'Reverse Rate', reverse_rate)
            if credit_amount:
                self.fo_assert_value_border('Rate', 'Credit Amount', credit_amount)
            if fee_amount:
                self.fo_assert_value_border('Rate', 'Fee Amount', fee_amount)
            if receive_amount:
                self.fo_assert_value_border('Rate', 'Receive Amount', receive_amount)
        self.wait_loading()
        self.fo_click_checkbox('Caution!  There is no doubt that banks may be used as a means of Money Laundering/ Terrorist Financing/ Proliferation of Weapons of Mass Destruction.')
        self.wait_loading()
        # click 'Accept'
        self.click_button('Accept')
        # approve
        if approve_later=='Y':
            self.click_button('Later')
        if approve_on_form=='Y':
            self.fo_approve_in_popup(
                username=username,
                password=password,
                reason=reason
            )
        if list_error_message:
        # verify error
            self.assert_error_message()
            self.assert_list_error_message(list_error_message)
            print('Transaction failed!')
        else:
        # verify success
            self.assert_button_disable('Accept')
            self.switch_to_core_banking()
            self.assert_notification('Saved successfully!')
            self.close_voucher()
            if expected_posting:
                self.assert_posting_data(**expected_posting)
            transaction_references=self.fo_get_text('Transaction references')
            print(f'Transaction references DPT_CSH: {transaction_references}')
            return transaction_references

    def dpt_csh_view(self, transaction_references, accounting_type_debit=None, account_number_debit=None, account_name_debit=None, currency_debit=None, type_debit=None, accounting_type_credit=None, account_name_credit=None, currency_credit=None, type_credit=None, enter_side=None, market_dr_rate=None, cross_rate=None, market_cr_rate=None, debit_amount=None, reverse_rate=None, credit_amount=None, fee_amount=None, receive_amount=None, customer_type=None, customer_code=None, full_name=None, paper_type=None, paper_number=None, telephone=None, address=None, nationality=None, description=None, ifc_codes=None, values=None, total_fee=None, expected_posting=None):
        self.transaction_view(transaction_references, 'FOF-FX Transaction')
        # compare value
        if expected_posting:
            self.assert_posting_data(**expected_posting)
        return transaction_references

# -------------------------- handle BO - TREASURY --------------------------
    # TRS-Treasury account information
    def treasury_account_simple_search(self, text):
        self.close_all_form()
        self.click_menu('Treasury', 'Account Information')
        self.wait_for_button_available('Search')
        self.assert_form_title('TRS-Account Information Search')
        self.simple_search(text)

    def treasury_account_view(self, account_number, account_status=None, counterparty_code=None, catalogue_code=None, trade_type=None, contract_rate=None, account_name=None, value_date=None, reference_rate=None, swap_point=None, debit_currency=None, credit_currency=None, debit_by=None, debit_amount=None, debit_account=None, credit_by=None, credit_amount=None, credit_account=None):
        # search treasury account
        self.treasury_account_simple_search(str(account_number).replace('-', ''))
        self.assert_table_data('Account number', 1, self.treasury_account_number_mask(account_number))
        if account_status:
            self.assert_table_data('Account status', 1, account_status)
        if catalogue_code:
            self.assert_table_data('Category code', 1, catalogue_code)
        if counterparty_code:
            self.assert_table_data('Counterparty code', 1, counterparty_code)
        # view treasury account
        self.click_table_menu('View', 1)
        self.wait_for_button_available('Modify')
        self.assert_form_title('TRS-Account Information-View')
        # verify value tab 'General information'
        self.bo_assert_value('Account number', self.treasury_account_number_mask(account_number))
        if counterparty_code:
            self.bo_assert_value_group('Counterparty code', counterparty_code)
        if account_name:
            self.bo_assert_text('Account name', account_name)
        if catalogue_code:
            self.bo_assert_text('Category code', catalogue_code)
        if trade_type:
            self.bo_assert_select('Trade type', trade_type)
        if account_status:
            self.bo_assert_select('Account status', account_status)
        if value_date:
            self.bo_assert_date('Value date', value_date)
        # verify value tab 'Settlement information'
        self.bo_click_tab('Settlement information')
        if value_date:
            self.bo_assert_value_multi('Phase 1', 'Value date', value_date)
        if debit_by:
            self.bo_assert_value_multi('Phase 1', 'Debit by', debit_by)
        if debit_account:
            self.bo_assert_text_multi('Phase 1', 'Debit account', str(debit_account).replace('-', ''))
        if debit_currency:
            self.bo_assert_value_multi('Phase 1', 'Debit currency', debit_currency)
        if debit_amount:
            self.bo_assert_value_multi('Phase 1', 'Debit amount', debit_amount)
        if reference_rate:
            self.bo_assert_value_multi('Phase 1', 'Reference rate', reference_rate)
        if swap_point:
            self.bo_assert_value_multi('Phase 1', 'Swap point', swap_point)
        if contract_rate:
            self.bo_assert_value_multi('Phase 1', 'Trade rate', contract_rate)
        if credit_by:
            self.bo_assert_value_multi('Phase 1', 'Credit by', credit_by)
        if credit_account:
            self.bo_assert_text_multi('Phase 1', 'Credit account', str(credit_account).replace('-', ''))
        if credit_currency:
            self.bo_assert_value_multi('Phase 1', 'Credit currency', credit_currency)
        if credit_amount:
            self.bo_assert_value_multi('Phase 1', 'Credit amount', credit_amount)

# -------------------------- handle BO - TRADE FINANCE --------------------------
    # TRD-Trade account information
    def trade_account_simple_search(self, text):
        self.close_all_form()
        self.click_menu('Trade Finance', 'Account Information')
        self.wait_for_button_available('Search')
        self.assert_form_title('TRD-Account Information Search')
        self.simple_search(text)

    def trade_account_view(self, account_number, account_status=None, category_code=None, customer_code=None, account_name=None, account_holder_type=None, branch_code=None, currency_code=None, business_group=None, details_category=None, term_and_condition=None, tenor=None, reference_number=None, customer_type=None, counter_party_name=None, counter_party_address=None, usance_days=None, holding_days=None, open_date=None, close_date=None, extension_date=None, effective_date=None, effective_date_extension=None, maturity_date=None, maturity_date_extension=None, last_date_of_shippment=None, last_transaction_date=None, previous_ac_status=None, document_status=None, previous_doc_status=None, place_of_maturity=None, country=None, partial_shipments=None, transhipment=None, created_by=None, approved_by=None, account_manager_staff_code=None, term_code=None, amount=None, release_amount=None, amount_paid=None, lower_tolerance=None, upper_tolerance=None, margin_deposit_account=None, margin_rate=None, margin_amount=None, released_margin_amount=None, guarantee_amount=None, released_guarantee_amount=None, secured_amount=None, released_secured_amount=None, off_balance_sheet_amount=None, release_off_balance_sheet_amount=None, off_balance_percentage=None, holding_amount=None, amount_sent_for_collection=None, amount_accept_of_payment=None, amount_arrived_of_payment=None, fee_amount=None, paid_fee_amount=None, negotiation_amount=None, transfer_amount=None, discounted_reta_reduction_rate=None, obs_percentage_rate=None, business_step_status_string=None, current_business_step=None, confirm=None, advising_maner=None, amend_no=None, draft_number=None, first_ref_account_number=None, cycle=None, week_debit=None, week_credit=None, month_debit=None, month_credit=None, quarter_debit=None, quarter_credit=None, semi_annual_debit=None, semi_annual_credit=None, year_debit=None, year_credit=None, expected_account_gl_names=None, expected_account_gl_numbers=None, expected_account_gl_name=None, expected_account_gl_number=None, issuing_bank=None, confirming_bank=None, negotiating_bank=None, paying_bank=None, advising_bank=None, remitting_bank=None, reference_number_in_agent_bank=None, remark=None, guarantee_period=None, guarantee_period_unit=None, bg_number=None, project_name=None, send_to=None, user_define_field=None):
        # search trade account
        self.trade_account_simple_search(str(account_number).replace('-', ''))
        self.assert_table_data('Account number', 1, self.trade_account_number_mask(account_number))
        if account_status:
            self.assert_table_data('Account status', 1, account_status)
        if category_code:
            self.assert_table_data('Category code', 1, category_code)
        if customer_code:
            self.assert_table_data('Customer code', 1, self.customer_code_mask(customer_code))
        # view trade account
        self.click_table_menu('View', 1)
        self.wait_for_button_available('Modify')
        self.assert_form_title('TRD-Account Information-View')
        # verify value tab 'Account GLs Information'
        self.bo_click_tab('Account GLs Information')
        if expected_account_gl_names:
            for account_gl_name, account_gl_number in zip(expected_account_gl_names, expected_account_gl_numbers):
                self.bo_assert_text_table_account_gls(account_gl_name, str(account_gl_number).replace('-',''))
        if expected_account_gl_name:
            self.bo_assert_text_table_account_gls(expected_account_gl_name, str(expected_account_gl_number).replace('-',''))
        # verify value tab 'General information'
        self.bo_click_tab('General information')
        self.bo_assert_value('Account number', self.trade_account_number_mask(account_number))
        if account_name:
            self.bo_assert_text('Account name', account_name)
        if customer_code:
            self.bo_assert_value_group('Account holder code', self.customer_code_mask(customer_code))
        if account_holder_type:
            self.bo_assert_select('Account holder type', account_holder_type)
        if branch_code:
            self.bo_assert_text_group('Branch code', branch_code)
        if category_code:
            self.bo_assert_text_group('Category code', category_code)
        if currency_code:
            self.bo_assert_select('Currency code', currency_code)
        if business_group:
            self.bo_assert_select('Business group', business_group)
        if details_category:
            self.bo_assert_select('Details category', details_category)
        if term_and_condition:
            self.bo_assert_select('Term and condition', term_and_condition)
        if tenor:
            self.bo_assert_select('Tenor', tenor)
        if reference_number:
            self.bo_assert_text('Reference number', reference_number)
        if customer_type:
            self.bo_assert_select('Customer type', customer_type)
        if counter_party_name:
            self.bo_assert_text('Counter party name', counter_party_name)
        if counter_party_address:
            self.bo_assert_text('Counter party address', counter_party_address)
        if usance_days:
            self.bo_assert_value('Usance days', usance_days)
        if holding_days:
            self.bo_assert_value('Holding days', holding_days)
        if open_date:
            self.bo_assert_date('Open date', open_date)
        if close_date:
            self.bo_assert_date('Close date', close_date)
        if extension_date:
            self.bo_assert_date('Extension date', extension_date)
        if effective_date:
            self.bo_assert_date('Effective date', effective_date)
        if effective_date_extension:
            self.bo_assert_date('Effective date extension', effective_date_extension)
        if maturity_date:
            self.bo_assert_date('Maturity date', maturity_date)
        if maturity_date_extension:
            self.bo_assert_date('Maturity date extension', maturity_date_extension)
        if last_date_of_shippment:
            self.bo_assert_date('Last date of shippment', last_date_of_shippment)
        if last_transaction_date:
            self.bo_assert_date('Last transaction date', last_transaction_date)
        if account_status:
            self.bo_assert_select('Account status', account_status)
        if previous_ac_status:
            self.bo_assert_select('Previous A/c status', previous_ac_status)
        if document_status:
            self.bo_assert_select('Document status', document_status)
        if previous_doc_status:
            self.bo_assert_select('Previous doc status', previous_doc_status)
        if place_of_maturity:
            self.bo_assert_text('Place of Maturity', place_of_maturity)
        if country:
            self.bo_assert_select('Country', country)
        if partial_shipments:
            self.bo_assert_select('Partial shipments', partial_shipments)
        if transhipment:
            self.bo_assert_select('Transhipment', transhipment)
        if created_by:
            self.bo_assert_text('Created by', created_by)
        if approved_by:
            self.bo_assert_text('Approved by', approved_by)
        if account_manager_staff_code:
            self.bo_assert_text('Account manager staff code', account_manager_staff_code)
        # verify value tab 'Commercial term'
        self.bo_click_tab('Commercial term')
        if term_code:
            self.bo_assert_select('Term code', term_code)
        if amount:
            self.bo_assert_value('Amount', amount)
        if release_amount:
            self.bo_assert_value('Release amount', release_amount)
        if amount_paid:
            self.bo_assert_value('Amount paid', amount_paid)
        if lower_tolerance:
            self.bo_assert_value('Lower tolerance', lower_tolerance)
        if upper_tolerance:
            self.bo_assert_value('Upper tolerance', upper_tolerance)
        if margin_deposit_account:
            self.bo_assert_value('Margin deposit account', margin_deposit_account)
        if margin_rate:
            self.bo_assert_value('Margin rate', margin_rate)
        if margin_amount:
            self.bo_assert_value('Margin amount', margin_amount)
        if released_margin_amount:
            self.bo_assert_value('Released margin amount', released_margin_amount)
        if guarantee_amount:
            self.bo_assert_value('Guarantee amount', guarantee_amount)
        if released_guarantee_amount:
            self.bo_assert_value('Released guarantee amount', released_guarantee_amount)
        if secured_amount:
            self.bo_assert_value('Secured amount', secured_amount)
        if released_secured_amount:
            self.bo_assert_value('Released secured amount', released_secured_amount)
        if off_balance_sheet_amount:
            self.bo_assert_value('Off-balance sheet amount', off_balance_sheet_amount)
        if release_off_balance_sheet_amount:
            self.bo_assert_value('Release off-balance sheet amount', release_off_balance_sheet_amount)
        if off_balance_percentage:
            self.bo_assert_value('Off Balance Percentage', off_balance_percentage)
        if holding_amount:
            self.bo_assert_value('Holding amount', holding_amount)
        if amount_sent_for_collection:
            self.bo_assert_value('Amount sent for collection', amount_sent_for_collection)
        if amount_accept_of_payment:
            self.bo_assert_value('Amount accept of payment', amount_accept_of_payment)
        if amount_arrived_of_payment:
            self.bo_assert_value('Amount arrived of payment', amount_arrived_of_payment)
        if fee_amount:
            self.bo_assert_value('Fee amount', fee_amount)
        if paid_fee_amount:
            self.bo_assert_value('Paid fee amount', paid_fee_amount)
        if negotiation_amount:
            self.bo_assert_value('Negotiation amount', negotiation_amount)
        if transfer_amount:
            self.bo_assert_value('Transfer amount', transfer_amount)
        if discounted_reta_reduction_rate:
            self.bo_assert_value('Discounted reta/reduction rate', discounted_reta_reduction_rate)
        if obs_percentage_rate:
            self.bo_assert_value('OBS percentage/rate', obs_percentage_rate)
        if business_step_status_string:
            self.bo_assert_text('Business step status string', business_step_status_string)
        if current_business_step:
            self.bo_assert_text('Current business step', current_business_step)
        if confirm:
            self.bo_assert_select('Confirm', confirm)
        if advising_maner:
            self.bo_assert_select('Advising maner', advising_maner)
        if amend_no:
            self.bo_assert_value('Amend no', amend_no)
        if draft_number:
            self.bo_assert_text('Draft number', draft_number)
        if first_ref_account_number:
            self.bo_assert_text('1st ref account number', first_ref_account_number)
        if cycle:
            self.bo_assert_value('Cycle', cycle)
        if week_debit:
            self.bo_assert_value('Week debit', week_debit)
        if week_credit:
            self.bo_assert_value('Week credit', week_credit)
        if month_debit:
            self.bo_assert_value('Month debit', month_debit)
        if month_credit:
            self.bo_assert_value('Month credit', month_credit)
        if quarter_debit:
            self.bo_assert_value('Quarter debit', quarter_debit)
        if quarter_credit:
            self.bo_assert_value('Quarter credit', quarter_credit)
        if semi_annual_debit:
            self.bo_assert_value('Semi-annual debit', semi_annual_debit)
        if semi_annual_credit:
            self.bo_assert_value('Semi-annual credit', semi_annual_credit)
        if year_debit:
            self.bo_assert_value('Year debit', year_debit)
        if year_credit:
            self.bo_assert_value('Year credit', year_credit)
        # verify value tab 'IFC list'
        self.bo_click_tab('IFC list')

        # verify value tab 'IFC GLs Information'
        self.bo_click_tab('IFC GLs Information')

        # verify value tab 'Other information'
        self.bo_click_tab('Other information')
        if issuing_bank:
            self.bo_assert_text('Issuing bank', issuing_bank)
        if confirming_bank:
            self.bo_assert_value_group('Confirming bank', confirming_bank)
        if negotiating_bank:
            self.bo_assert_value_group('Negotiating bank', negotiating_bank)
        if paying_bank:
            self.bo_assert_value_group('Paying bank', paying_bank)
        if advising_bank:
            self.bo_assert_value_group('Advising bank', advising_bank)
        if remitting_bank:
            self.bo_assert_value_group('Remitting bank', remitting_bank)
        if reference_number_in_agent_bank:
            self.bo_assert_text('Reference number in agent bank', reference_number_in_agent_bank)
        if remark:
            self.bo_assert_text('Remark', remark)
        if guarantee_period:
            self.bo_assert_select('Guarantee period', guarantee_period)
        if guarantee_period_unit:
            self.bo_assert_select('Guarantee period unit', guarantee_period_unit)
        if bg_number:
            self.bo_assert_text('BG number', bg_number)
        if project_name:
            self.bo_assert_text('Project name', project_name)
        if send_to:
            self.fo_assert_text_multi_line('Send to', send_to)
        if user_define_field:
            self.bo_assert_text('User define field', user_define_field)
        # verify value tab 'Document attachment'
        self.bo_click_tab('Document attachment')

    # TRD-Document attachment
    def trade_document_attachment_simple_search(self, text):
        self.close_all_form()
        self.click_menu('Trade Finance', 'Document Attachment')
        self.wait_for_button_available('Search')
        self.assert_form_title('TRD-Document attachment-Search')
        self.simple_search(text)

    def trade_document_attachment_add(self, account_number, file_path, expire_date=None, document_description=None, import_date=None, last_update_date=None, document_type=None, document_name=None):
        # open form
        self.close_all_form()
        self.click_menu('Trade Finance', 'Document Attachment')
        self.wait_for_button_available('Add')
        self.assert_form_title('TRD-Document attachment-Search')
        self.click_button('Add')
        self.wait_for_button_available('Save')
        self.assert_form_title('TRD-Document attachment-Add')
        # choose file
        self.bo_choose_file(file_path)
        # enter value
        self.bo_set_value('Account number', account_number)
        if expire_date:
            self.bo_set_value('Expire Date', expire_date)
        if document_description:
            self.bo_set_text('Document description', document_description)
        self.click_button('Save')
        self.assert_button_disable('Save')
        self.assert_notification('Save successfully')
        account_number = self.bo_get_value_data('Account number')
        # search and verify
        self.trade_document_attachment_simple_search(str(account_number).replace('-', ''))
        self.assert_table_data('Account Number', 1, self.trade_account_number_mask(account_number))
        self.assert_table_data('Approve date', 1, ' ')
        self.assert_table_data('Status', 1, 'Pending Approve')
        if expire_date:
            self.assert_table_data('Expire date', 1, expire_date)
        if document_description:
            self.assert_table_data('Document description', 1, document_description)
        if import_date:
            self.assert_table_data('Import date', 1, import_date)
        if last_update_date:
            self.assert_table_data('Last update date', 1, last_update_date)
        if document_type:
            self.assert_table_data('Document type', 1, document_type)
        if document_name:
            self.assert_table_data('Document name', 1, document_name)
        print('Account number: ' + account_number)
        return account_number

    def trade_document_attachment_view(self, account_number, expire_date=None, document_description=None, status=None, approve_date=None, import_date=None, last_update_date=None, document_type=None, document_name=None):
        # search and verify trade document attachment
        self.trade_document_attachment_simple_search(str(account_number).replace('-', ''))
        self.assert_table_data('Account Number', 1, self.trade_account_number_mask(account_number))
        if approve_date:
            self.assert_table_data('Approve date', 1, approve_date)
        if status:
            self.assert_table_data('Status', 1, status)
        if expire_date:
            self.assert_table_data('Expire date', 1, expire_date)
        if document_description:
            self.assert_table_data('Document description', 1, document_description)
        if import_date:
            self.assert_table_data('Import date', 1, import_date)
        if last_update_date:
            self.assert_table_data('Last update date', 1, last_update_date)
        if document_type:
            self.assert_table_data('Document type', 1, document_type)
        if document_name:
            self.assert_table_data('Document name', 1, document_name)
        # view trade document attachment
        self.click_table_menu('View', 1)
        self.wait_for_button_available('Modify')
        self.assert_form_title('TRD-Document attachment-View')
        self.click_close_notification()
        # verify value tab 'General'
        self.bo_assert_value_data('Account number', self.trade_account_number_mask(account_number))
        if expire_date:
            self.bo_assert_value_data('Expire Date', expire_date)
        if document_description:
            self.bo_assert_text_data('Document description', document_description)

    def trade_document_attachment_update(self, account_number, expire_date=None, document_description=None, status=None, approve_date=None, import_date=None, last_update_date=None, document_type=None, document_name=None):
        self.trade_document_attachment_view(account_number)
        self.wait_loading()
        self.click_button('Modify')
        # update value tab 'General'
        if expire_date:
            self.bo_set_value('Expire Date', expire_date)
        if document_description:
            self.bo_set_text('Document description', document_description)
        # click 'Save'
        self.click_button('Save')
        self.assert_button_disable('Save')
        self.assert_notification('Save successfully')
        account_number = self.bo_get_value_data('Account number')
        # search and verify
        self.trade_document_attachment_simple_search(str(account_number).replace('-', ''))
        self.assert_table_data('Account Number', 1, self.trade_account_number_mask(account_number))
        if approve_date:
            self.assert_table_data('Approve date', 1, approve_date)
        if status:
            self.assert_table_data('Status', 1, status)
        if expire_date:
            self.assert_table_data('Expire date', 1, expire_date)
        if document_description:
            self.assert_table_data('Document description', 1, document_description)
        if import_date:
            self.assert_table_data('Import date', 1, import_date)
        if last_update_date:
            self.assert_table_data('Last update date', 1, last_update_date)
        if document_type:
            self.assert_table_data('Document type', 1, document_type)
        if document_name:
            self.assert_table_data('Document name', 1, document_name)
        print('Account number: ' + account_number)
        return account_number

    def trade_document_attachment_approve(self, account_number, expire_date=None, document_description=None, approve_date=None, import_date=None, last_update_date=None, document_type=None, document_name=None):
        self.trade_document_attachment_view(account_number)
        self.wait_loading()
        self.click_button('Approve')
        self.assert_button_disable('Approve')
        self.wait_loading()
        self.assert_notification('Approve successfully')
        account_number = self.bo_get_value_data('Account number')
        # search and verify
        self.trade_document_attachment_simple_search(str(account_number).replace('-', ''))
        self.assert_table_data('Account Number', 1, self.trade_account_number_mask(account_number))
        self.assert_table_data('Status', 1, 'Normal')
        if approve_date:
            self.assert_table_data('Approve date', 1, approve_date)
        if expire_date:
            self.assert_table_data('Expire date', 1, expire_date)
        if document_description:
            self.assert_table_data('Document description', 1, document_description)
        if import_date:
            self.assert_table_data('Import date', 1, import_date)
        if last_update_date:
            self.assert_table_data('Last update date', 1, last_update_date)
        if document_type:
            self.assert_table_data('Document type', 1, document_type)
        if document_name:
            self.assert_table_data('Document name', 1, document_name)
        print('Account number: ' + account_number)
        return account_number

# -------------------------- handle BO - CUSTOMER --------------------------
    # CTM-Customer Profile
    def customer_profile_simple_search(self, text):
        self.close_all_form()
        self.click_menu('Customer', 'Customer Profile')
        self.wait_for_button_available('Add')
        self.assert_form_title('CTM-Customer Profile-Search')
        self.simple_search(text)

    def customer_profile_add(self, business_line=None, full_name=None, home_01=None, street_01=None, ward_01=None, township_01=None, home_02=None, street_02=None, ward_02=None, township_02=None, name_01=None, account_no_01=None, name_02=None, account_no_02=None, mobile_phone=None, employer_name=None, gender=None, date_of_birth=None, nationality=None, paper_type=None, paper_number=None, resident_status=None, title=None, customer_type=None, customer_sub_type=None, first_name=None, last_name=None, father_name=None, title_of_organization=None, occupation=None, business_type=None, starting_date_of_company=None, place_of_birth=None, country_of_company=None, state_nrc=None, district_nrc=None, type_nrc=None, registration_no_nrc=None, tin_number=None, issue_date_of_paper=None, issue_place_of_paper=None, expire_date_of_paper=None, customer_segment=None, bank_identification=None, fdi_info=None, home_phone=None, email_address=None, education=None, marital_status=None, classification=None, staff_care=None, account_operations=None, country_of_income=None, account_owner_referral_rm=None, remark_field_to_add=None, income=None, position=None, credit_line=None, currency=None, mm_limit=None, currency_mm=None, fx_limit=None, currency_fx=None, suffix=None, reason_for_other_paper_type=None, economic_sector=None, group_sub_type=None, group_type=None, sub_economic_sector=None, reason_for_other_economic_sector=None, reason_for_other_sub_economic_sector=None, reason_for_other_occupation=None, reason_for_other_business_type=None, financial_institute=None, isic_code=None, province_01=None, province_02=None):
        # open form
        self.close_all_form()
        self.click_menu('Customer', 'Customer Profile')
        self.assert_form_title('CTM-Customer Profile-Search')
        self.click_button('Add')
        self.wait_for_button_available('Save')
        self.assert_form_title('CTM-Customer Profile-Add')
        # enter value tab 'General information'
        if business_line:
            self.bo_select('Business line', business_line)
        if title:
            self.bo_select('Title', title)
        if customer_type:
            self.bo_select('Customer type', customer_type)
        if customer_sub_type:
            self.bo_select('Customer sub type', customer_sub_type)
        if first_name:
            self.bo_write_text('First name (en)', first_name)
        if last_name:
            self.bo_write_text('Last name (en)', last_name)
        if father_name:
            self.bo_write_text('Father name', father_name)
        if title_of_organization:
            self.bo_select('Title of organization', title_of_organization)
        if first_name is None:
            self.bo_write_text('Full name', full_name)
        # self.assertEqual(self.bo_get_text('Full name'), full_name)
        if full_name:
            self.bo_assert_text('Full name', full_name)
        if gender:
            self.bo_select('Gender', gender)
        if date_of_birth:
            self.bo_write_date('Date of birth', date_of_birth)
        if starting_date_of_company:
            self.bo_write_date('Starting date of company', starting_date_of_company)
        if place_of_birth:
            self.bo_write_text('Place of birth', place_of_birth)
        if country_of_company:
            self.bo_select('Country of company', country_of_company)
        if suffix:
            self.bo_select('Suffix', suffix)
        if nationality:
            self.bo_select('Nationality', nationality)
        if paper_type:
            self.bo_select('Paper type', paper_type)
        if state_nrc:
            self.bo_select('State', state_nrc)
        if district_nrc:
            self.bo_select('District', district_nrc)
        if type_nrc:
            self.bo_select('Type', type_nrc)
        if registration_no_nrc:
            self.bo_write('Registration No', registration_no_nrc)
        if paper_number:
            self.bo_write_text('Paper number', paper_number, clear_text='Y')
        if tin_number:
            self.bo_write('TIN number', tin_number)
        if reason_for_other_paper_type:
            self.bo_write_text('Reason for Other (Paper type)', reason_for_other_paper_type)
        if issue_date_of_paper:
            self.bo_write_date('Issue date of paper', issue_date_of_paper)
        if issue_place_of_paper:
            self.bo_write_text('Issue place of paper', issue_place_of_paper)
        if expire_date_of_paper:
            self.bo_write_date('Expire date of paper', expire_date_of_paper)
        if economic_sector:
            self.bo_select('Economic sector', economic_sector)
        if group_sub_type:
            self.bo_select('Group sub type', group_sub_type)
        if group_type:
            self.bo_select('Group type', group_type)
        if sub_economic_sector:
            self.bo_select('Sub economic sector', sub_economic_sector)
        if bank_identification:
            self.bo_select('Bank Identification', bank_identification)
        if resident_status:
            self.bo_select('Resident status', resident_status)
        if customer_segment:
            self.bo_select('Customer segment', customer_segment)
        if fdi_info:
            self.bo_write_text('FDI info', fdi_info)
        if reason_for_other_economic_sector:
            self.bo_write_text('Reason for Other (Economic sector)', reason_for_other_economic_sector)
        if reason_for_other_sub_economic_sector:
            self.bo_write_text('Reason for Other (Sub economic sector)', reason_for_other_sub_economic_sector)
        if home_01:
            self.bo_write_text_multi('Legal address', 'Home', home_01)
        if street_01:
            self.bo_write_text_multi('Legal address', 'Street', street_01)
        if ward_01:
            self.bo_write_text_multi('Legal address', 'Ward', ward_01)
        if township_01:
            self.bo_write_text_multi('Legal address', 'Township', township_01)
        if province_01:
            self.bo_write_text_multi('Legal address', 'Province', province_01)
        if home_02:
            self.bo_write_text_multi('Contact local address', 'Home', home_02)
        if street_02:
            self.bo_write_text_multi('Contact local address', 'Street', street_02)
        if ward_02:
            self.bo_write_text_multi('Contact local address', 'Ward', ward_02)
        if township_02:
            self.bo_write_text_multi('Contact local address', 'Township', township_02)
        if province_02:
            self.bo_write_text_multi('Contact local address', 'Province', province_02)
        if name_01:
            self.bo_write_text_multi('Introducer 1', 'Name', name_01)
        if account_no_01:
            self.bo_write_multi('Introducer 1', 'Account No', account_no_01)
        if name_02:
            self.bo_write_text_multi('Introducer 2', 'Name', name_02)
        if account_no_02:
            self.bo_write_multi('Introducer 2', 'Account No', account_no_02)
        if home_phone:
            self.bo_write_text('Home phone', home_phone)
        if mobile_phone:
            self.bo_write_text('Mobile phone', mobile_phone)
        if occupation:
            self.bo_select('Occupation', occupation)
        if employer_name:
            self.bo_write_text('Employer Name', employer_name)
        if business_type:
            self.bo_select('Business Type', business_type)
        if marital_status:
            self.bo_select('Marital status', marital_status)
        if education:
            self.bo_select('Education', education)
        if email_address:
            self.bo_write('Email address', email_address)
        if reason_for_other_occupation:
            self.bo_write_text('Reason for Other (Occupation)', reason_for_other_occupation)
        if reason_for_other_business_type:
            self.bo_write_text('Reason for Other (Business Type)', reason_for_other_business_type)
        if isic_code:
            self.bo_write_group('ISIC Code', isic_code)
        if financial_institute:
            self.bo_select('Financial Institute', financial_institute)
        # enter value tab 'Other information'
        self.bo_click_tab('Other information')
        if classification:
            self.bo_select('Classification', classification)
        if staff_care:
            self.bo_select('Staff care', staff_care)
        if account_operations:
            self.bo_select('Account Operations', account_operations)
        if country_of_income:
            self.bo_select('Country of Income', country_of_income)
        if account_owner_referral_rm:
            self.bo_select('Account Owner/Referral/RM', account_owner_referral_rm)
        if remark_field_to_add:
            self.bo_write_text('Remark field to add', remark_field_to_add)
        if income:
            self.bo_select('Income', income)
        if position:
            self.bo_write_text('Position ', position)
        # enter value tab 'Credit line information'
        self.bo_click_tab('Credit line information')
        if currency_fx:
            self.bo_select_group('Currency FX', currency_fx)
        if fx_limit:
            self.bo_write_number_group('FX limit', str(fx_limit).replace(',', ''))
        if currency_mm:
            self.bo_select_group('Currency MM', currency_mm)
        if mm_limit:
            self.bo_write_number_group('MM limit', str(mm_limit).replace(',', ''))
        if currency:
            self.bo_select_group('Currency', currency)
        if credit_line:
            self.bo_write_number_group('Credit line', str(credit_line).replace(',', ''))
        self.click_button('Save')
        self.assert_button_disable('Save')
        self.assert_notification('Save successfully')
        # back to tab 'General information'
        self.bo_click_tab('General information')
        customer_code = self.bo_get_value('Customer code')
        print('Customer code: ' + customer_code)
        return customer_code

    def customer_profile_view(self, customer_code_mask, business_line=None, full_name=None, home_01=None, street_01=None, ward_01=None, township_01=None, home_02=None, street_02=None, ward_02=None, township_02=None, name_01=None, account_no_01=None, name_02=None, account_no_02=None, mobile_phone=None, employer_name=None, gender=None, date_of_birth_starting_date_of_company=None, nationality=None, paper_type=None, paper_number=None, resident_status=None, title=None, customer_type=None, customer_sub_type=None, first_name=None, last_name=None, father_name=None, title_of_organization=None, occupation=None, business_type=None, starting_date_of_company=None, place_of_birth=None, country_of_company=None, tin_number=None, issue_date_of_paper=None, issue_place_of_paper=None, expire_date_of_paper=None, customer_segment=None, bank_identification=None, fdi_info=None, home_phone=None, email_address=None, education=None, marital_status=None, classification=None, staff_care=None, account_operations=None, country_of_income=None, account_owner_referral_rm=None, remark_field_to_add=None, income=None, position=None, credit_line=None, currency=None, mm_limit=None, currency_mm=None, fx_limit=None, currency_fx=None, suffix=None, reason_for_other_paper_type=None, economic_sector=None, group_sub_type=None, group_type=None, sub_economic_sector=None, reason_for_other_economic_sector=None, reason_for_other_sub_economic_sector=None, reason_for_other_occupation=None, reason_for_other_business_type=None, financial_institute=None, isic_code=None, province_01=None, province_02=None):
        # search customer profile
        self.customer_profile_simple_search(str(customer_code_mask).replace('-', ''))
        self.assert_table_data('Customer code', 1, customer_code_mask)
        # view customer profile
        self.click_table_menu('View', 1)
        self.wait_for_button_available('Modify')
        self.assert_form_title('CTM-Customer Profile-View')
        # verify value tab 'General information'
        self.bo_assert_value('Customer code', customer_code_mask)
        if business_line:
            self.bo_assert_select('Business line', business_line)
        if title:
            self.bo_assert_select('Title', title)
        if customer_type:
            self.bo_assert_select('Customer type', customer_type)
        if customer_sub_type:
            self.bo_assert_select('Customer sub type', customer_sub_type)
        if first_name:
            self.bo_assert_text('First name (en)', first_name)
        if last_name:
            self.bo_assert_text('Last name (en)', last_name)
        if full_name:
            self.bo_assert_text('Full name', full_name)
        if father_name:
            self.bo_assert_text('Father name', father_name)
        if gender:
            self.bo_assert_select('Gender', gender)
        if date_of_birth_starting_date_of_company:
            self.bo_assert_date('Date of birth/Starting date of company', date_of_birth_starting_date_of_company)
        if place_of_birth:
            self.bo_assert_text('Place of birth', place_of_birth)
        if nationality:
            self.bo_assert_select('Nationality', nationality)
        if paper_type:
            self.bo_assert_select('Paper type', paper_type)
        if paper_number:
            self.bo_assert_text('Paper number', paper_number)
        if tin_number:
            self.bo_assert_value('TIN number', tin_number)
        if issue_date_of_paper:
            self.bo_assert_date('Issue date of paper', issue_date_of_paper)
        if issue_place_of_paper:
            self.bo_assert_text('Issue place of paper', issue_place_of_paper)
        if expire_date_of_paper:
            self.bo_assert_date('Expire date of paper', expire_date_of_paper)
        if customer_segment:
            self.bo_assert_select('Customer segment', customer_segment)
        if resident_status:
            self.bo_assert_select('Resident status', resident_status)
        if bank_identification:
            self.bo_assert_select('Bank Identification', bank_identification)
        if fdi_info:
            self.bo_assert_text('FDI info', fdi_info)
        # verify value tab 'Other information'
        self.bo_click_tab('Other information')
        # verify value tab 'Credit line information'
        self.bo_click_tab('Credit line information')
        # back to tab 'General information'
        self.bo_click_tab('General information')

    def customer_profile_update(self, customer_code_mask, full_name=None, home_01=None, street_01=None, ward_01=None, township_01=None, home_02=None, street_02=None, ward_02=None, township_02=None, name_01=None, account_no_01=None, name_02=None, account_no_02=None, mobile_phone=None, employer_name=None, gender=None, nationality=None, paper_type=None, paper_number=None, resident_status=None, title=None, customer_sub_type=None, first_name=None, last_name=None, father_name=None, title_of_organization=None, occupation=None, business_type=None, date_of_birth_starting_date_of_company=None, place_of_birth=None, country_of_company=None, tin_number=None, issue_date_of_paper=None, issue_place_of_paper=None, expire_date_of_paper=None, customer_segment=None, bank_identification=None, fdi_info=None, home_phone=None, email_address=None, education=None, marital_status=None, classification=None, staff_care=None, account_operations=None, country_of_income=None, account_owner_referral_rm=None, remark_field_to_add=None, income=None, position=None, credit_line=None, currency=None, mm_limit=None, currency_mm=None, fx_limit=None, currency_fx=None, suffix=None, reason_for_other_paper_type=None, economic_sector=None, group_sub_type=None, group_type=None, sub_economic_sector=None, reason_for_other_economic_sector=None, reason_for_other_sub_economic_sector=None, reason_for_other_occupation=None, reason_for_other_business_type=None, financial_institute=None, isic_code=None, province_01=None, province_02=None):
        # search customer profile
        self.customer_profile_simple_search(str(customer_code_mask).replace('-', ''))
        self.assert_table_data('Customer code', 1, customer_code_mask)
        # view customer profile
        self.click_table_menu('View', 1)
        self.wait_for_button_available('Modify')
        self.assert_form_title('CTM-Customer Profile-View')
        self.bo_click_tab('General information')
        self.click_button('Modify')
        # update value tab 'General information'
        if title:
            self.bo_select('Title', title)
        if customer_sub_type:
            self.bo_select('Customer sub type', customer_sub_type)
        if self.bo_get_select('Business line') == 'Personal':
            if first_name:
                self.bo_write_text('First name (en)', first_name)
            if last_name:
                self.bo_write_text('Last name (en)', last_name)
            if father_name:
                self.bo_write_text('Father name', father_name)
            if full_name:
                self.bo_assert_text('Full name', full_name)
        if self.bo_get_select('Business line') != 'Personal':
            if full_name:
                self.bo_write_text('Full name', full_name)
        if title_of_organization:
            self.bo_select('Title of organization', title_of_organization)
        if gender:
            self.bo_select('Gender', gender)
        if date_of_birth_starting_date_of_company:
            self.bo_write_date('Date of birth/Starting date of company', date_of_birth_starting_date_of_company)
        if place_of_birth:
            self.bo_write_text('Place of birth', place_of_birth)
        if country_of_company:
            self.bo_select('Country of company', country_of_company)
        if suffix:
            self.bo_select('Suffix', suffix)
        if nationality:
            self.bo_select('Nationality', nationality)
        if paper_type:
            self.bo_select('Paper type', paper_type)
        if paper_number:
            self.bo_write_text('Paper number', paper_number)
        if tin_number:
            self.bo_write('TIN number', tin_number)
        if reason_for_other_paper_type:
            self.bo_write_text('Reason for Other (Paper type)', reason_for_other_paper_type)
        if issue_date_of_paper:
            self.bo_write_date('Issue date of paper', issue_date_of_paper)
        if issue_place_of_paper:
            self.bo_write_text('Issue place of paper', issue_place_of_paper)
        if expire_date_of_paper:
            self.bo_write_date('Expire date of paper', expire_date_of_paper)
        if economic_sector:
            self.bo_select('Economic sector', economic_sector)
        if group_sub_type:
            self.bo_select('Group sub type', group_sub_type)
        if group_type:
            self.bo_select('Group type', group_type)
        if sub_economic_sector:
            self.bo_select('Sub economic sector', sub_economic_sector)
        if bank_identification:
            self.bo_select('Bank Identification', bank_identification)
        if resident_status:
            self.bo_select('Resident status', resident_status)
        if customer_segment:
            self.bo_select('Customer segment', customer_segment)
        if fdi_info:
            self.bo_write_text('FDI info', fdi_info)
        if reason_for_other_economic_sector:
            self.bo_write_text('Reason for Other (Economic sector)', reason_for_other_economic_sector)
        if reason_for_other_sub_economic_sector:
            self.bo_write_text('Reason for Other (Sub economic sector)', reason_for_other_sub_economic_sector)
        if home_01:
            self.bo_write_text_multi('Legal address', 'Home', home_01)
        if street_01:
            self.bo_write_text_multi('Legal address', 'Street', street_01)
        if ward_01:
            self.bo_write_text_multi('Legal address', 'Ward', ward_01)
        if township_01:
            self.bo_write_text_multi('Legal address', 'Township', township_01)
        if province_01:
            self.bo_write_text_multi('Legal address', 'Province', province_01)
        if home_02:
            self.bo_write_text_multi('Contact local address', 'Home', home_02)
        if street_02:
            self.bo_write_text_multi('Contact local address', 'Street', street_02)
        if ward_02:
            self.bo_write_text_multi('Contact local address', 'Ward', ward_02)
        if township_02:
            self.bo_write_text_multi('Contact local address', 'Township', township_02)
        if province_02:
            self.bo_write_text_multi('Contact local address', 'Province', province_02)
        if name_01:
            self.bo_write_text_multi('Introducer 1', 'Name', name_01)
        if account_no_01:
            self.bo_write_multi('Introducer 1', 'Account No', account_no_01)
        if name_02:
            self.bo_write_text_multi('Introducer 2', 'Name', name_02)
        if account_no_02:
            self.bo_write_multi('Introducer 2', 'Account No', account_no_02)
        if home_phone:
            self.bo_write_text('Home phone', home_phone)
        if mobile_phone:
            self.bo_write_text('Mobile phone', mobile_phone)
        if occupation:
            self.bo_select('Occupation', occupation)
        if employer_name:
            self.bo_write_text('Employer Name', employer_name)
        if business_type:
            self.bo_select('Business Type', business_type)
        if marital_status:
            self.bo_select('Marital status', marital_status)
        if education:
            self.bo_select('Education', education)
        if email_address:
            self.bo_write('Email address', email_address)
        if reason_for_other_occupation:
            self.bo_write_text('Reason for Other (Occupation)', reason_for_other_occupation)
        if reason_for_other_business_type:
            self.bo_write_text('Reason for Other (Business Type)', reason_for_other_business_type)
        if isic_code:
            self.bo_write_group('ISIC Code', isic_code)
        if financial_institute:
            self.bo_select('Financial Institute', financial_institute)
        # enter value tab 'Other information'
        self.bo_click_tab('Other information')
        if classification:
            self.bo_select('Classification', classification)
        if account_operations:
            self.bo_select('Account Operations', account_operations)
        if country_of_income:
            self.bo_select('Country of Income', country_of_income)
        if account_owner_referral_rm:
            self.bo_select('Account Owner/Referral/RM', account_owner_referral_rm)
        if remark_field_to_add:
            self.bo_write_text('Remark field to add', remark_field_to_add)
        if income:
            self.bo_select('Income', income)
        if position:
            self.bo_write_text('Position', position)
        # enter value tab 'Credit line information'
        self.bo_click_tab('Credit line information')
        if currency_fx:
            self.bo_select_group('Currency FX ', currency_fx)
        if fx_limit:
            self.bo_write_number_group('FX limit', str(fx_limit).replace(',', ''))
        if currency_mm:
            self.bo_select_group('Currency MM', currency_mm)
        if mm_limit:
            self.bo_write_number_group('MM limit ', str(mm_limit).replace(',', ''))
        if currency:
            self.bo_select_group('Currency', currency)
        if credit_line:
            self.bo_write_number_group('Credit line', str(credit_line).replace(',', ''))
        self.click_button('Save')
        self.assert_button_disable('Save')
        self.assert_notification('Save successfully')
        # back to tab 'General information'
        self.bo_click_tab('General information')
        customer_code = self.bo_get_value('Customer code')
        print('Customer code: ' + customer_code)
        return customer_code

    def check_customer_profile_not_exist(self, customer_code):
        customer_code = str(customer_code).replace('-', '')
        # search customer code
        self.customer_profile_simple_search(customer_code)
        if (self.get_text_notification(timeout=3) == 'Data not found'):
            print(f"Customer code '{customer_code}' does NOT exist.")
            return True
        else:
            print(f"Customer code '{customer_code}' already exists.")
            return False

    # CTM-Approve Profile Modification
    def customer_profile_modify_search(self, text):
        self.close_all_form()
        self.click_menu('Customer', 'Approve Modify Customer')
        self.wait_for_button_available('Search')
        self.assert_form_title('CTM-Approve Profile Modification-Search')
        self.simple_search(text)

    def customer_profile_modify_view(self, customer_code_mask):
        # search customer profile modify
        self.customer_profile_modify_search(str(customer_code_mask).replace('-', ''))
        self.assert_table_data('Customer code', 1, customer_code_mask)
        # view customer profile modify
        self.click_table_menu(row=1)
        self.wait_for_button_available('View Modification')
        self.assert_form_title('CTM-Approve Profile Modification-View')
        # verify value tab 'General information'
        self.bo_assert_value('Customer code', customer_code_mask)

    def customer_profile_modify_approve(self, customer_code_mask):
        self.customer_profile_modify_view(customer_code_mask)
        self.click_button('View Modification')
        self.wait_loading()
        self.click_button('Approve')
        self.wait_loading()
        self.assert_notification('Approve successfully')
        # back to tab 'General information'
        self.bo_click_tab('General information')
        customer_code = self.bo_get_value('Customer code')
        print('Customer code: ' + customer_code)
        self.customer_profile_modify_search(str(customer_code_mask).replace('-', ''))
        self.assert_search_not_found()
        return customer_code

    def customer_profile_modify_reject(self, customer_code_mask):
        self.customer_profile_modify_view(customer_code_mask)
        self.click_button('View Modification')
        self.wait_loading()
        self.click_button('Reject')
        self.wait_loading()
        self.assert_notification('Reject successfully')
        # back to tab 'General information'
        self.bo_click_tab('General information')
        customer_code = self.bo_get_value('Customer code')
        print('Customer code: ' + customer_code)
        self.customer_profile_modify_search(str(customer_code_mask).replace('-', ''))
        self.assert_search_not_found()
        return customer_code

    # CTM-Customer Linkage
    def customer_linkage_search(self, text):
        self.close_all_form()
        self.click_menu('Customer', 'Customer Linkage')
        self.wait_for_button_available('Search')
        self.assert_form_title('CTM-Customer Linkage-Search')
        self.simple_search(text, placeholder='Search Text')

    def customer_linkage_view(self, customer_code_mask, linkage_status=None, linkage_description=None):
        # search customer linkage
        self.customer_linkage_search(str(customer_code_mask).replace('-', ''))
        self.assert_table_data('Master Customer Code', 1, customer_code_mask)
        # view customer linkage
        self.click_table_menu(row=1)
        self.wait_for_button_available('Modify')
        self.assert_form_title('CTM-Customer Linkage-View')
        # verify value tab 'General Information'
        self.bo_assert_value_group('Master Customer Code', customer_code_mask)
        if linkage_status:
            self.bo_assert_select('Linkage status', linkage_status)
        if linkage_description:
            self.bo_assert_select('Linkage description', linkage_description)

    def customer_linkage_update(self, customer_code_mask, linkage_description=None, detail_customer_code=None, linkage_type=None):
        self.customer_linkage_view(customer_code_mask)
        self.click_button('Modify')
        self.wait_loading()
        if detail_customer_code:
            self.click_button('Add')
            self.bo_write_data('Detail customer code', detail_customer_code)
            # self.key_escape()
            if linkage_type:
                self.bo_select_data('Linkage type', linkage_type)
            self.click_button('Apply')
        if linkage_description:
            self.bo_select('Linkage description', linkage_description)
        self.click_button('Save')
        self.assert_button_disable('Save')
        self.assert_notification('Saved successfully!')
        # back to tab 'General information'
        self.bo_click_tab('General Information')
        customer_code = self.bo_get_value_group('Master Customer Code')
        print('Customer code: ' + customer_code)
        return customer_code

    # CTM-Approve Customer Linkage Modify
    def customer_linkage_modify_search(self, text):
        self.close_all_form()
        self.click_menu('Customer', 'Approve Modify Customer Linkage')
        self.wait_for_button_available('Search')
        self.assert_form_title('CTM-Approve Customer Linkage Modify-Search')
        self.simple_search(text, placeholder='Search Text')

    def customer_linkage_modify_view(self, customer_code_mask):
        # search customer linkage modify
        self.customer_linkage_modify_search(str(customer_code_mask).replace('-', ''))
        self.assert_table_data('Master Customer Code', 1, customer_code_mask)
        # view customer linkage modify
        self.click_table_menu(row=1)
        self.wait_for_button_available('View Modification')
        self.assert_form_title('CTM-Approve Customer Linkage Modify-View')
        # verify value tab 'General information'
        self.bo_assert_value_group('Master Customer Code', customer_code_mask)

    def customer_linkage_modify_approve(self, customer_code_mask):
        self.customer_linkage_modify_view(customer_code_mask)
        self.click_button('View Modification')
        self.wait_loading()
        self.click_button('Approve')
        self.wait_loading()
        self.assert_notification('Approve successfully')
        # back to tab 'General Information'
        self.bo_click_tab('General Information')
        customer_code = self.bo_get_value_group('Master Customer Code')
        print('Customer code: ' + customer_code)
        self.customer_linkage_modify_search(str(customer_code_mask).replace('-', ''))
        self.assert_search_not_found()
        return customer_code

    def customer_linkage_modify_reject(self, customer_code_mask):
        self.customer_linkage_modify_view(customer_code_mask)
        self.click_button('View Modification')
        self.wait_loading()
        self.click_button('Reject')
        self.wait_loading()
        self.assert_notification('Reject successfully')
        # back to tab 'General Information'
        self.bo_click_tab('General Information')
        customer_code = self.bo_get_value_group('Master Customer Code')
        print('Customer code: ' + customer_code)
        self.customer_linkage_modify_search(str(customer_code_mask).replace('-', ''))
        self.assert_search_not_found()
        return customer_code

    # CTM-Customer relation management (Customer Group)
    def customer_group_search(self, text):
        self.close_all_form()
        self.click_menu('Customer', 'Customer Group')
        self.wait_for_button_available('Search')
        self.assert_form_title('CTM-Customer relation management-Search')
        self.simple_search(text, placeholder='Search Text')

    def customer_group_view(self, customer_code_mask, group_status=None):
        # search customer group
        self.customer_group_search(str(customer_code_mask).replace('-', ''))
        self.assert_table_data('Mater customer code', 1, customer_code_mask)
        # view customer group
        self.click_table_menu(row=1)
        self.wait_for_button_available('Modify')
        self.assert_form_title('CTM-Customer relation management-View')
        # verify value tab 'General Information'
        self.bo_assert_value('Master customer', customer_code_mask)
        if group_status:
            self.bo_assert_select('Group status', group_status)

    def customer_group_update(self, customer_code_mask, customer_code=None, position=None):
        self.customer_group_view(customer_code_mask)
        self.click_button('Modify')
        self.wait_loading()
        if customer_code:
            self.click_button('Add')
            self.bo_write_data('Customer code', customer_code)
            if position:
                self.bo_write_text_data('Position', position)
            self.click_button('Apply')
        self.wait_loading()
        self.click_button('Save')
        self.assert_button_disable('Save')
        self.assert_notification('Saved successfully!')
        # back to tab 'General information'
        self.bo_click_tab('General Information')
        customer_code = self.bo_get_value('Master customer')
        print('Customer code: ' + customer_code)
        return customer_code

    # CTM-Approve Customer relation management Modify
    def customer_group_modify_search(self, text):
        self.close_all_form()
        self.click_menu('Customer', 'Approve Modify Customer Group')
        self.wait_for_button_available('Search')
        self.assert_form_title('CTM-Approve Customer relation management Modify-Search')
        self.simple_search(text, placeholder='Search Text')

    def customer_group_modify_view(self, customer_code_mask):
        # search customer group modify
        self.customer_group_modify_search(str(customer_code_mask).replace('-', ''))
        self.assert_table_data('Mater customer code', 1, customer_code_mask)
        # view customer group modify
        self.click_table_menu(row=1)
        self.wait_for_button_available('View Modification')
        self.assert_form_title('CTM-Approve Customer relation management Modify-View')
        # verify value tab 'General Information'
        self.bo_assert_value('Master customer', customer_code_mask)

    def customer_group_modify_approve(self, customer_code_mask):
        self.customer_group_modify_view(customer_code_mask)
        self.click_button('View Modification')
        self.wait_loading()
        self.click_button('Approve')
        self.wait_loading()
        self.assert_notification('Approve successfully')
        # back to tab 'General Information'
        self.bo_click_tab('General Information')
        customer_code = self.bo_get_value('Master customer')
        print('Customer code: ' + customer_code)
        self.customer_group_modify_search(str(customer_code_mask).replace('-', ''))
        self.assert_search_not_found()
        return customer_code

    def customer_group_modify_reject(self, customer_code_mask):
        self.customer_group_modify_view(customer_code_mask)
        self.click_button('View Modification')
        self.wait_loading()
        self.click_button('Reject')
        self.wait_loading()
        self.assert_notification('Reject successfully')
        # back to tab 'General Information'
        self.bo_click_tab('General Information')
        customer_code = self.bo_get_value('Master customer')
        print('Customer code: ' + customer_code)
        self.customer_group_modify_search(str(customer_code_mask).replace('-', ''))
        self.assert_search_not_found()
        return customer_code

# -------------------------- handle BO - DEPOSIT --------------------------
    # DPT-Catalogue Definition
    def deposit_catalogue_simple_search(self, text):
        self.close_all_form()
        self.click_menu('Deposit', 'Catalogue Definition')
        self.wait_for_button_available('Search')
        self.assert_form_title('DPT-Catalogue Definition-Search')
        self.simple_search(text)
        self.wait_loading()

    def deposit_catalogue_add(self, catalogue_code=None, name=None, currency_code=None, deposit_type=None, deposit_sub_type=None, deposit_purpose=None, deposit_classification=None, passbook_or_statement_or_receipt=None, minimum_deposit_amount=None, catalogue_status=None, interest_payment_restrictions=None, debit_accounting=False, debit_cash=False, debit_deposit=False, credit_accounting=False, credit_cash=False, credit_deposit=False, tenor_1=None, tenor_unit_1=None, tenor_2=None, tenor_unit_2=None, deposit_tenor=None, deposit_tenor_unit=None, interest_tenor=None, interest_tenor_unit=None, minimum_tenor=None, minimum_tenor_unit=None, multiple_deposit_allow=None, multiple_withdrawal_allow=None, early_withdrawal=None, minimum_tenor_allow_early_withdrawal=None, minimum_tenor_allow_early_withdrawal_unit=None, credit_interest_yn=None, credit_interest_tenor=None, credit_interest_tenor_unit=None, the_day_of_tenor_for_crediting_interest=None, minimum_dormant_amount=None, dormant_period=None, type_of_dormant_period=None, rollover_option=None, rollover_to_catalogue=None, initial_deposit_amount=None, ifc_codes=None, sys_account_names=None, coa_accounts=None, account_aliass=None, replace_code=None, replace_bys=None, system_account_names=None, customer_sectors=None, customer_resident_statuss=None, business_lines=None, sub_products=None, bank_identifications=None, list_error_message=None):
        # open form
        self.close_all_form()
        self.click_menu('Deposit', 'Catalogue Definition')
        self.wait_for_button_available('Add')
        self.assert_form_title('DPT-Catalogue Definition-Search')
        self.click_button('Add')
        self.wait_for_button_available('Save')
        self.assert_form_title('DPT-Catalogue Definition-Add')
        # enter value
        self.bo_click_tab('General information')
        if catalogue_code:
            self.bo_write('Catalogue code', catalogue_code)
        if name:
            self.bo_write_text('Name', name)
        if currency_code:
            self.bo_select('Currency code', currency_code)
        if deposit_type:
            self.bo_select('Deposit type', deposit_type)
        if deposit_sub_type:
            self.bo_select('Deposit sub type', deposit_sub_type)
        if deposit_purpose:
            self.bo_select('Deposit purpose', deposit_purpose)
        if deposit_classification:
            self.bo_select('Deposit classification', deposit_classification)
        if passbook_or_statement_or_receipt:
            self.bo_select('Passbook or statement or receipt', passbook_or_statement_or_receipt)
        if minimum_deposit_amount:
            self.bo_write_number('Minimum deposit amount', minimum_deposit_amount)
        if catalogue_status:
            self.bo_select('Catalogue status', catalogue_status)
        if interest_payment_restrictions:
            self.bo_select_multi('Interest payment restriction', interest_payment_restrictions)
        collap_debit = 'Debit With'
        self.bo_click_collap(collap_debit)
        if debit_accounting:
            self.click_checkbox_in_multi(collap_debit, 'Accounting')
        if debit_cash:
            self.click_checkbox_in_multi(collap_debit, 'Cash')
        if debit_deposit:
            self.click_checkbox_in_multi(collap_debit, 'Deposit')
        collap_credit = 'Credit With'
        self.bo_click_collap(collap_credit)
        if credit_accounting:
            self.click_checkbox_in_multi(collap_credit, 'Accounting')
        if credit_cash:
            self.click_checkbox_in_multi(collap_credit, 'Cash')
        if credit_deposit:
            self.click_checkbox_in_multi(collap_credit, 'Deposit')
        self.bo_click_tab('Tenor and relative information')
        if tenor_1:
            self.bo_write_group('Tenor 1', tenor_1)
        if tenor_unit_1:
            self.bo_select_group('Tenor unit 1', tenor_unit_1)
        if tenor_2:
            self.bo_write_group('Tenor 2', tenor_2)
        if tenor_unit_2:
            self.bo_select_group('Tenor unit 2', tenor_unit_2)
        if deposit_tenor:
            self.bo_write_group('Deposit tenor', deposit_tenor)
        if deposit_tenor_unit:
            self.bo_select_group('Deposit tenor unit', deposit_tenor_unit)
        if interest_tenor:
            self.bo_write('Interest tenor', interest_tenor)
        if interest_tenor_unit:
            self.bo_select('Interest tenor unit', interest_tenor_unit)
        if minimum_tenor:
            self.bo_write_group('Minimum tenor', minimum_tenor)
        if minimum_tenor_unit:
            self.bo_select_group('Minimum tenor unit', minimum_tenor_unit)
        if multiple_deposit_allow:
            self.bo_select('Multiple deposit allow', multiple_deposit_allow)
        if multiple_withdrawal_allow:
            self.bo_select('Multiple withdrawal allow', multiple_withdrawal_allow)
        if early_withdrawal:
            self.bo_select('Early withdrawal', early_withdrawal)
        if minimum_tenor_allow_early_withdrawal:
            self.bo_write_group('Minimum tenor allow early withdrawal', minimum_tenor_allow_early_withdrawal)
        if minimum_tenor_allow_early_withdrawal_unit:
            self.bo_select_group('Minimum tenor allow early withdrawal unit', minimum_tenor_allow_early_withdrawal_unit)
        if credit_interest_yn:
            self.bo_select('Credit interest (Y/N)', credit_interest_yn)
        if credit_interest_tenor:
            self.bo_write_group('Credit interest tenor', credit_interest_tenor)
        if credit_interest_tenor_unit:
            self.bo_select_group('Credit interest tenor unit', credit_interest_tenor_unit)
        if the_day_of_tenor_for_crediting_interest:
            self.bo_write('The day of tenor for crediting interest', the_day_of_tenor_for_crediting_interest)
        if minimum_dormant_amount:
            self.bo_write_number('Minimum Dormant amount', minimum_dormant_amount)
        if dormant_period:
            self.bo_write_group('Dormant period', dormant_period)
        if type_of_dormant_period:
            self.bo_select_group('Type of dormant period', type_of_dormant_period)
        if rollover_option:
            self.bo_select('Rollover option', rollover_option)
        if rollover_to_catalogue:
            self.lookup_data('Rollover to catalogue', 'Code', rollover_to_catalogue)
        if initial_deposit_amount:
            self.bo_write_number('Initial deposit amount', initial_deposit_amount)
        self.bo_click_tab('IFC information ')
        if ifc_codes:
            for ifc_code in ifc_codes:
                self.click_button_in_tab('Add')
                self.select('IFC Code', ifc_code)
                self.click_button_in_tab('Apply')
        self.bo_click_tab('GLs information ')
        if sys_account_names:
            count = len(sys_account_names)
            if not all(
                len(lst) == count for lst in [
                    account_aliass,
                    coa_accounts if coa_accounts else [None] * count
                ]
            ):
                raise ValueError("All input lists must have the same length or be None.")
            for i in range(count):
                self.add_gls_entry(i, sys_account_names, account_aliass, coa_accounts)
        self.bo_click_tab('Extension Group of Account Information')
        if replace_bys:
            count = len(replace_bys)
            if not all(
                len(lst) == count for lst in [
                    system_account_names, business_lines,
                    customer_sectors or [None] * count,
                    customer_resident_statuss or [None] * count,
                    sub_products or [None] * count,
                    bank_identifications or [None] * count
                ]
            ):
                raise ValueError("All input lists must have the same length or be None.")
            for i in range(count):
                self.add_extension_group_entry(
                    i,
                    replace_bys,
                    system_account_names,
                    business_lines,
                    customer_sectors,
                    customer_resident_statuss,
                    sub_products,
                    bank_identifications,
                    replace_code
                )
        # click 'Save'
        self.click_button('Save')
        if list_error_message:
        # verify error
            self.assert_error_message()
            self.assert_list_error_message(list_error_message)
            print(f'Add catalogue code: {catalogue_code} failed!')
        else:
            # verify success
            self.assert_button_disable('Save')
            self.assert_notification('Saved successfully!')        
            self.bo_click_tab('General information')
            catalogue_code = self.bo_get_value('Catalogue code')
            print('Catalogue code: ' + catalogue_code)
            # search and verify
            self.deposit_catalogue_simple_search(catalogue_code)
            if catalogue_code:
                self.assert_table_data('Catalogue code', 1, catalogue_code)
            if name:
                self.assert_table_data('Catalogue name', 1, name)
            if currency_code:
                self.assert_table_data('Currency code', 1, currency_code)
            if deposit_type:
                self.assert_table_data('Deposit type', 1, deposit_type)
            if passbook_or_statement_or_receipt:
                self.assert_table_data('Passbook or statement', 1, passbook_or_statement_or_receipt)
            if tenor_1:
                self.assert_table_data('Tenor', 1, tenor_1)
            if tenor_unit_1:
                self.assert_table_data('Tenor unit', 1, tenor_unit_1)
            if catalogue_status:
                self.assert_table_data('Status', 1, catalogue_status)
            return catalogue_code

    def deposit_catalogue_view(self, catalogue_code, catalogue_name=None, interest_payment_restrictions=None, expected_ifc_list_codes=None, expected_ifc_names=None, expected_ifc_values=None, expected_ifc_types=None, expected_ifc_tenors=None, expected_ifc_tenor_units=None, expected_ifc_statuss=None, expected_gls_sys_account_names=None, expected_gls_account_aliass=None, expected_extension_sys_account_names=None, expected_extension_conditions=None, expected_extension_replace_bys=None):
        # search
        self.deposit_catalogue_simple_search(catalogue_code)
        if catalogue_code:
            self.assert_table_data('Catalogue code', 1, catalogue_code)
        # view
        self.click_table_menu('View', 1)
        self.wait_for_button_available('Modify')
        self.assert_form_title('DPT-Catalogue Definition-View')
        # verify value tab 'General information'
        self.bo_click_tab('General information')
        self.bo_assert_value('Catalogue code', catalogue_code)
        if interest_payment_restrictions:
            self.bo_assert_select_multi('Interest payment restriction', interest_payment_restrictions)
        if catalogue_name:
            self.bo_assert_text('Name', catalogue_name)
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
        print('View catalogue code: ' + catalogue_code)
        return catalogue_code

    def deposit_catalogue_update(self, catalogue_code, catalogue_name=None, list_error_message=None):
        self.deposit_catalogue_view(catalogue_code)
        self.wait_loading()
        self.click_button('Modify')
        # update value
        self.bo_click_tab('General information')
        if catalogue_name or catalogue_name == '':
            self.bo_write_text('Name', catalogue_name)
        # click 'Save'
        self.click_button('Save')
        if list_error_message:
        # verify error
            self.assert_error_message()
            self.assert_list_error_message(list_error_message)
            print(f'Update catalogue code: {catalogue_code} failed!')
        else:
            # verify success
            self.assert_button_disable('Save')
            self.assert_notification('Saved successfully!')
            self.bo_click_tab('General information')
            catalogue_code = self.bo_get_value('Catalogue code')
            # search and verify
            self.deposit_catalogue_view(
                catalogue_code=catalogue_code,
                catalogue_name=catalogue_name
            )
            print('Updated catalogue code: ' + catalogue_code)
            return catalogue_code

    def deposit_catalogue_delete(self, catalogue_code, list_error_message=None):
        # search
        self.deposit_catalogue_simple_search(catalogue_code)
        if catalogue_code:
            self.assert_table_data('Catalogue code', 1, catalogue_code)
        # delete
        self.click_table_menu('Delete', 1)
        self.wait_loading()
        self.click_button_in_popup('Yes')
        if list_error_message:
        # verify error
            self.assert_error_message()
            self.assert_list_error_message(list_error_message)
            print(f'Delete catalogue code: {catalogue_code} failed!')
        else:
            # verify success
            self.assert_notification('Deleted successfully')
            # search and verify
            self.deposit_catalogue_simple_search(catalogue_code)
            self.assert_search_not_found()
            print('Deleted catalogue code: ' + catalogue_code)
            return catalogue_code

    # DPT-Account Information
    def deposit_account_simple_search(self, text):
        self.close_all_form()
        self.click_menu('Deposit', 'Account Information')
        self.wait_for_button_available('Add')
        self.assert_form_title('DPT-Account Information-Search')
        self.simple_search(text)

    def deposit_account_view(self, account_number, passbook_or_receipt_number=None, linkage_account_number=None, account_name=None, currency_code=None, account_holder_type=None, account_holder=None, branch_id=None, account_status=None, catalogue_code=None, deposit_type=None, deposit_sub_type=None, begin_of_tenor=None, end_of_tenor=None, open_date=None, close_date=None, last_transaction_date=None, last_date_system_transfer_interest_to_due=None, dormant_date=None, last_change_dormant_to_normal_date=None, created_by=None, approved_by=None, account_manager_staff_code=None, agent_hub_referral=None, relation_customers=None, business_purpose_code=None, is_restricted=None, current_balance=None, available_balance=None, minimum_deposit_amount=None, minimum_amount_to_dormant=None, earmark_block_amount=None, initial_deposit_amount=None, interest_accrual=None, interest_receivable=None, interest_prepaid=None, interest_due=None, interest_not_paid=None, interest_paid=None, deposit_amount=None, withdraw_amount=None, deposit_tenor=None, interest_tenor=None, minimum_tenor=None, multiple_deposit_allow=None, multiple_withdrawal_allow=None, early_withdrawal=None, minimum_tenor_allow_early_withdrawal=None, credit_interest=None, credit_interest_tenor=None, the_day_of_tenor_for_crediting_interest=None, dormant_period=None, rollover_option=None, rollover_to_catalogue=None, employer_organization_name=None, reference_id=None, reason_of_account_opening=None, relationship_manager=None, expected_account_gl_names=None, expected_account_gl_numbers=None, expected_account_gl_name=None, expected_account_gl_number=None, expected_ifc_codes=None, expected_ifc_gl_names=None, expected_ifc_gl_numbers=None, expected_ifc_list_codes=None, expected_ifc_code=None, expected_ifc_gl_name=None, expected_ifc_gl_number=None, expected_ifc_names=None, expected_ifc_base_values=None, expected_ifc_is_linkeds=None, expected_ifc_values=None, expected_ifc_margin_values=None, expected_ifc_statuses=None, expected_ifc_outstandings=None, expected_ifc_paids=None, expected_ifc_basic_balances=None, expected_ifc_name=None, expected_ifc_base_value=None, expected_ifc_is_linked=None, expected_ifc_value=None, expected_ifc_margin_value=None, expected_ifc_status=None, expected_ifc_outstanding=None, expected_ifc_paid=None, expected_ifc_basic_balance=None):
        # search deposit account
        self.deposit_account_simple_search(str(account_number).replace('-', ''))
        self.assert_table_data('Account number', 1, self.deposit_account_number_mask(account_number))
        # view deposit account
        self.click_table_menu('View', 1)
        self.wait_for_button_available('Modify')
        self.assert_form_title('DPT-Account Information-View')
        # verify value tab 'General information'
        self.bo_click_tab('General information')
        self.bo_assert_value('Account number', self.deposit_account_number_mask(account_number))
        if passbook_or_receipt_number:
            self.bo_assert_text('Passbook or receipt number', str(passbook_or_receipt_number).replace('-', ''))
        if linkage_account_number:
            self.bo_assert_value_group('Linkage account number', self.deposit_account_number_mask(linkage_account_number))
        if account_name:
            self.bo_assert_text('Account name', account_name)
        if currency_code:
            self.bo_assert_select('Currency code', currency_code)
        if account_holder_type:
            self.bo_assert_select('Account holder type', account_holder_type)
        if account_holder:
            self.bo_assert_value('Account holder', self.customer_code_mask(account_holder))
        if branch_id:
            self.bo_assert_text('Branch ID', branch_id)
        if account_status:
            self.bo_assert_select('Account status', account_status)
        if catalogue_code:
            self.bo_assert_value('Catalogue code', catalogue_code)
        if deposit_type:
            self.bo_assert_select('Deposit type', deposit_type)
        if deposit_sub_type:
            self.bo_assert_select('Deposit sub type', deposit_sub_type)
        if begin_of_tenor:
            self.bo_assert_date('Begin of tenor', begin_of_tenor)
        if end_of_tenor:
            self.bo_assert_date('End of tenor', end_of_tenor)
        if open_date:
            self.bo_assert_date('Open date', open_date)
        if close_date:
            self.bo_assert_date('Close date', close_date)
        if last_transaction_date:
            self.bo_assert_date('Last transaction date', last_transaction_date)
        if last_date_system_transfer_interest_to_due:
            self.bo_assert_date('Last date system transfer interest to due', last_date_system_transfer_interest_to_due)
        if dormant_date:
            self.bo_assert_date('Dormant date', dormant_date)
        if last_change_dormant_to_normal_date:
            self.bo_assert_date('Last change dormant to normal date', last_change_dormant_to_normal_date)
        if created_by:
            self.bo_assert_text_group('Created by', created_by)
        if approved_by:
            self.bo_assert_text_group('Approved by', approved_by)
        if account_manager_staff_code:
            self.bo_assert_text_group('Account manager staff code', account_manager_staff_code)
        if agent_hub_referral:
            self.bo_assert_value_group('Agent hub referral', agent_hub_referral)
        if relation_customers:
            self.bo_assert_value('Relation customers', relation_customers)
        if business_purpose_code:
            self.bo_assert_value('Business Purpose Code', business_purpose_code)
        if is_restricted:
            self.bo_assert_select('Is Restricted', is_restricted)
        # verify value tab 'Balance information'
        self.bo_click_tab('Balance information')
        if current_balance:
            self.bo_assert_value('Current balance', current_balance)
        if available_balance:
            self.bo_assert_value('Available balance', available_balance)
        if minimum_deposit_amount:
            self.bo_assert_value('Minimum deposit amount', minimum_deposit_amount)
        if minimum_amount_to_dormant:
            self.bo_assert_value('Minimum amount to dormant', minimum_amount_to_dormant)
        if earmark_block_amount:
            self.bo_assert_value('Earmark (block) amount', earmark_block_amount)
        if initial_deposit_amount:
            self.bo_assert_value('Initial deposit amount', initial_deposit_amount)
        if interest_accrual:
            self.bo_assert_value('Interest accrual', interest_accrual)
        if interest_receivable:
            self.bo_assert_value('Interest receivable', interest_receivable)
        if interest_prepaid:
            self.bo_assert_value('Interest prepaid', interest_prepaid)
        if interest_due:
            self.bo_assert_value('Interest due', interest_due)
        if interest_not_paid:
            self.bo_assert_value('Interest not paid', interest_not_paid)
        if interest_paid:
            self.bo_assert_value('Interest paid', interest_paid)
        if deposit_amount:
            self.bo_assert_value('Deposit amount', deposit_amount)
        if withdraw_amount:
            self.bo_assert_value('Withdraw amount', withdraw_amount)
        # verify value tab 'Tenor and relative information'
        self.bo_click_tab('Tenor and relative information')
        if deposit_tenor:
            self.bo_assert_value('Deposit tenor', deposit_tenor)
        if interest_tenor:
            self.bo_assert_value('Interest tenor', interest_tenor)
        if minimum_tenor:
            self.bo_assert_value('Minimum tenor', minimum_tenor)
        if multiple_deposit_allow:
            self.bo_assert_select('Multiple deposit allow', multiple_deposit_allow)
        if multiple_withdrawal_allow:
            self.bo_assert_select('Multiple withdrawal allow', multiple_withdrawal_allow)
        if early_withdrawal:
            self.bo_assert_select('Early withdrawal (Y/N)', early_withdrawal)
        if minimum_tenor_allow_early_withdrawal:
            self.bo_assert_value('Minimum tenor allow early withdrawal', minimum_tenor_allow_early_withdrawal)
        if credit_interest:
            self.bo_assert_select('Credit interest (Y/N)', credit_interest)
        if credit_interest_tenor:
            self.bo_assert_value('Credit interest tenor', credit_interest_tenor)
        if the_day_of_tenor_for_crediting_interest:
            self.bo_assert_value('The day of tenor for crediting interest', the_day_of_tenor_for_crediting_interest)
        if dormant_period:
            self.bo_assert_value('Dormant period', dormant_period)
        if rollover_option:
            self.bo_assert_select('Rollover option', rollover_option)
        if rollover_to_catalogue:
            self.bo_assert_value('Rollover to catalogue', rollover_to_catalogue)
        # verify value tab 'Addition information'
        self.bo_click_tab('Addition information')
        if employer_organization_name:
            self.bo_assert_text('Employer Organization Name', employer_organization_name)
        if reference_id:
            self.bo_assert_text('Reference id', reference_id)
        if reason_of_account_opening:
            self.bo_assert_text('Reason of Account Opening', reason_of_account_opening)
        if relationship_manager:
            self.bo_assert_select('Relationship Manager', relationship_manager)
        # verify value tab 'Account GLs Information'
        self.bo_click_tab('Account GLs Information')
        if expected_account_gl_names:
            for account_gl_name, account_gl_number in zip(expected_account_gl_names, expected_account_gl_numbers):
                self.bo_assert_text_table_account_gls(account_gl_name, str(account_gl_number).replace('-',''))
        if expected_account_gl_name:
            self.bo_assert_text_table_account_gls(expected_account_gl_name, str(expected_account_gl_number).replace('-',''))
        # verify value tab 'IFC list'
        self.bo_click_tab('IFC list')
        if expected_ifc_names:
            for ifc_code, ifc_name in zip(expected_ifc_list_codes, expected_ifc_names):
                self.bo_assert_text_table('IFC code', ifc_code, 'IFC name', ifc_name)
        if expected_ifc_name:
            self.bo_assert_text_table('IFC code', expected_ifc_code, 'IFC name', expected_ifc_name)
        if expected_ifc_base_values:
            for ifc_code, ifc_base_value in zip(expected_ifc_list_codes, expected_ifc_base_values):
                self.bo_assert_text_table('IFC code', ifc_code, 'Base value', ifc_base_value)
        if expected_ifc_base_value:
            self.bo_assert_text_table('IFC code', expected_ifc_code, 'Base value', expected_ifc_base_value)
        if expected_ifc_is_linkeds:
            for ifc_code, ifc_is_linked in zip(expected_ifc_list_codes, expected_ifc_is_linkeds):
                self.bo_assert_text_table('IFC code', ifc_code, 'Is linked', ifc_is_linked)
        if expected_ifc_is_linked:
            self.bo_assert_text_table('IFC code', expected_ifc_code, 'Is linked', expected_ifc_is_linked)
        if expected_ifc_values:
            for ifc_code, ifc_value in zip(expected_ifc_list_codes, expected_ifc_values):
                self.bo_assert_text_table('IFC code', ifc_code, 'IFC Value', ifc_value)
        if expected_ifc_value:
            self.bo_assert_text_table('IFC code', expected_ifc_code, 'IFC Value', expected_ifc_value)
        if expected_ifc_margin_values:
            for ifc_code, ifc_margin_value in zip(expected_ifc_list_codes, expected_ifc_margin_values):
                self.bo_assert_text_table('IFC code', ifc_code, 'Margin Value', ifc_margin_value)
        if expected_ifc_margin_value:
                self.bo_assert_text_table('IFC code', expected_ifc_code, 'Margin Value', expected_ifc_margin_value)
        if expected_ifc_statuses:
            for ifc_code, ifc_status in zip(expected_ifc_list_codes, expected_ifc_statuses):
                self.bo_assert_text_table('IFC code', ifc_code, 'Status', ifc_status)
        if expected_ifc_status:
            self.bo_assert_text_table('IFC code', expected_ifc_code, 'Status', expected_ifc_status)
        if expected_ifc_outstandings:
            for ifc_code, ifc_outstanding in zip(expected_ifc_list_codes, expected_ifc_outstandings):
                self.bo_assert_text_table('IFC code', ifc_code, 'Oustanding', ifc_outstanding)
        if expected_ifc_outstanding:
                self.bo_assert_text_table('IFC code', expected_ifc_code, 'Oustanding', expected_ifc_outstanding)
        if expected_ifc_paids:
            for ifc_code, ifc_paid in zip(expected_ifc_list_codes, expected_ifc_paids):
                self.bo_assert_text_table('IFC code', ifc_code, 'Paid', ifc_paid)
        if expected_ifc_paid:
                self.bo_assert_text_table('IFC code', expected_ifc_code, 'Paid', expected_ifc_paid)
        if expected_ifc_basic_balances:
            for ifc_code, ifc_basic_balance in zip(expected_ifc_list_codes, expected_ifc_basic_balances):
                self.bo_assert_text_table('IFC code', ifc_code, 'Basic balance', ifc_basic_balance)
        if expected_ifc_basic_balance:
                self.bo_assert_text_table('IFC code', expected_ifc_code, 'Basic balance', expected_ifc_basic_balance)
        # verify value tab 'IFC GLs Information'
        self.bo_click_tab('IFC GLs Information')
        if expected_ifc_codes:
            for ifc_code, ifc_gl_name, ifc_gl_number in zip(expected_ifc_codes, expected_ifc_gl_names, expected_ifc_gl_numbers):
                self.bo_assert_text_table_ifc_gls(ifc_code, ifc_gl_name, str(ifc_gl_number).replace('-',''))

    def deposit_account_update(self, account_number, agent_hub_referral=None, is_restricted=None, rollover_option=None, rollover_to_catalogue=None, reason_of_account_opening=None, list_error_message=None):
        # search deposit account
        self.deposit_account_simple_search(str(account_number).replace('-', ''))
        self.assert_table_data('Account number', 1, account_number)
        # view deposit account
        self.click_table_menu('View', 1)
        self.wait_for_button_available('Modify')
        self.assert_form_title('DPT-Account Information-View')
        self.click_button('Modify')
        # update value tab 'General information'
        self.bo_click_tab('General information')
        if agent_hub_referral:
            self.bo_write_group('Agent hub referral', agent_hub_referral)
        if is_restricted:
            self.bo_select('Is Restricted', is_restricted)
        # update value tab 'Tenor and relative information'
        self.bo_click_tab('Tenor and relative information')
        if rollover_option:
            self.bo_select('Rollover option', rollover_option)
        if rollover_to_catalogue:
            self.lookup_data('Rollover to catalogue', 'Code', rollover_to_catalogue)
        # update value tab 'Addition information'
        self.bo_click_tab('Addition information')
        if reason_of_account_opening:
            self.bo_write_text('Reason of Account Opening', reason_of_account_opening)
        # update value tab 'IFC list'
        # self.bo_click_tab('IFC list')
        # click 'Save'
        self.click_button('Save')
        if list_error_message:
        # verify error
            self.assert_error_message()
            self.assert_list_error_message(list_error_message)
            print(f'Update account number: {account_number} failed!')
            return ''
        else:
        # verify success
            self.assert_button_disable('Save')
            self.assert_notification('Save successfully')
            account_number = self.bo_get_value_data('Account number')
            print('Updated account number: ' + account_number)
            return account_number

    def deposit_account_delete(self, account_number, list_error_message=None):
        # search deposit account
        account_number = str(account_number).replace('-', '')
        self.deposit_account_simple_search(account_number)
        self.assert_table_data('Account number', 1, self.deposit_account_number_mask(account_number))
        # delete deposit account
        self.click_table_menu('Delete', 1)
        self.wait_loading()
        self.click_button_in_popup('Yes')
        if list_error_message:
        # verify error
            self.assert_error_message()
            self.assert_list_error_message(list_error_message)
            print(f'Delete account number: {account_number} failed!')
        else:
        # verify success
            self.assert_notification('Deleted successfully')
            # search and verify
            self.deposit_account_simple_search(account_number)
            self.assert_search_not_found()
            print('Account number: ' + account_number)
            return account_number

    def check_deposit_account_not_exist(self, account_number):
        account_number = str(account_number).replace('-', '')
        # search account number
        self.deposit_account_simple_search(account_number)
        if (self.get_text_notification(timeout=3) == 'Data not found'):
            print(f"Account number '{account_number}' does NOT exist.")
            return True
        else:
            print(f"Account number '{account_number}' already exists.")
            return False

    # DPT-Approve Account Modification
    def deposit_account_modify_search(self, text):
        self.close_all_form()
        self.click_menu('Deposit', 'Approve Account Modification')
        self.wait_for_button_available('Search')
        self.assert_form_title('DPT-Approve Account Modification-Search')
        self.simple_search(text)

    def deposit_account_modify_view(self, account_number):
        # search deposit account modify
        self.deposit_account_modify_search(str(account_number).replace('-', ''))
        self.assert_table_data('Account number', 1, account_number)
        # view deposit account modify
        self.click_table_menu(row=1)
        self.wait_for_button_available('View Modification')
        self.assert_form_title('DPT-Approve Account Modification-View')
        # verify value tab 'General information'
        self.bo_assert_value('Account number', account_number)

    def deposit_account_modify_approve(self, account_number):
        self.deposit_account_modify_view(account_number)
        self.click_button('View Modification')
        self.wait_loading()
        self.click_button('Approve')
        self.wait_loading()
        self.assert_notification('Approve successfully')
        # back to tab 'General information'
        self.bo_click_tab('General information')
        self.bo_assert_value('Account number', account_number)
        account_number_actual = self.bo_get_value('Account number')
        print('Account number: ' + account_number_actual)
        self.deposit_account_modify_search(str(account_number_actual).replace('-', ''))
        self.assert_search_not_found()
        return account_number_actual

    def deposit_account_modify_reject(self, account_number):
        self.deposit_account_modify_view(account_number)
        self.click_button('View Modification')
        self.wait_loading()
        self.click_button('Reject')
        self.wait_loading()
        self.assert_notification('Reject successfully')
        # back to tab 'General information'
        self.bo_click_tab('General information')
        self.bo_assert_value('Account number', account_number)
        account_number_actual = self.bo_get_value('Account number')
        print('Account number: ' + account_number_actual)
        self.deposit_account_modify_search(str(account_number_actual).replace('-', ''))
        self.assert_search_not_found()
        return account_number_actual

    # DPT-Stock Inventory
    def stock_inventory_advanced_search(self, stock_prefix, from_serial, to_serial, stock_type=None):
        self.close_all_form()
        self.click_menu('Deposit', 'Stock Inventory')
        self.wait_for_button_available('Add')
        self.assert_form_title('DPT-Stock Inventory-Search')
        self.click_collap_multi_non_tab('Advanced search')
        self.advanced_search('Stock prefix', stock_prefix, field_type='A')
        if len(from_serial) != 6:
            from_serial = self.get_serial_number_no_refix(from_serial)
        self.advanced_search('From serial from', from_serial, in_group='Y')
        if len(to_serial) != 6:
            to_serial = self.get_serial_number_no_refix(to_serial)
        self.advanced_search('To serial to', to_serial, in_group='Y')
        if not stock_type:
            self.advanced_search('Stock type', stock_type, field_type='S')
        self.click_button_search_advanced()

    def stock_inventory_simple_search(self, text):
        self.close_all_form()
        self.click_menu('Deposit', 'Stock Inventory')
        self.wait_for_button_available('Add')
        self.assert_form_title('DPT-Stock Inventory-Search')
        self.simple_search(text)

    def stock_inventory_view(self, stock_prefix, from_serial, to_serial, stock_no=None, book_status=None, confirm_status=None, branch=None, user_create=None, user_approved=None, stock_holding_user=None, status_of_stock_leaves=None, stock_type=None, issuing_name=None, issuer_id_number=None, issuer_contact_number=None, amount=None, currency=None, beneficiary_name=None, beneficiary_id_number=None, contact=None, beneficiary_address=None, stock_balance=None, module=None, no_of_leaves_book=None, no_of_books=None, stock_leaves_status=None, ref_account_no=None, purpose=None, branch_code=None, assigned_teller_code=None, created_by=None, approved_by=None):
        self.stock_inventory_advanced_search(stock_prefix, from_serial, to_serial, stock_type=stock_type)
        # verify value at search
        self.assert_table_data('Stock prefix', 1, stock_prefix)
        self.assert_table_data('From serial', 1, from_serial)
        self.assert_table_data('To serial', 1, to_serial)
        if stock_no:
            self.assert_table_data('Stock No', 1, stock_no)
        if book_status:
            self.assert_table_data('Book status', 1, book_status)
        if confirm_status:
            self.assert_table_data('Confirm status', 1, confirm_status)
        if branch:
            self.assert_table_data('Branch', 1, branch)
        if user_create:
            self.assert_table_data('User create', 1, user_create)
        if user_approved:
            self.assert_table_data('User approved', 1, user_approved)
        if stock_holding_user:
            self.assert_table_data('Stock holding user', 1, stock_holding_user)
        if status_of_stock_leaves:
            self.assert_table_data('Status of stock leaves', 1, status_of_stock_leaves)
        if stock_type:
            self.assert_table_data('Stock type', 1, stock_type)
        if ref_account_no:
            self.assert_table_data('Account number', 1, ref_account_no)
        if issuing_name:
            self.assert_table_data('Issuing name', 1, issuing_name)
        if issuer_id_number:
            self.assert_table_data('Issuer ID number', 1, issuer_id_number)
        if issuer_contact_number:
            self.assert_table_data('Issuer contact number', 1, issuer_contact_number)
        if amount:
            amount_value = self.format_number(amount)
            self.assert_table_data('Amount', 1, amount_value)
        if currency:
            self.assert_table_data('Currency', 1, currency)
        if beneficiary_name:
            self.assert_table_data('Beneficiary name', 1, beneficiary_name)
        if beneficiary_id_number:
            self.assert_table_data('Beneficiary ID number', 1, beneficiary_id_number)
        if contact:
            self.assert_table_data('Contact', 1, contact)
        if beneficiary_address:
            self.assert_table_data('Beneficiary address', 1, beneficiary_address)
        if stock_balance:
            stock_balance_value = self.format_number(stock_balance)
            self.assert_table_data('Stock balance', 1, stock_balance_value)
        # view
        self.click_table_menu('View', 1)
        self.wait_loading()
        self.assert_form_title('DPT-Stock Inventory-View')
        # verify value tab 'Stock inventory information'
        self.bo_click_tab('Stock inventory information')
        if stock_no:
            self.bo_assert_text('Stock No.', stock_no)
        if module:
            self.bo_assert_select('Module', module)
        if stock_type:
            self.bo_assert_select('Stock type', stock_type)
        if from_serial:
            self.bo_assert_text('From serial', from_serial)
        if to_serial:
            self.bo_assert_text('To serial', to_serial)
        if stock_prefix:
            self.bo_assert_text('Stock prefix', stock_prefix)
        if no_of_leaves_book:
            self.bo_assert_text('No. of leaves/book', no_of_leaves_book)
        if no_of_books:
            self.bo_assert_text('No. of books', no_of_books)
        if stock_leaves_status:
            self.bo_assert_text('Stock leaves status', stock_leaves_status)
        if confirm_status:
            self.bo_assert_select('Confirm status', confirm_status)
        if book_status:
            self.bo_assert_select('Book Status', book_status)
        if ref_account_no:
            self.bo_assert_text('Ref. account No.', ref_account_no)
        if purpose:
            self.bo_assert_text('Purpose', purpose)
        if branch_code:
            self.bo_assert_text('Branch code', branch_code)
        if assigned_teller_code:
            self.bo_assert_text_group('Assigned teller code', assigned_teller_code)
        if created_by:
            self.bo_assert_text_group('Created by', created_by)
        if approved_by:
            self.bo_assert_text_group('Approved by', approved_by)
        # verify value tab 'Detail Information'
        self.bo_click_tab('Detail Information')
        if issuer_id_number:
            self.bo_assert_text('Issuer ID number', issuer_id_number)
        if issuing_name:
            self.bo_assert_text('Issuing name', issuing_name)
        if issuer_contact_number:
            self.bo_assert_text('Issuer contact number', issuer_contact_number)
        if amount:
            self.bo_assert_value('Amount', f"{amount}0")
        if currency:
            self.bo_assert_text('Currency', currency)
        if beneficiary_id_number:
            self.bo_assert_text('Beneficiary ID number', beneficiary_id_number)
        if beneficiary_name:
            self.bo_assert_text('Beneficiary name', beneficiary_name)
        if beneficiary_address:
            self.bo_assert_text('Beneficiary address', beneficiary_address)
        if contact:
            self.bo_assert_text('Contact', contact)
        if stock_balance:
            self.bo_assert_value('Stock balance', stock_balance)

    def stock_inventory_delete(self, stock_prefix, from_serial, to_serial, stock_type=None, list_error_message=None):
        self.stock_inventory_advanced_search(stock_prefix, from_serial, to_serial, stock_type=stock_type)
        # delete
        self.click_table_menu('Delete', 1)
        self.wait_loading()
        self.click_button_in_popup('Yes')
        if list_error_message:
        # verify error
            self.assert_error_message()
            self.assert_list_error_message(list_error_message)
            print(f'Delete stock_prefix: {stock_prefix}, from_serial: {from_serial}, to_serial: {to_serial} failed!')
        else:
        # verify success
            self.assert_notification('Deleted successfully')
            # search and verify
            self.stock_inventory_advanced_search(stock_prefix, from_serial, to_serial, stock_type=stock_type)
            self.assert_search_not_found()
            print(f'Deleted stock_prefix: {stock_prefix}, from_serial: {from_serial}, to_serial: {to_serial}')
            return stock_prefix, from_serial, to_serial

    # DPT-Account Linkage
    def dpt_account_linkage_simple_search(self, text):
        self.close_all_form()
        self.click_menu('Payment', 'Account Linkage')
        self.wait_for_button_available('Search')
        self.assert_form_title('DPT-Account Linkage-Search')
        self.simple_search(text)
        self.wait_loading()

    def dpt_account_linkage_add(self, master_module_name, master_account_code, linkage_module_name, linkage_account_code, linkage_type, linkage_classification, linkage_description=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.click_menu('Payment', 'Account Linkage')
        self.wait_for_button_available('Add')
        self.assert_form_title('DPT-Account Linkage-Search')
        self.click_button('Add')
        self.wait_for_button_available('Accept')
        self.assert_form_title('DPT-Account Linkage-Add')
        # enter value
        self.select('Master module name', master_module_name)
        self.lookup_data('Master account code', 'Code', master_account_code)
        self.click_button('Add')
        self.select('Linkage module name', linkage_module_name)
        self.lookup_data('Linkage account  code', 'Code', linkage_account_code)
        self.select('Linkage type', linkage_type)
        self.select('Linkage classification', linkage_classification)
        if linkage_description:
            self.fo_write_text('Linkage description', linkage_description)
        self.click_button('Apply')
        if ifc_codes:
            self.add_fees(ifc_codes, values, total_fee)
        # click 'Accept'
        self.click_button('Accept')
        # approve
        if approve_later=='Y':
            self.click_button('Later')
        if approve_on_form=='Y':
            self.fo_approve_in_popup(
                username=username,
                password=password,
                reason=reason
            )
        if list_error_message:
        # verify error
            self.assert_error_message()
            self.assert_list_error_message(list_error_message)
            print('Transaction failed!')
        else:
        # verify success
            self.assert_button_disable('Accept')
            self.switch_to_core_banking()
            self.assert_notification('Saved successfully!')
            self.close_voucher()
            if expected_posting:
                self.assert_posting_data(**expected_posting)
            transaction_references=self.fo_get_text('Transaction references')
            print(f'Transaction references DPT_OPAL: {transaction_references}')
            master_account_code=self.fo_get_value_group('Master account code')
            print(f'Master account number: {master_account_code}')
            linkage_account_code=self.get_text_table_data('Linkage account code', 1)
            print(f'Linkage account code: {linkage_account_code}')
            return transaction_references, master_account_code, linkage_account_code

    def dpt_account_linkage_view(self, master_account_number, master_module_name=None, row=None, linkage_module_name=None, linkage_account_code=None, linkage_account_name=None, linkage_description=None, linkage_type=None, linkage_classification=None):
        master_account_number = str(master_account_number).replace('-', '')
        if row is None:
            row = 1
        # search
        self.dpt_account_linkage_simple_search(master_account_number)
        if master_account_number:
            self.assert_table_data('Master account number', 1, master_account_number)
        # view
        self.click_table_menu('View', 1)
        self.wait_for_button_available('Modify')
        self.assert_form_title('DPT-Account Linkage-View')
        # verify value
        self.bo_assert_value_group('Master account number', master_account_number)
        if master_module_name:
            self.bo_assert_select('Master module name', master_module_name)
        if linkage_module_name:
            self.assert_table_data('Linkage module name', row, linkage_module_name)
        if linkage_account_code:
            self.assert_table_data('Linkage account code', row, linkage_account_code)
        if linkage_account_name:
            self.assert_table_data('Linkage account name', row, linkage_account_name)
        if linkage_description:
            self.assert_table_data('Linkage description', row, linkage_description)
        if linkage_type:
            self.assert_table_data('Linkage type', row, linkage_type)
        if linkage_classification:
            self.assert_table_data('Linkage class', row, linkage_classification)
        print('View master account number: ' + master_account_number)
        return master_account_number

    def dpt_account_linkage_update(self, master_account_number, action=None, row=None, linkage_type=None, linkage_classification=None, linkage_description=None, list_error_message=None):
        master_account_number = str(master_account_number).replace('-', '')
        if row is None:
            row = 1
        self.dpt_account_linkage_view(master_account_number)
        self.wait_loading()
        self.click_button('Modify')
        # update value
        if action == 'Modify':
            self.click_table_menu(action, row)
            if linkage_type:
                self.select('Linkage type', linkage_type)
            if linkage_classification:
                self.select('Linkage classification', linkage_classification)
            if linkage_description:
                self.bo_set_text('Linkage description', linkage_description)
            # click 'Apply'
            self.click_button('Apply')
            # click 'Save'
            self.click_button('Save')
            if list_error_message:
            # verify error
                self.assert_error_message()
                self.assert_list_error_message(list_error_message)
                print('Update modify failed!')
            else:
            # verify success
                self.assert_button_disable('Save')
                self.assert_notification('Saved successfully!')
                master_account_number = self.bo_get_value_data('Master account number')
                # search and verify
                self.dpt_account_linkage_view(
                    master_account_number=master_account_number,
                    linkage_type=linkage_type,
                    linkage_classification=linkage_classification,
                    linkage_description=linkage_description
                )
                self.wait_loading()
                print('Updated modify for master account number: ' + master_account_number)
                return master_account_number
        # remove link value
        if action == 'Remove':
            self.click_table_menu(action, row)
            # click 'Save'
            self.click_button('Save')
            if list_error_message:
            # verify error
                self.assert_error_message()
                self.assert_list_error_message(list_error_message)
                print('Update remove failed!')
            else:
            # verify success
                self.assert_button_disable('Save')
                self.assert_notification('Saved successfully!')
                master_account_number = self.bo_get_value_data('Master account number')
                # search and verify
                self.dpt_account_linkage_view(
                    master_account_number=master_account_number,
                    linkage_type=linkage_type,
                    linkage_classification=linkage_classification,
                    linkage_description=linkage_description
                )
                self.wait_loading()
                print('Updated remove for master account number: ' + master_account_number)
                return master_account_number
        if action is None:
            # click 'Save'
            self.click_button('Save')
            if list_error_message:
            # verify error
                self.assert_error_message()
                self.assert_list_error_message(list_error_message)
                print('Update failed!')
            else:
            # verify success
                self.assert_button_disable('Save')
                self.assert_notification('Saved successfully!')
                master_account_number = self.bo_get_value_data('Master account number')
                # search and verify
                self.dpt_account_linkage_view(
                    master_account_number=master_account_number,
                    linkage_type=linkage_type,
                    linkage_classification=linkage_classification,
                    linkage_description=linkage_description
                )
                self.wait_loading()
                print('Updated master account number: ' + master_account_number)
                return master_account_number

    def dpt_account_linkage_delete(self, master_account_number):
        master_account_number = str(master_account_number).replace('-', '')
        # search GL account
        self.dpt_account_linkage_simple_search(master_account_number)
        if master_account_number:
            self.assert_table_data('Master account number', 1, master_account_number)
        # delete GL account
        self.click_table_menu('Delete', 1)
        self.wait_loading()
        self.click_button_in_popup('Yes')
        self.assert_notification('Deleted successfully')
        # search and verify
        self.wait_loading()
        self.dpt_account_linkage_simple_search(master_account_number)
        self.assert_search_not_found()
        print('Delete master account number: ' + master_account_number)
        return master_account_number

# -------------------------- handle BO - MORTGAGE --------------------------
    # MTG-Account Information
    def mortgage_account_simple_search(self, text):
        self.close_all_form()
        self.click_menu('Collateral', 'Account Information')
        self.wait_for_button_available('Search')
        self.assert_form_title('MTG-Account Information-Search')
        self.simple_search(text)

    def mortgage_account_view(self, account_number, account_name=None, cc_contract=None, currency_code=None, book_currency_code=None, account_holder_type=None, customer_code=None, branch_code=None, collateral_account_status=None, catalogue_code=None, collateral_asset_type=None, collateral_asset_classification=None, collateral_rate=None, risk_allocation_rate=None, book_scope=None, depreciation_option=None, was_register_at_collateral_center=None, security_paper_type=None, reference_number=None, name_of_title=None, house_no=None, plot_no=None, holding_no=None, ward_no=None, block_no=None, area_acre=None, street=None, township=None, division_city=None, location=None, legal_local_address=None, evaluate_by=None, evaluate_method=None, evaluate_date=None, new_evaluate_date=None, insurance_name=None, open_date=None, insurance_expiry_date=None, close_date=None, last_transaction_date=None, created_by=None, approved_by=None, account_manager_staff_id=None, other_paper_type=None, other_paper_no=None, collateral_asset_value=None, market_value=None, forced_sale_value=None, current_secure_amount=None, cc_amount=None, loan_to_fsv=None, released_collateral_amount=None, keeping_amount=None, keeping_release_amount=None, other_counter_party_collateral_amount=None, other_counter_party_collateral_released=None, sum_insurance_amount=None, premium_amount=None, original_amount_price=None, accumulate_of_depreciation_amount=None, net_book_value_after_depreciation=None, week_debit=None, week_credit=None, month_debit=None, month_credit=None, quarter_debit=None, quarter_credit=None, semi_annual_debit=None, semi_annual_credit=None, year_debit=None, year_credit=None, remark=None, reference_id=None, owner=None, user_define_1=None, user_define_2=None, user_define_3=None, user_define_4=None, user_define_5=None, policy_number=None, expiry_date=None, policy_amount=None, company_issues_policy=None):
        # search mortgage account
        self.mortgage_account_simple_search(str(account_number).replace('-', ''))
        self.assert_table_data('Account number', 1, str(account_number).replace('-', ''))
        if account_name:
            self.assert_table_data('Account name', 1, account_name)
        if currency_code:
            self.assert_table_data('Currency', 1, currency_code)
        if collateral_account_status:
            self.assert_table_data('Status', 1, collateral_account_status)
        if catalogue_code:
            self.assert_table_data('Catalogue code', 1, catalogue_code)
        if customer_code:
            self.assert_table_data('Customer code', 1, self.customer_code_mask(customer_code))
        if collateral_asset_type:
            self.assert_table_data('Collateral type', 1, collateral_asset_type)
        if collateral_asset_classification:
            self.assert_table_data('Classification', 1, collateral_asset_classification)
        # view mortgage account
        self.click_table_menu('View', 1)
        self.wait_for_button_available('Modify')
        self.assert_form_title('MTG-Account Information-View')
        # verify value tab 'General information'
        self.bo_click_tab('General information')
        self.bo_assert_text('Account code', str(account_number).replace('-', ''))
        if account_name:
            self.bo_assert_text('Account name', account_name)
        if cc_contract:
            self.bo_assert_text('CC contract', cc_contract)
        if currency_code:
            self.bo_assert_select('Currency code', currency_code)
        if book_currency_code:
            self.bo_assert_select('Book currency code', book_currency_code)
        if account_holder_type:
            self.bo_assert_select('Account holder type', account_holder_type)
        if customer_code:
            self.bo_assert_value_group('Customer code', customer_code)
        if branch_code:
            self.bo_assert_text('Branch code', branch_code)
        if collateral_account_status:
            self.bo_assert_select('Collateral account status', collateral_account_status)
        if catalogue_code:
            self.bo_assert_text_group('Catalogue code', catalogue_code)
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
        if was_register_at_collateral_center:
            self.bo_assert_select('Was register at collateral center', was_register_at_collateral_center)
        if security_paper_type:
            self.bo_assert_select('Security paper type', security_paper_type)
        if reference_number:
            self.bo_assert_text('Reference number', reference_number)
        self.bo_click_collap('Other address')
        if name_of_title:
            self.bo_assert_text_multi('Name of title', name_of_title)
        if house_no:
            self.bo_assert_text_multi('House no', house_no)
        if plot_no:
            self.bo_assert_text_multi('Plot no', plot_no)
        if holding_no:
            self.bo_assert_text_multi('Holding no', holding_no)
        if ward_no:
            self.bo_assert_text_multi('Ward no', ward_no)
        if block_no:
            self.bo_assert_text_multi('Block no', block_no)
        if area_acre:
            self.bo_assert_text_multi('Area (acre)', area_acre)
        if street:
            self.bo_assert_text_multi('Street', street)
        if township:
            self.bo_assert_text_multi('Township', township)
        if division_city:
            self.bo_assert_text_multi('Division, city', division_city)
        if location:
            self.bo_assert_select('Location', location)
        if legal_local_address:
            self.bo_assert_text('Legal local address', legal_local_address)
        if evaluate_by:
            self.bo_assert_text('Evaluate by', evaluate_by)
        if evaluate_method:
            self.bo_assert_select('Evaluate method', evaluate_method)
        if evaluate_date:
            self.bo_assert_date('Evaluate date', evaluate_date)
        if new_evaluate_date:
            self.bo_assert_date('New evaluate date', new_evaluate_date)
        if insurance_name:
            self.bo_assert_text('Insurance Name', insurance_name)
        if open_date:
            self.bo_assert_date('Open date', open_date)
        if insurance_expiry_date:
            self.bo_assert_text('Insurance Expiry Date', insurance_expiry_date)
        if close_date:
            self.bo_assert_date('Close date', close_date)
        if last_transaction_date:
            self.bo_assert_date('Last transaction date', last_transaction_date)
        if created_by:
            self.bo_assert_text_group('Created by', created_by)
        if approved_by:
            self.bo_assert_text_group('Approved by', approved_by)
        if account_manager_staff_id:
            self.bo_assert_text_group('Account manager staff id', account_manager_staff_id)
        # verify value tab 'Other paper information'
        self.bo_click_tab('Other paper information')
        if other_paper_type:
            self.bo_assert_select('Other paper type', other_paper_type)
        if other_paper_no:
            self.bo_assert_text('Other paper no', other_paper_no)
        # verify value tab 'Outstanding information'
        self.bo_click_tab('Outstanding information')
        if collateral_asset_value:
            self.bo_assert_value('Collateral asset value', collateral_asset_value)
        if market_value:
            self.bo_assert_value('Market value', market_value)
        if forced_sale_value:
            self.bo_assert_value('Forced sale value', forced_sale_value)
        if current_secure_amount:
            self.bo_assert_value('Current secure amount', current_secure_amount)
        if cc_amount:
            self.bo_assert_value('CC amount', cc_amount)
        if loan_to_fsv:
            self.bo_assert_value('Loan to FSV (%)', loan_to_fsv)
        if released_collateral_amount:
            self.bo_assert_value('Released collateral amount', released_collateral_amount)
        if keeping_amount:
            self.bo_assert_value('Keeping amount', keeping_amount)
        if keeping_release_amount:
            self.bo_assert_value('Keeping release amount', keeping_release_amount)
        if other_counter_party_collateral_amount:
            self.bo_assert_value('Other counter party collateral amount', other_counter_party_collateral_amount)
        if other_counter_party_collateral_released:
            self.bo_assert_value('Other counter party collateral released', other_counter_party_collateral_released)
        if sum_insurance_amount:
            self.bo_assert_value('Sum insurance amount', sum_insurance_amount)
        if premium_amount:
            self.bo_assert_value('Premium amount', premium_amount)
        if original_amount_price:
            self.bo_assert_value('Original amount/price', original_amount_price)
        if accumulate_of_depreciation_amount:
            self.bo_assert_value('Accumulate of depreciation amount', accumulate_of_depreciation_amount)
        if net_book_value_after_depreciation:
            self.bo_assert_value('Net book value after depreciation', net_book_value_after_depreciation)
        if week_debit:
            self.bo_assert_value('Week debit', week_debit)
        if week_credit:
            self.bo_assert_value('Week credit', week_credit)
        if month_debit:
            self.bo_assert_value('Month debit', month_debit)
        if month_credit:
            self.bo_assert_value('Month credit', month_credit)
        if quarter_debit:
            self.bo_assert_value('Quarter debit', quarter_debit)
        if quarter_credit:
            self.bo_assert_value('Quarter credit', quarter_credit)
        if semi_annual_debit:
            self.bo_assert_value('Semi-annual debit', semi_annual_debit)
        if semi_annual_credit:
            self.bo_assert_value('Semi-annual credit', semi_annual_credit)
        if year_debit:
            self.bo_assert_value('Year debit', year_debit)
        if year_credit:
            self.bo_assert_value('Year credit', year_credit)
        # verify value tab 'Secured Account'
        self.bo_click_tab('Secured Account')
        # verify value tab 'Addition information'
        self.bo_click_tab('Addition information')
        if remark:
            self.bo_assert_text('Remark', remark)
        if reference_id:
            self.bo_assert_text('Reference id', reference_id)
        if owner:
            self.bo_assert_text('Owner', owner)
        if user_define_1:
            self.bo_assert_text('User define 1', user_define_1)
        if user_define_2:
            self.bo_assert_text('User define 2', user_define_2)
        if user_define_3:
            self.bo_assert_text('User define 3', user_define_3)
        if user_define_4:
            self.bo_assert_text('User define 4', user_define_4)
        if user_define_5:
            self.bo_assert_text('User define 5', user_define_5)
        if policy_number:
            self.bo_assert_text('Policy number', policy_number)
        if expiry_date:
            self.bo_assert_date('Expiry date', expiry_date)
        if policy_amount:
            self.bo_assert_value('Policy Amount', policy_amount)
        if company_issues_policy:
            self.bo_assert_text('Company issues policy', company_issues_policy)

# -------------------------- handle BO - ACCOUNTING --------------------------
    # ACT-Bank Account Definition
    def accounting_bank_account_definition_simple_search(self, text):
        self.close_all_form()
        self.click_menu('Accounting', 'Bank Account Definition')
        self.wait_for_button_available('Search')
        self.assert_form_title('ACT-Bank Account Definition-Search')
        self.simple_search(text)
        self.wait_loading()

    def accounting_bank_account_definition_add(self, account_level, currency_code, account_number, account_name, short_account_name, direct_posting, is_inactive, branch_code, laos_name=None, thai_name=None, khmer_name=None, vietnamese_name=None, account_classification=None, reverse_balance=None, balance_side=None, posting_side=None, account_group=None, account_categories=None, job_process_option=None):
        # Check if the GL account number exists; if not, break the loop
        account_number = str(account_number).replace('-', '')
        if self.check_gl_account_not_exist(account_number):
            print('Account number does not exist')
            # open form
            self.close_all_form()
            self.click_menu('Accounting', 'Bank Account Definition')
            self.wait_for_button_available('Add')
            self.assert_form_title('ACT-Bank Account Definition-Search')
            self.click_button('Add')
            self.wait_for_button_available('Save')
            self.assert_form_title('ACT-Bank Account Definition-Add')
            # enter value
            if account_level:
                self.bo_select_single('Account level', account_level)
            if currency_code:
                self.bo_select_single('Currency code', currency_code)
            if account_number:
                self.bo_set_text('Account number', account_number)
            if account_name:
                self.bo_set_text('Account name', account_name)
            if short_account_name:
                self.bo_set_text('Short account name', short_account_name)
            if laos_name is not None or thai_name is not None or khmer_name is not None or vietnamese_name is not None:
                collap_name = 'Other name'
                self.bo_click_collap_single(collap_name)
                if laos_name:
                    self.bo_write_text_multi_single(collap_name, 'Laos name', laos_name)
                if thai_name:
                    self.bo_write_text_multi_single(collap_name, 'Thai name', thai_name)
                if khmer_name:
                    self.bo_write_text_multi_single(collap_name, 'Khmer name', khmer_name)
                if vietnamese_name:
                    self.bo_write_text_multi_single(collap_name, 'Vietnamese name', vietnamese_name)
            if account_classification:
                self.bo_select_single('Account classification', account_classification)
            if reverse_balance:
                self.bo_select_single('Reverse balance', reverse_balance)
            if balance_side:
                self.bo_select_single('Balance side', balance_side)
            if posting_side:
                self.bo_select_single('Posting side', posting_side)
            if account_group:
                self.bo_select_single('Account group', account_group)
            if account_categories:
                self.bo_select_single('Account categories', account_categories)
            if direct_posting:
                self.bo_select_single('Direct posting', direct_posting)
            if is_inactive:
                self.bo_select_single('Is Inactive', is_inactive)
            if job_process_option:
                self.bo_select_single('Job process option', job_process_option)
            if branch_code:
                self.assertEqual(str(self.bo_get_select_single('Branch Code')).split(' - ')[0], branch_code)
            self.click_button('Save')
            self.assert_button_disable('Save')
            self.assert_notification('Saved successfully!')
            account_number = self.bo_get_text_data('Account number')
            # search and verify
            self.accounting_bank_account_definition_simple_search(account_number)
            if account_level:
                self.assert_table_data('Account level', 1, str(account_level).split('-')[0])
            if account_number:
                self.assert_table_data('Account number', 1, account_number)
            if currency_code:
                self.assert_table_data('Currency', 1, currency_code)
            if account_name:
                self.assert_table_data('Account name', 1, account_name)
            if account_classification:
                self.assert_table_data('Classification', 1, account_classification)
            if balance_side:
                self.assert_table_data('Balance side', 1, balance_side)
            if account_group:
                self.assert_table_data('Group', 1, account_group)
        else:
            print('Account number already exists')
        print('Account number: ' + account_number)
        return account_number

    def accounting_bank_account_definition_view(self, account_number, account_level=None, currency_code=None, account_name=None, short_account_name=None, laos_name=None, thai_name=None, khmer_name=None, vietnamese_name=None, account_classification=None, reverse_balance=None, balance_side=None, posting_side=None, account_group=None, account_categories=None, direct_posting=None, is_inactive=None, job_process_option=None, branch_code=None):
        account_number = str(account_number).replace('-', '')
        # search GL account
        self.accounting_bank_account_definition_simple_search(account_number)
        if account_number:
            self.assert_table_data('Account number', 1, account_number)
        # view GL account
        self.click_table_menu('View', 1)
        self.wait_for_button_available('Modify')
        self.assert_form_title('ACT-Bank Account Definition-View')
        # verify value tab 'General'
        if account_level:
            self.bo_assert_select('Account level', account_level)
        if currency_code:
            self.bo_assert_select('Currency code', currency_code)
        if account_number:
            self.bo_assert_text('Account number', account_number)
        if account_name:
            self.bo_assert_text('Account name', account_name)
        if short_account_name:
            self.bo_assert_text('Short account name', short_account_name)
        if laos_name is not None or thai_name is not None or khmer_name is not None or vietnamese_name is not None:
            collap_name = 'Other name'
            self.bo_click_collap(collap_name)
            if laos_name:
                self.bo_assert_text_multi(collap_name, 'Laos name', laos_name)
            if thai_name:
                self.bo_assert_text_multi(collap_name, 'Thai name', thai_name)
            if khmer_name:
                self.bo_assert_text_multi(collap_name, 'Khmer name', khmer_name)
            if vietnamese_name:
                self.bo_assert_text_multi(collap_name, 'Vietnamese name', vietnamese_name)
        if account_classification:
            self.bo_assert_select('Account classification', account_classification)
        if reverse_balance:
            self.bo_assert_select('Reverse balance', reverse_balance)
        if balance_side:
            self.bo_assert_select('Balance side', balance_side)
        if posting_side:
            self.bo_assert_select('Posting side', posting_side)
        if account_group:
            self.bo_assert_select('Account group', account_group)
        if account_categories:
            self.bo_assert_select('Account categories', account_categories)
        if direct_posting:
            self.bo_assert_select('Direct posting', direct_posting)
        if is_inactive:
            self.bo_assert_select('Is Inactive', is_inactive)
        if job_process_option:
            self.bo_assert_select('Job process option', job_process_option)
        if branch_code:
            self.assertEqual(str(self.bo_get_select('Branch Code')).split(' - ')[0], branch_code)
        print('View account number: ' + account_number)
        return account_number

    def accounting_bank_account_definition_update(self, account_number, account_level=None, currency_code=None, account_name=None, short_account_name=None, laos_name=None, thai_name=None, khmer_name=None, vietnamese_name=None, account_classification=None, reverse_balance=None, balance_side=None, posting_side=None, account_group=None, account_categories=None, direct_posting=None, is_inactive=None, job_process_option=None, branch_code=None):
        self.accounting_bank_account_definition_view(account_number)
        self.wait_loading()
        self.click_button('Modify')
        # update value tab 'General'
        if account_name:
            self.bo_write_text('Account name', account_name)
        if short_account_name:
            self.bo_write_text('Short account name', short_account_name)
        if laos_name is not None or thai_name is not None or khmer_name is not None or vietnamese_name is not None:
            collap_name = 'Other name'
            self.bo_click_collap(collap_name)
            if laos_name:
                self.bo_write_text_multi(collap_name, 'Laos name', laos_name)
            if thai_name:
                self.bo_write_text_multi(collap_name, 'Thai name', thai_name)
            if khmer_name:
                self.bo_write_text_multi(collap_name, 'Khmer name', khmer_name)
            if vietnamese_name:
                self.bo_write_text_multi(collap_name, 'Vietnamese name', vietnamese_name)
        if account_classification:
            self.bo_select('Account classification', account_classification)
        if reverse_balance:
            self.bo_select('Reverse balance', reverse_balance)
        if balance_side:
            self.bo_select('Balance side', balance_side)
        if posting_side:
            self.bo_select('Posting side', posting_side)
        if account_group:
            self.bo_select('Account group', account_group)
        if account_categories:
            self.bo_select('Account categories', account_categories)
        if direct_posting:
            self.bo_select('Direct posting', direct_posting)
        if is_inactive:
            self.bo_select('Is Inactive', is_inactive)
        if job_process_option:
            self.bo_select('Job process option', job_process_option)
        # click 'Save'
        self.click_button('Save')
        self.assert_button_disable('Save')
        self.assert_notification('Saved successfully!')
        account_number = self.bo_get_text_data('Account number')
        # search and verify
        self.accounting_bank_account_definition_view(
            account_number=account_number,
            account_level=account_level,
            currency_code=currency_code,
            account_name=account_name,
            short_account_name=short_account_name,
            laos_name=laos_name,
            thai_name=thai_name,
            khmer_name=khmer_name,
            vietnamese_name=vietnamese_name,
            account_classification=account_classification,
            reverse_balance=reverse_balance,
            balance_side=balance_side,
            posting_side=posting_side,
            account_group=account_group,
            account_categories=account_categories,
            direct_posting=direct_posting,
            is_inactive=is_inactive,
            job_process_option=job_process_option,
            branch_code=branch_code
        )
        print('Updated account number: ' + account_number)
        return account_number

    def accounting_bank_account_definition_delete(self, account_number):
        account_number = str(account_number).replace('-', '')
        # search GL account
        self.accounting_bank_account_definition_simple_search(account_number)
        if account_number:
            self.assert_table_data('Account number', 1, account_number)
        # delete GL account
        self.click_table_menu('Delete', 1)
        self.wait_loading()
        self.click_button_in_popup('Yes')
        self.assert_notification('Deleted successfully')
        # search and verify
        self.accounting_bank_account_definition_simple_search(account_number)
        self.assert_search_not_found()
        print('Account number: ' + account_number)
        return account_number

    def check_gl_account_not_exist(self, account_number):
        account_number = str(account_number).replace('-', '')
        # search GL account
        self.accounting_bank_account_definition_simple_search(account_number)
        if (self.get_text_notification(timeout=3) == 'Data not found'):
            return True
        else:
            return False

    def add_gl_level_9_use_for_testing(self, branch_code, currency_code, account_number):
        """
        If the account number already exists, do not add it.
        """
        account_name = f'GL Test ({currency_code})'
        self.accounting_bank_account_definition_add(
            account_level='9-Ninth level of system chart (Details account)',
            currency_code=currency_code,
            account_number=account_number,
            account_name=account_name,
            short_account_name=account_name,
            direct_posting='Yes',
            is_inactive='No',
            branch_code=branch_code
        )

# -------------------------- handle BO - PAYMENT --------------------------


# -------------------------- handle common methods --------------------------
    def check_serial_number_not_exist(self, generated_number_from, generated_number_to, prefix, s_type=None):
        self.stock_inventory_advanced_search(prefix, generated_number_from, generated_number_to, s_type)
        if (self.get_text_notification(timeout=5) == 'Data not found'):
            return True
        else:
            return False

    def gen_serial_number(self, prefix, s_type, index):
        """
        Gen serial number use for stock
        Args:
            prefix (str): prefix of stock.
            s_type (str): stock type.
            index (int): the number of next serial number, 0 means gen one number only, 9: means gen 10 numbers, 24: means gen 25 numbers.
        Returns:
            Tuple ([str, str]): from number, to number. include prefix and format of stock number XX-000000.
        """
        while True:
            # Generate a random number with the desired format
            generated_number_from = f"7{random.randint(0, 99999):05}"
            generated_number_to = f"{int(generated_number_from) + index:05}"
            # Check if the generated number exists; if not, break the loop
            if self.check_serial_number_not_exist(generated_number_from, generated_number_to, prefix=prefix, s_type=s_type):
                break
        generated_number_from = f"{prefix}-{generated_number_from}"
        generated_number_to = f"{prefix}-{generated_number_to}"
        return generated_number_from, generated_number_to

    def get_list_serial_number(self, prefix, number_from, number_to):
        start = int(str(number_from).split('-')[1])
        end = int(str(number_to).split('-')[1])
        list_serial_numbers = [f"{prefix}-{num:06}" for num in range(start, end + 1)] # because the range() function in Python generates numbers up to but not including the end value
        return list_serial_numbers

    def get_next_serial_number(self, prefix, stock_number, index):
        serial_number = str(stock_number).replace(prefix+'-', '')
        next_serial_number = f"{int(serial_number) + index}"
        next_stock_number = f"{prefix}-{next_serial_number}"
        return next_stock_number

    def get_serial_number_no_refix(self, serial_number):
        """
        format: 'XX000000' or 'XX-000000'.

        Args:
            serial_number: input serial number have prefix.

        Returns:
            serial_number have no prefix: 000000 or None if serial_number have format incorrect.
        """
        serial_number = str(serial_number).replace('-', '')
        if len(serial_number) == 8:
            return serial_number[2:]
        elif len(serial_number) == 6:
            return serial_number
        else:
            return None

    def deposit_account_number_mask(self, account_number):
        account_number = str(account_number).replace('-', '')
        if len(account_number) < 12:
            log.warn("Account number must be at least 12 digits long")
            return ''
        # Format the string as XX-XXX-XXXXXX-X
        account_number_mask = f"{account_number[:2]}-{account_number[2:5]}-{account_number[5:11]}-{account_number[11:]}"
        return account_number_mask

    def treasury_account_number_mask(self, account_number):
        account_number = str(account_number).replace('-', '')
        if len(account_number) < 12:
            log.warn("Account number must be at least 12 digits long")
            return ''
        # Format the string as XXX-XX-XXXXXXX
        account_number_mask = f"{account_number[:3]}-{account_number[3:5]}-{account_number[5:]}"
        return account_number_mask

    def trade_account_number_mask(self, account_number):
        account_number = str(account_number).replace('-', '')
        if len(account_number) < 15:
            log.warn("Account number must be at least 15 digits long")
            return ''
        # Format the string as XXX-X-XX-XX-XXXXXX-X
        account_number_mask = (
            f"{account_number[:3]}-{account_number[3:4]}-"
            f"{account_number[4:6]}-{account_number[6:8]}-"
            f"{account_number[8:14]}-{account_number[14:]}"
        )
        return account_number_mask

    def customer_code_mask(self, customer_code):
        customer_code = str(customer_code).replace('-', '')
        if len(customer_code) < 8:
            log.warn("Customer code must be at least 8 digits long")
            return ''
        # Format the string as X-X-XXXXXX
        customer_code_mask = f"{customer_code[:1]}-{customer_code[1:2]}-{customer_code[2:]}"
        return customer_code_mask

    def gl_account_number_mask(self, gl_account_number):
        gl_account_number = str(gl_account_number).replace('-', '')
        if len(gl_account_number) < 18:
            log.warn("GL account number must be at least 18 digits long")
            return ''
        # Format the string as XXX-XXXXXXXXXXXXX-XX
        gl_account_number_mask = f"{gl_account_number[:3]}-{gl_account_number[3:16]}-{gl_account_number[16:]}"
        return gl_account_number_mask

    def add_fees(self, ifc_codes, values, total_fee=None):
        """
        Adds multiple fees based on lists of fee codes and corresponding values.

        Args:
            ifc_codes (list): A list of fee codes. Ex: ['101', '102', '103']
            values (list): A list of corresponding fee values. Ex: ['100.00', '0.1', '1,000.54']
            total_fee (str): Ex: 'Total Amount = 1,100.64'
        """
        if len(ifc_codes) != len(values):
            print('Error: The number of fee codes and values do not match.')
            return
        for ifc_code, value in zip(ifc_codes, values):
            self.click_button('Add')
            self.wait_loading()
            self.fo_write_text_group('Interest/fee/charge code', ifc_code)
            self.wait_loading()
            self.fo_write_number('Value', str(value).replace(',', ''))
            self.wait_loading()
            self.click_button('Apply')
            self.wait_loading()
        if total_fee:
            self.assert_total_fee_table_data(total_fee)

    def add_extension_group_entry(self, i, replace_bys, system_account_names, business_lines, customer_sectors=None, customer_resident_statuss=None, sub_products=None, bank_identifications=None, replace_code=None):
        self.click_button_in_tab('Add')
        self.write_textarea('Replace by', replace_bys[i])
        self.write_textarea('System account name', system_account_names[i])
        if replace_code:
            self.select('Replace code', replace_code)
        # Lấy từng giá trị tương ứng nếu có
        conditions = [
            ('Customer sector', customer_sectors[i] if customer_sectors else None),
            ('Customer resident status', customer_resident_statuss[i] if customer_resident_statuss else None),
            ('Business line', business_lines[i]),
            ('Sub product', sub_products[i] if sub_products else None),
            ('Bank Identification', bank_identifications[i] if bank_identifications else None)
        ]
        if any(value is not None for _, value in conditions):
            self.bo_click_collap('Condition account of group')
            for label, value in conditions:
                if value is not None:
                    self.select(label, value)
        self.click_button_in_tab('Apply')

    def add_gls_entry(self, i, sys_account_names, account_aliass, coa_accounts=None):
        self.click_button_in_tab('Add')
        self.write_textarea('Sys Account Name', sys_account_names[i])
        if coa_accounts:
            self.write_textarea('COA Account', coa_accounts[i])
        self.write_textarea('Account Alias', account_aliass[i])
        self.click_button_in_tab('Apply')

    def format_number(self, number):
        number = str(number).replace(',', '')
        number = float(number)
        if number.is_integer():
            return str(int(number))
        else:
            return str(number)

    def assert_posting_debit_account_number(self, index, expected):
        self.assert_table_data_posting('Debit', 'Account number', index=index, expected=expected)

    def assert_posting_debit_amount(self, index, expected):
        self.assert_table_data_posting('Debit', 'Amount', index=index, expected=expected)

    def assert_posting_credit_account_number(self, index, expected):
        self.assert_table_data_posting('Credit', 'Account number', index=index, expected=expected)

    def assert_posting_credit_amount(self, index, expected):
        self.assert_table_data_posting('Credit', 'Amount', index=index, expected=expected)

    def assert_posting_data(self, expected_debits=None, expected_credits=None):
        """
        Hàm tổng quát để kiểm tra dữ liệu trong bảng Posting cho cả Debit và Credit theo thứ tự nhóm của cặp Posting.

        Args:
            self: Tham chiếu đến đối tượng chứa các hàm assert.
            expected_debits (list, optional): Danh sách các dictionary hoặc tuple chứa dữ liệu mong đợi cho Debit.
                Mỗi phần tử trong danh sách đại diện cho một dòng và chứa thông tin cho 'Account number' và 'Amount'.
                Ví dụ: [{'Account number': '002-1101001010404-01', 'Amount': '1,000.00'}, ...]
                Hoặc: [('002-1101001010404-01', '1,000.00'), ...]
                Defaults to None.
            expected_credits (list, optional): Danh sách tương tự như expected_debits nhưng dành cho Credit.
                Defaults to None.
        """
        if expected_debits:
            for index, expected_data in enumerate(expected_debits, start=1):
                if isinstance(expected_data, dict):
                    expected_account = expected_data.get('Account number')
                    expected_amount = expected_data.get('Amount')
                elif isinstance(expected_data, (tuple, list)) and len(expected_data) == 2:
                    expected_account, expected_amount = expected_data
                else:
                    raise ValueError(f"Invalid format for expected debit data at index {index}: {expected_data}")

                if expected_account is not None:
                    self.assert_posting_debit_account_number(str(index), self.gl_account_number_mask(expected_account))
                if expected_amount is not None:
                    self.assert_posting_debit_amount(str(index), str(expected_amount))

        if expected_credits:
            for index, expected_data in enumerate(expected_credits, start=1):
                if isinstance(expected_data, dict):
                    expected_account = expected_data.get('Account number')
                    expected_amount = expected_data.get('Amount')
                elif isinstance(expected_data, (tuple, list)) and len(expected_data) == 2:
                    expected_account, expected_amount = expected_data
                else:
                    raise ValueError(f"Invalid format for expected credit data at index {index}: {expected_data}")

                if expected_account is not None:
                    self.assert_posting_credit_account_number(str(index), self.gl_account_number_mask(expected_account))
                if expected_amount is not None:
                    self.assert_posting_credit_amount(str(index), str(expected_amount))

        # # Cách sử dụng hàm mới:
        # def test_posting_with_variable_rows(self):
        #     trade_gl_number = "002-1101001010404-01"
        #     sg_bg_amount = "1,000.00"
        #     liability_gl_number = "002-2020301010202-01"
        #     cash_gl_number = "003-1010301000101-01"
        #     total_fee_amount = "1,000.00"
        #     ifcc_gl_number = "003-1101001010202-01"

        #     # Ví dụ với 2 dòng Debit và 2 dòng Credit
        #     expected_data_1 = {
        #         'expected_debits': [
        #             {'Account number': trade_gl_number, 'Amount': sg_bg_amount},
        #             {'Account number': cash_gl_number, 'Amount': total_fee_amount},
        #         ],
        #         'expected_credits': [
        #             {'Account number': liability_gl_number, 'Amount': sg_bg_amount},
        #             {'Account number': ifcc_gl_number, 'Amount': total_fee_amount},
        #         ],
        #     }
        #     self.assert_posting_data(**expected_data_1)

        #     # Ví dụ với 3 dòng Debit và 1 dòng Credit
        #     expected_data_2 = {
        #         'expected_debits': [
        #             (trade_gl_number, sg_bg_amount),
        #             (cash_gl_number, total_fee_amount),
        #             ('Debit Account 3', 'Debit Amount 3'),
        #         ],
        #         'expected_credits': [
        #             ('Credit Account 1', 'Credit Amount 1'),
        #         ],
        #     }
        #     self.assert_posting_data(**expected_data_2)

        #     # Ví dụ chỉ có Debit
        #     expected_data_3 = {
        #         'expected_debits': [
        #             {'Account number': trade_gl_number, 'Amount': sg_bg_amount},
        #         ],
        #     }
        #     self.assert_posting_data(**expected_data_3)

        #     # Ví dụ chỉ có Credit
        #     expected_data_4 = {
        #         'expected_credits': [
        #             {'Account number': liability_gl_number, 'Amount': sg_bg_amount},
        #             {'Account number': ifcc_gl_number, 'Amount': total_fee_amount},
        #             {'Account number': 'Credit Account 3', 'Amount': 'Credit Amount 3'},
        #             {'Account number': 'Credit Account 4', 'Amount': 'Credit Amount 4'},
        #         ],
        #     }
        #     self.assert_posting_data(**expected_data_4)
