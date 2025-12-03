from webui_test.case import *

class DepositActions(TestCase):

# -------------------------- handle FO - DEPOSIT --------------------------
    # DPT_OPN: 1100: Open new deposit account
    def dpt_opn(self, customer_type=None, customer_code=None, relation_customers=None, catalogue_code=None, customer_segmentation=None, business_purpose_code=None, to_account_number=None, agent_hub_referral=None, employer_organization_name=None, reason_of_account_opening=None, safe_deposit_locker_number=None, relationship_manager=None, description=None, i_m_banking=None, mpu_card=None, passbook_cheque_book=None, wallet=None, account_number=None, catalogue_name=None, deposit_type=None, deposit_sub_type=None, deposit_purpose=None, account_holder_name=None, rollover_option=None, auto_transfer_option=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
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
        if safe_deposit_locker_number:
            self.fo_write_text('Safe Deposit Locker Number', safe_deposit_locker_number)
        self.key_escape()
        if relationship_manager:
            self.fo_select('Relationship Manager', relationship_manager)
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_write_text('Description', description)
        if i_m_banking is None or i_m_banking == '':
            i_m_banking = False
        if i_m_banking:
            self.fo_click_checkbox('I/M Banking')
        if mpu_card is None or mpu_card == '':
            mpu_card = False
        if mpu_card:
            self.fo_click_checkbox('MPU Card')
        if passbook_cheque_book is None or passbook_cheque_book == '':
            passbook_cheque_book = False
        if passbook_cheque_book:
            self.fo_click_checkbox('Passbook/Cheque Book')
        if wallet is None or wallet == '':
            wallet = False
        if wallet:
            self.fo_click_checkbox('Wallet')
        if account_number:
            self.fo_assert_value_group('Account number', self.deposit_account_number_mask(account_number))
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
            self.check_notification('Saved successfully!')
            self.close_voucher()
            if expected_posting:
                self.assert_posting_data(**expected_posting)
            transaction_references=self.assert_transaction_number_not_null()
            print(f'Transaction references DPT_OPN: {transaction_references}')
            account_number_out=self.fo_get_value_group('Account number')
            print(f'Account number: {account_number_out}')
            return transaction_references, account_number_out

    def dpt_opn_view(self, transaction_references, customer_type=None, customer_code=None, relation_customers=None, catalogue_code=None, customer_segmentation=None, business_purpose_code=None, to_account_number=None, agent_hub_referral=None, employer_organization_name=None, reason_of_account_opening=None, safe_deposit_locker_number=None, relationship_manager=None, description=None, i_m_banking=None, mpu_card=None, passbook_cheque_book=None, wallet=None, account_number=None, catalogue_name=None, deposit_type=None, deposit_sub_type=None, deposit_purpose=None, account_holder_name=None, rollover_option=None, auto_transfer_option=None, expected_posting=None):
        self.transaction_view(transaction_references, '1100: Open new deposit account')
        # compare value
        if customer_type:
            self.fo_assert_select('Customer type', customer_type)
        if customer_code:
            self.fo_assert_value('Customer code', self.customer_code_mask(customer_code))
        if relation_customers:
            self.fo_assert_select_multi('Relation customers', relation_customers)
        if catalogue_code:
            self.fo_assert_value('Catalogue code', catalogue_code)
        if customer_segmentation:
            self.fo_assert_select('Customer segmentation', customer_segmentation)
        if business_purpose_code:
            self.fo_assert_text_group('Business Purpose Code', business_purpose_code)
        if to_account_number:
            self.fo_assert_value_group('To Account number', self.deposit_account_number_mask(to_account_number))
        if agent_hub_referral:
            self.fo_assert_value_group('Agent hub referral', agent_hub_referral)
        if employer_organization_name:
            self.fo_assert_text('Employer Organization Name', employer_organization_name)
        if reason_of_account_opening:
            self.fo_assert_text('Reason of Account Opening', reason_of_account_opening)
        if safe_deposit_locker_number:
            self.fo_assert_text('Safe Deposit Locker Number', safe_deposit_locker_number)
        if relationship_manager:
            self.fo_assert_select('Relationship Manager', relationship_manager)
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_assert_text('Description', description)
        if i_m_banking is None or i_m_banking == '':
            i_m_banking = False
        if i_m_banking is not None or i_m_banking != '':
            self.fo_assert_checkbox('I/M Banking', i_m_banking)
        if mpu_card is None or mpu_card == '':
            mpu_card = False
        if mpu_card is not None or mpu_card != '':
            self.fo_assert_checkbox('MPU Card', mpu_card)
        if passbook_cheque_book is None or passbook_cheque_book == '':
            passbook_cheque_book = False
        if passbook_cheque_book is not None or passbook_cheque_book != '':
            self.fo_assert_checkbox('Passbook/Cheque Book', passbook_cheque_book)
        if wallet is None or wallet == '':
            wallet = False
        if wallet is not None or wallet != '':
            self.fo_assert_checkbox('Wallet', wallet)
        if account_number:
            self.fo_assert_value_group('Account number', self.deposit_account_number_mask(account_number))
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
        if expected_posting:
            self.assert_posting_data(**expected_posting)
        self.fo_assert_checkbox('Caution!  There is no doubt that banks may be used as a means of Money Laundering/ Terrorist Financing/ Proliferation of Weapons of Mass Destruction.', True)
        transaction_references=self.assert_transaction_number_not_null()
        print(f'F8: Transaction references DPT_OPN: {transaction_references}')
        account_number_out=self.fo_get_value_group('Account number')
        print(f'F8: Account number: {account_number_out}')
        return transaction_references, account_number_out

    def dpt_opn_error(self, customer_type=None, customer_code=None, catalogue_code=None, reason_of_account_opening=None, error_message=None, list_error_message=None):
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
        if catalogue_code:
            self.fo_write('Catalogue code', catalogue_code)
        # verify error
        if error_message:
            self.wait_loading()
            self.assert_notification(error_message)
            self.assert_button_disable('Accept')
            print('Transaction verify alert failed!')
        if list_error_message:
            self.wait_loading()
            if customer_code:
                self.write_text_input_non_tab('Customer code', customer_code, need_tab='N')
            if reason_of_account_opening:
                self.fo_write_text('Reason of Account Opening', reason_of_account_opening)
            self.wait_loading()
            self.fo_click_checkbox('Caution!  There is no doubt that banks may be used as a means of Money Laundering/ Terrorist Financing/ Proliferation of Weapons of Mass Destruction.')
            self.wait_loading()
            # click 'Accept'
            self.click_button('Accept')
            self.assert_error_message()
            self.assert_list_error_message(list_error_message)
            print('Transaction verify accept failed!')

    def dpt_opn_lookup(self, customer_type=None, customer_code=None, relation_customers=None, catalogue_code=None, customer_segmentation=None, business_purpose_code=None, to_account_number=None, agent_hub_referral=None, employer_organization_name=None, reason_of_account_opening=None, safe_deposit_locker_number=None, relationship_manager=None, description=None, i_m_banking=None, mpu_card=None, passbook_cheque_book=None, wallet=None, account_number=None, catalogue_name=None, deposit_type=None, deposit_sub_type=None, deposit_purpose=None, account_holder_name=None, rollover_option=None, auto_transfer_option=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
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
            self.lookup_data_text(
                title='Customer code',
                value_search_code=self.no_mask(customer_code),
                value_code=self.no_mask(customer_code),
            )
        self.key_escape()
        if relation_customers:
            self.fo_select_multi('Relation customers', relation_customers)
        if catalogue_code:
            self.lookup_data_text(
                title='Catalogue code',
                value_search_code=catalogue_code,
                value_code=catalogue_code,
            )
        self.key_escape()
        if customer_segmentation:
            self.fo_select('Customer segmentation', customer_segmentation)
        if business_purpose_code:
            self.lookup_data_text(
                title='Business Purpose Code',
                value_search_code=business_purpose_code,
                value_code=business_purpose_code,
            )
        if to_account_number:
            self.lookup_data_text(
                title='To Account number',
                value_search_code=self.no_mask(to_account_number),
                value_code=self.no_mask(to_account_number),
            )
        if agent_hub_referral:
            self.lookup_data_text(
                title='Agent hub referral',
                value_search_code=agent_hub_referral,
                value_code=agent_hub_referral,
            )
        if employer_organization_name:
            self.fo_write_text('Employer Organization Name', employer_organization_name)
        if reason_of_account_opening:
            self.fo_write_text('Reason of Account Opening', reason_of_account_opening)
        if safe_deposit_locker_number:
            self.fo_write_text('Safe Deposit Locker Number', safe_deposit_locker_number)
        self.key_escape()
        if relationship_manager:
            self.fo_select('Relationship Manager', relationship_manager)
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_write_text('Description', description)
        if i_m_banking is None or i_m_banking == '':
            i_m_banking = False
        if i_m_banking:
            self.fo_click_checkbox('I/M Banking')
        if mpu_card is None or mpu_card == '':
            mpu_card = False
        if mpu_card:
            self.fo_click_checkbox('MPU Card')
        if passbook_cheque_book is None or passbook_cheque_book == '':
            passbook_cheque_book = False
        if passbook_cheque_book:
            self.fo_click_checkbox('Passbook/Cheque Book')
        if wallet is None or wallet == '':
            wallet = False
        if wallet:
            self.fo_click_checkbox('Wallet')
        if account_number:
            self.fo_assert_value_group('Account number', self.deposit_account_number_mask(account_number))
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
            self.check_notification('Saved successfully!')
            self.close_voucher()
            if expected_posting:
                self.assert_posting_data(**expected_posting)
            transaction_references=self.assert_transaction_number_not_null()
            print(f'Transaction references DPT_OPN: {transaction_references}')
            account_number_out=self.fo_get_value_group('Account number')
            print(f'Account number: {account_number_out}')
            return transaction_references, account_number_out

    # DPT_APR: Approve deposit account
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
            self.fo_assert_value_group('Linkage account number', self.deposit_account_number_mask(linkage_account_number))
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
            self.check_notification('Saved successfully!')
            self.close_voucher()
            if expected_posting:
                self.assert_posting_data(**expected_posting)
            transaction_references=self.assert_transaction_number_not_null()
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
            self.fo_assert_value_group('Linkage account number', self.deposit_account_number_mask(linkage_account_number))
        if created_by:
            self.fo_assert_select('Created by', created_by)
        if expected_posting:
            self.assert_posting_data(**expected_posting)
        transaction_references=self.assert_transaction_number_not_null()
        print(f'F8: Transaction references DPT_APR: {transaction_references}')
        account_number_out=self.fo_get_value_group('Account number')
        print(f'F8: Account number: {account_number_out}')
        return transaction_references, account_number_out

    # DPT_REJ: Reject deposit account 
    def dpt_rej(self, account_number=None, description=None, account_holder_name=None, account_holding_branch_name=None, catalogue_code=None, catalogue_name=None, customer_segmentation=None, deposit_type=None, deposit_sub_type=None, created_by=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.open_fo('DPT_REJ', 'Reject deposit account ')
        self.wait_for_button_available('Accept')
        self.assert_form_title('Reject deposit account ')
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
            self.check_notification('Saved successfully!')
            self.close_voucher()
            if expected_posting:
                self.assert_posting_data(**expected_posting)
            transaction_references=self.assert_transaction_number_not_null()
            print(f'Transaction references DPT_REJ: {transaction_references}')
            account_number_out=self.fo_get_value_group('Account number')
            print(f'Account number: {account_number_out}')
            return transaction_references, account_number_out

    def dpt_rej_view(self, transaction_references, account_number=None, description=None, account_holder_name=None, account_holding_branch_name=None, catalogue_code=None, catalogue_name=None, customer_segmentation=None, deposit_type=None, deposit_sub_type=None, created_by=None, expected_posting=None):
        self.transaction_view(transaction_references, 'Reject deposit account ')
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
        if created_by:
            self.fo_assert_select('Created by', created_by)
        if expected_posting:
            self.assert_posting_data(**expected_posting)
        transaction_references=self.assert_transaction_number_not_null()
        print(f'F8: Transaction references DPT_REJ: {transaction_references}')
        account_number_out=self.fo_get_value_group('Account number')
        print(f'F8: Account number: {account_number_out}')
        return transaction_references, account_number_out

    # DPT_CDP: 1110: Cash deposit
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
            self.fo_write_number('Amount deposit', amount_deposit)
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
            self.check_notification('Saved successfully!')
            self.close_voucher()
            if expected_posting:
                self.assert_posting_data(**expected_posting)
            transaction_references=self.assert_transaction_number_not_null()
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
        if account_holding_branch_name:
            self.fo_assert_text('Account holding branch name', account_holding_branch_name)
        if depositor_name:
            self.fo_assert_text('Depositor name', depositor_name)
        if expected_posting:
            self.assert_posting_data(**expected_posting)
        self.fo_assert_checkbox('Caution!  There is no doubt that banks may be used as a means of Money Laundering/ Terrorist Financing/ Proliferation of Weapons of Mass Destruction.', True)
        transaction_references=self.assert_transaction_number_not_null()
        print(f'F8: Transaction references DPT_CDP: {transaction_references}')
        account_number_out=self.fo_get_value_group('Account number')
        print(f'F8: Account number: {account_number_out}')
        return transaction_references, account_number_out

    # DPT_MDP: 1112: Miscellaneous deposit
    def dpt_mdp(self, account_number=None, amount_deposit=None, debit_accounting=None, depositor_name=None, depositor_code=None, depositor_address=None, mobile_phone=None, nrc=None, description=None, account_holding_branch_name=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.open_fo('DPT_MDP', '1112: Miscellaneous deposit')
        self.wait_for_button_available('Accept')
        self.assert_form_title('1112: Miscellaneous deposit')
        # enter value
        if account_number:
            self.fo_write_group('Account number', self.no_mask(account_number))
            self.wait_loading()
        if amount_deposit:
            self.fo_write_number_group('Amount Deposit', amount_deposit)
            self.wait_loading()
        if debit_accounting:
            self.fo_write_group('Debit accounting', self.no_mask(debit_accounting))
            self.wait_loading()
        if depositor_name:
            self.fo_write_text('Depositor name', depositor_name)
        if depositor_code:
            self.fo_write('Depositor code', self.no_mask(depositor_code))
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
        if ifc_codes:
            self.add_fees(ifc_codes, values, total_fee)
        if account_holding_branch_name:
            self.fo_assert_text(' Account holding branch name', account_holding_branch_name)
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
            self.check_notification('Saved successfully!')
            self.close_voucher()
            if expected_posting:
                self.assert_posting_data(**expected_posting)
            transaction_references=self.assert_transaction_number_not_null()
            print(f'Transaction references DPT_MDP: {transaction_references}')
            account_number_out=self.fo_get_value_group('Account number')
            print(f'Account number: {account_number_out}')
            debit_accounting_out=self.fo_get_value_group('Debit accounting')
            print(f'Debit accounting: {debit_accounting_out}')
            return transaction_references, account_number_out, debit_accounting_out

    def dpt_mdp_view(self, transaction_references, account_number=None, amount_deposit=None, debit_accounting=None, depositor_name=None, depositor_code=None, depositor_address=None, mobile_phone=None, nrc=None, description=None, account_holding_branch_name=None, expected_posting=None):
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
        if account_holding_branch_name:
            self.fo_assert_text(' Account holding branch name', account_holding_branch_name)
        if expected_posting:
            self.assert_posting_data(**expected_posting)
        transaction_references=self.assert_transaction_number_not_null()
        print(f'F8: Transaction references DPT_MDP: {transaction_references}')
        account_number_out=self.fo_get_value_group('Account number')
        print(f'F8: Account number: {account_number_out}')
        debit_accounting_out=self.fo_get_value_group('Debit accounting')
        print(f'F8: Debit accounting: {debit_accounting_out}')
        return transaction_references, account_number_out, debit_accounting_out

    # DPT_TRF: 1130: Transfer from deposit account to deposit account
    def dpt_trf(self, debit_account=None, amount=None, credit_account=None, debit_account_name=None, customer_code=None, customer_address=None, mobile_phone=None, nrc=None, description=None, account_holding_branch_name=None, passbook_number=None, balance_debit_account=None, available_balance_debit_account=None, total_fee_on_form=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.open_fo('DPT_TRF', '1130: Transfer from deposit account to deposit account')
        self.wait_for_button_available('Accept')
        self.assert_form_title('1130: Transfer from deposit account to deposit account')
        # enter value
        if debit_account:
            self.fo_write_group('Debit account', self.no_mask(debit_account))
            self.wait_loading()
        if amount:
            self.fo_write_number('Amount', amount)
            self.wait_loading()
        if credit_account:
            self.fo_write_group('Credit account', self.no_mask(credit_account))
            self.wait_loading()
        if debit_account_name:
            self.fo_write_text('Debit account name', debit_account_name)
        if customer_code:
            self.fo_write('Customer code', customer_code)
        if customer_address:
            self.fo_write_text('Customer address', customer_address)
        if mobile_phone:
            self.fo_click_collap('Customer description')
            self.fo_write_text_multi('Customer description', 'Mobile phone', mobile_phone)
        if nrc:
            self.fo_click_collap('Customer description')
            self.fo_write_text_multi('Customer description', 'NRC', nrc)
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_write_text('Description', description)
        if account_holding_branch_name:
            self.fo_assert_text('Account holding branch name', account_holding_branch_name)
        if passbook_number:
            self.fo_assert_text('Passbook number', self.stock_number_no_mask(passbook_number))
        if balance_debit_account:
            self.fo_assert_value('Balance debit account', balance_debit_account)
        if available_balance_debit_account:
            self.fo_assert_value('Available balance debit account', available_balance_debit_account)
        if total_fee_on_form:
            self.fo_assert_value('Total fee', total_fee_on_form)
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
            self.check_notification('Saved successfully!')
            self.close_voucher()
            if expected_posting:
                self.assert_posting_data(**expected_posting)
            transaction_references=self.assert_transaction_number_not_null()
            print(f'Transaction references DPT_TRF: {transaction_references}')
            debit_account_out=self.fo_get_value_group('Debit account')
            print(f'Debit account: {debit_account_out}')
            credit_account_out=self.fo_get_value_group('Credit account')
            print(f'Credit account: {credit_account_out}')
            return transaction_references, debit_account_out, credit_account_out

    def dpt_trf_view(self, transaction_references, debit_account=None, amount=None, credit_account=None, debit_account_name=None, customer_code=None, customer_address=None, mobile_phone=None, nrc=None, description=None, account_holding_branch_name=None, passbook_number=None, balance_debit_account=None, available_balance_debit_account=None, total_fee_on_form=None, expected_posting=None):
        self.transaction_view(transaction_references, '1130: Transfer from deposit account to deposit account')
        # compare value
        if debit_account:
            self.fo_assert_value_group('Debit account', self.deposit_account_number_mask(debit_account))
        if amount:
            self.fo_assert_value('Amount', amount)
        if credit_account:
            self.fo_assert_value_group('Credit account', self.deposit_account_number_mask(credit_account))
        if debit_account_name:
            self.fo_assert_text('Debit account name', debit_account_name)
        if customer_code:
            self.fo_assert_value('Customer code', self.customer_code_mask(customer_code))
        if customer_address:
            self.fo_assert_text('Customer address', customer_address)
        if mobile_phone:
            self.fo_click_collap('Customer description')
            self.fo_assert_text_multi('Customer description', 'Mobile phone', mobile_phone)
        if nrc:
            self.fo_click_collap('Customer description')
            self.fo_assert_text_multi('Customer description', 'NRC', nrc)
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_assert_text('Description', description)
        if account_holding_branch_name:
            self.fo_assert_text('Account holding branch name', account_holding_branch_name)
        if passbook_number:
            self.fo_assert_text('Passbook number', self.stock_number_no_mask(passbook_number))
        if balance_debit_account:
            self.fo_assert_value('Balance debit account', balance_debit_account)
        if available_balance_debit_account:
            self.fo_assert_value('Available balance debit account', available_balance_debit_account)
        if total_fee_on_form:
            self.fo_assert_value('Total fee', total_fee_on_form)
        if expected_posting:
            self.assert_posting_data(**expected_posting)
        self.fo_assert_checkbox('Caution!  There is no doubt that banks may be used as a means of Money Laundering/ Terrorist Financing/ Proliferation of Weapons of Mass Destruction.', True)
        transaction_references=self.assert_transaction_number_not_null()
        print(f'F8: Transaction references DPT_TRF: {transaction_references}')
        debit_account_out=self.fo_get_value_group('Debit account')
        print(f'F8: Debit account: {debit_account_out}')
        credit_account_out=self.fo_get_value_group('Credit account')
        print(f'F8: Credit account: {credit_account_out}')
        return transaction_references, debit_account_out, credit_account_out

    # DPT_CWR: 1120: Cash withdrawal
    def dpt_cwr(self, account_number=None, withdraw_amount=None, withdrawer_name=None, withdrawer_id=None, withdrawer_address=None, mobile_phone=None, nrc=None, description=None, account_holding_branch_name=None, passbook_number=None, current_balance=None, available_balance=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.open_fo('DPT_CWR', '1120')
        self.wait_for_button_available('Accept')
        self.assert_form_title('1120: Cash withdrawal')
        # enter value
        if account_number:
            self.fo_write_group('Account number', self.no_mask(account_number))
            self.wait_loading()
        if withdraw_amount:
            self.fo_write_number('Withdraw amount', withdraw_amount)
            self.wait_loading()
        if withdrawer_name:
            self.fo_write_text('Withdrawer name', withdrawer_name)
        if withdrawer_id:
            self.fo_write('Withdrawer id', withdrawer_id)
        if withdrawer_address:
            self.fo_write_text('Withdrawer address', withdrawer_address)
        if mobile_phone:
            self.fo_click_collap('Withdrawer description')
            self.fo_write_text_multi('Withdrawer description', 'Mobile phone', mobile_phone)
        if nrc:
            self.fo_click_collap('Withdrawer description')
            self.fo_write_text_multi('Withdrawer description', 'NRC', nrc)
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_write_text('Description', description)
        if ifc_codes:
            self.add_fees(ifc_codes, values, total_fee)
        if account_holding_branch_name:
            self.fo_assert_text('Account holding branch name', account_holding_branch_name)
        if passbook_number:
            self.fo_assert_text('Passbook number', self.stock_number_no_mask(passbook_number))
        if current_balance:
            self.fo_assert_value('Current balance', current_balance)
        if available_balance:
            self.fo_assert_value('Available balance', available_balance)
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
            self.check_notification('Saved successfully!')
            self.close_voucher()
            if expected_posting:
                self.assert_posting_data(**expected_posting)
            transaction_references=self.assert_transaction_number_not_null()
            print(f'Transaction references DPT_CWR: {transaction_references}')
            account_number_out=self.fo_get_value_group('Account number')
            print(f'Account number: {account_number_out}')
            return transaction_references, account_number_out

    def dpt_cwr_view(self, transaction_references, account_number=None, withdraw_amount=None, withdrawer_name=None, withdrawer_id=None, withdrawer_address=None, mobile_phone=None, nrc=None, description=None, account_holding_branch_name=None, passbook_number=None, current_balance=None, available_balance=None, expected_posting=None):
        self.transaction_view(transaction_references, '1120: Cash withdrawal')
        # compare value
        if account_number:
            self.fo_assert_value_group('Account number', self.deposit_account_number_mask(account_number))
        if withdraw_amount:
            self.fo_assert_value('Withdraw amount', withdraw_amount)
        if withdrawer_name:
            self.fo_assert_text('Withdrawer name', withdrawer_name)
        if withdrawer_id:
            self.fo_assert_value('Withdrawer id', self.customer_code_mask(withdrawer_id))
        if withdrawer_address:
            self.fo_assert_text('Withdrawer address', withdrawer_address)
        if mobile_phone:
            self.fo_click_collap('Withdrawer description')
            self.fo_assert_text_multi('Withdrawer description', 'Mobile phone', mobile_phone)
        if nrc:
            self.fo_click_collap('Withdrawer description')
            self.fo_assert_text_multi('Withdrawer description', 'NRC', nrc)
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_assert_text('Description', description)
        if account_holding_branch_name:
            self.fo_assert_text('Account holding branch name', account_holding_branch_name)
        if passbook_number:
            self.fo_assert_text('Passbook number', self.stock_number_no_mask(passbook_number))
        if current_balance:
            self.fo_assert_value('Current balance', current_balance)
        if available_balance:
            self.fo_assert_value('Available balance', available_balance)
        if expected_posting:
            self.assert_posting_data(**expected_posting)
        self.fo_assert_checkbox('Caution!  There is no doubt that banks may be used as a means of Money Laundering/ Terrorist Financing/ Proliferation of Weapons of Mass Destruction.', True)
        transaction_references=self.assert_transaction_number_not_null()
        print(f'F8: Transaction references DPT_CWR: {transaction_references}')
        account_number_out=self.fo_get_value_group('Account number')
        print(f'F8: Account number: {account_number_out}')
        return transaction_references, account_number_out

    # DPT_MWR: 1122: Miscellaneous withdrawal
    def dpt_mwr(self, account_number=None, withdraw_amount=None, credit_accounting=None, withdrawer_name=None, withdrawer_code=None, withdrawer_address=None, mobile_phone=None, nrc=None, description=None, values_date=None, account_holding_branch_name=None, passbook_number=None, current_balance=None, available_balance=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.open_fo('DPT_MWR', '1122')
        self.wait_for_button_available('Accept')
        self.assert_form_title('1122: Miscellaneous withdrawal')
        # enter value
        if account_number:
            self.fo_write_group('Account number', self.no_mask(account_number))
            self.wait_loading()
        if withdraw_amount:
            self.fo_write_number('Withdraw amount', withdraw_amount)
            self.wait_loading()
        if credit_accounting:
            self.fo_write_group('Credit accounting', self.no_mask(credit_accounting))
            self.wait_loading()
        if withdrawer_name:
            self.fo_write_text('Withdrawer name', withdrawer_name)
        if withdrawer_code:
            self.fo_write('Withdrawer code', withdrawer_code)
        if withdrawer_address:
            self.fo_write_text('Withdrawer address', withdrawer_address)
        if mobile_phone:
            self.fo_click_collap('Withdrawer description')
            self.fo_write_text_multi('Withdrawer description', 'Mobile phone', mobile_phone)
        if nrc:
            self.fo_click_collap('Withdrawer description')
            self.fo_write_text_multi('Withdrawer description', 'NRC', nrc)
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_write_text('Description', description)
        if values_date:
            self.fo_write_date('Values date', values_date)
        if ifc_codes:
            self.add_fees(ifc_codes, values, total_fee)
        if account_holding_branch_name:
            self.fo_assert_text('Account holding branch name', account_holding_branch_name)
        if passbook_number:
            self.fo_assert_text('Passbook number', self.stock_number_no_mask(passbook_number))
        if current_balance:
            self.fo_assert_value('Current balance', current_balance)
        if available_balance:
            self.fo_assert_value('Available balance', available_balance)
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
            self.check_notification('Saved successfully!')
            self.close_voucher()
            if expected_posting:
                self.assert_posting_data(**expected_posting)
            transaction_references=self.assert_transaction_number_not_null()
            print(f'Transaction references DPT_MWR: {transaction_references}')
            account_number_out=self.fo_get_value_group('Account number')
            print(f'Account number: {account_number_out}')
            credit_accounting_out=self.fo_get_value_group('Credit accounting')
            print(f'Credit accounting: {credit_accounting_out}')
            return transaction_references, account_number_out, credit_accounting_out

    def dpt_mwr_view(self, transaction_references, account_number=None, withdraw_amount=None, credit_accounting=None, withdrawer_name=None, withdrawer_code=None, withdrawer_address=None, mobile_phone=None, nrc=None, description=None, values_date=None, account_holding_branch_name=None, passbook_number=None, current_balance=None, available_balance=None, expected_posting=None):
        self.transaction_view(transaction_references, '1122: Miscellaneous withdrawal')
        # compare value
        if account_number:
            self.fo_assert_value_group('Account number', self.deposit_account_number_mask(account_number))
        if withdraw_amount:
            self.fo_assert_value('Withdraw amount', withdraw_amount)
        if credit_accounting:
            self.fo_assert_value_group('Credit accounting', self.gl_account_number_mask(credit_accounting))
        if withdrawer_name:
            self.fo_assert_text('Withdrawer name', withdrawer_name)
        if withdrawer_code:
            self.fo_assert_value('Withdrawer code', self.customer_code_mask(withdrawer_code))
        if withdrawer_address:
            self.fo_assert_text('Withdrawer address', withdrawer_address)
        if mobile_phone:
            self.fo_click_collap('Withdrawer description')
            self.fo_assert_text_multi('Withdrawer description', 'Mobile phone', mobile_phone)
        if nrc:
            self.fo_click_collap('Withdrawer description')
            self.fo_assert_text_multi('Withdrawer description', 'NRC', nrc)
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_assert_text('Description', description)
        if values_date:
            self.fo_assert_date('Values date', values_date)
        if account_holding_branch_name:
            self.fo_assert_text('Account holding branch name', account_holding_branch_name)
        if passbook_number:
            self.fo_assert_text('Passbook number', self.stock_number_no_mask(passbook_number))
        if current_balance:
            self.fo_assert_value('Current balance', current_balance)
        if available_balance:
            self.fo_assert_value('Available balance', available_balance)
        if expected_posting:
            self.assert_posting_data(**expected_posting)
        self.fo_assert_checkbox('Caution!  There is no doubt that banks may be used as a means of Money Laundering/ Terrorist Financing/ Proliferation of Weapons of Mass Destruction.', True)
        transaction_references=self.assert_transaction_number_not_null()
        print(f'F8: Transaction references DPT_MWR: {transaction_references}')
        account_number_out=self.fo_get_value_group('Account number')
        print(f'F8: Account number: {account_number_out}')
        credit_accounting_out=self.fo_get_value_group('Credit accounting')
        print(f'F8: Credit accounting: {credit_accounting_out}')
        return transaction_references, account_number_out, credit_accounting_out

    # DPT_CAS: 11841: Change account status
    def dpt_cas(self, account_number=None, new_status=None, description=None, account_holding_branch_name=None, current_status=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.open_fo('DPT_CAS', '11841')
        self.wait_for_button_available('Accept')
        self.assert_form_title('11841: Change account status')
        # enter value
        if account_number:
            self.fo_write_group('Account number', self.no_mask(account_number))
            self.wait_loading()
        self.key_escape()
        if new_status:
            self.fo_select('New status', new_status)
            self.wait_loading()
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_write_text('Description', description)
        if ifc_codes:
            self.add_fees(ifc_codes, values, total_fee)
        if account_holding_branch_name:
            self.fo_assert_text('Account holding branch name', account_holding_branch_name)
        if current_status:
            self.fo_assert_text('Current status', current_status)
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
            self.check_notification('Saved successfully!')
            self.close_voucher()
            if expected_posting:
                self.assert_posting_data(**expected_posting)
            transaction_references=self.assert_transaction_number_not_null()
            print(f'Transaction references DPT_CAS: {transaction_references}')
            account_number_out=self.fo_get_value_group('Account number')
            print(f'Account number: {account_number_out}')
            new_status_out=self.fo_get_select('New status')
            print(f'New status: {new_status_out}')
            return transaction_references, account_number_out, new_status_out

    def dpt_cas_view(self, transaction_references, account_number=None, new_status=None, description=None, account_holding_branch_name=None, current_status=None, expected_posting=None):
        self.transaction_view(transaction_references, '11841: Change account status')
        # compare value
        if account_number:
            self.fo_assert_value_group('Account number', self.deposit_account_number_mask(account_number))
        if new_status:
            self.fo_assert_select('New status', new_status)
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_assert_text('Description', description)
        if account_holding_branch_name:
            self.fo_assert_text('Account holding branch name', account_holding_branch_name)
        if current_status:
            self.fo_assert_text('Current status', current_status)
        if expected_posting:
            self.assert_posting_data(**expected_posting)
        transaction_references=self.assert_transaction_number_not_null()
        print(f'F8: Transaction references DPT_CAS: {transaction_references}')
        account_number_out=self.fo_get_value_group('Account number')
        print(f'F8: Account number: {account_number_out}')
        new_status_out=self.fo_get_select('New status')
        print(f'F8: New status: {new_status_out}')
        return transaction_references, account_number_out, new_status_out

    # DPT_BLK: 11840: Block account
    def dpt_blk(self, account_number=None, depositor_name=None, depositor_id=None, depositor_address=None, mobile_phone=None, nrc=None, description=None, block_reason=None, account_holding_branch_name=None, depositor_balance=None, depositor_currency=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.open_fo('DPT_BLK', '11840')
        self.wait_for_button_available('Accept')
        self.assert_form_title('11840: Block account')
        # enter value
        if account_number:
            self.fo_write_group('Account number', self.no_mask(account_number))
            self.wait_loading()
        if depositor_name:
            self.fo_write_text('Depositor name', depositor_name)
        if depositor_id:
            self.fo_write('Depositor id', depositor_id)
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
        self.key_escape()
        if block_reason:
            self.fo_select('Block reason', block_reason)
        if ifc_codes:
            self.add_fees(ifc_codes, values, total_fee)
        if account_holding_branch_name:
            self.fo_assert_text('Account holding branch name', account_holding_branch_name)
        if depositor_balance:
            self.fo_assert_value('Depositor balance', depositor_balance)
        if depositor_currency:
            self.fo_assert_select('Depositor currency', depositor_currency)
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
            self.check_notification('Saved successfully!')
            self.close_voucher()
            if expected_posting:
                self.assert_posting_data(**expected_posting)
            transaction_references=self.assert_transaction_number_not_null()
            print(f'Transaction references DPT_BLK: {transaction_references}')
            account_number_out=self.fo_get_value_group('Account number')
            print(f'Account number: {account_number_out}')
            return transaction_references, account_number_out

    def dpt_blk_view(self, transaction_references, account_number=None, depositor_name=None, depositor_id=None, depositor_address=None, mobile_phone=None, nrc=None, description=None, block_reason=None, account_holding_branch_name=None, depositor_balance=None, depositor_currency=None, expected_posting=None):
        self.transaction_view(transaction_references, '11840: Block account')
        # compare value
        if account_number:
            self.fo_assert_value_group('Account number', self.deposit_account_number_mask(account_number))
        if depositor_name:
            self.fo_assert_text('Depositor name', depositor_name)
        if depositor_id:
            self.fo_assert_value('Depositor id', self.customer_code_mask(depositor_id))
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
        if block_reason:
            self.fo_assert_select('Block reason', block_reason)
        if account_holding_branch_name:
            self.fo_assert_text('Account holding branch name', account_holding_branch_name)
        if depositor_balance:
            self.fo_assert_value('Depositor balance', depositor_balance)
        if depositor_currency:
            self.fo_assert_select('Depositor currency', depositor_currency)
        if expected_posting:
            self.assert_posting_data(**expected_posting)
        transaction_references=self.assert_transaction_number_not_null()
        print(f'F8: Transaction references DPT_BLK: {transaction_references}')
        account_number_out=self.fo_get_value_group('Account number')
        print(f'F8: Account number: {account_number_out}')
        return transaction_references, account_number_out

    # DPT_RLS: 11843: Release block account
    def dpt_rls(self, account_number=None, depositor_name=None, depositor_id=None, depositor_address=None, mobile_phone=None, nrc=None, description=None, account_holding_branch_name=None, block_reason=None, depositor_balance=None, depositor_currency=None, expired_date=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.open_fo('DPT_RLS', '11843')
        self.wait_for_button_available('Accept')
        self.assert_form_title('11843: Release block account')
        # enter value
        if account_number:
            self.fo_write_group('Account number', self.no_mask(account_number))
            self.wait_loading()
        if depositor_name:
            self.fo_write_text('Depositor name', depositor_name)
        if depositor_id:
            self.fo_write('Depositor id', depositor_id)
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
        if ifc_codes:
            self.add_fees(ifc_codes, values, total_fee)
        if account_holding_branch_name:
            self.fo_assert_text('Account holding branch name', account_holding_branch_name)
        if block_reason:
            self.fo_assert_select('Block reason', block_reason)
        if depositor_balance:
            self.fo_assert_value('Depositor balance', depositor_balance)
        if depositor_currency:
            self.fo_assert_select('Depositor currency', depositor_currency)
        if expired_date:
            self.fo_assert_date('Expired date', expired_date)
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
            self.check_notification('Saved successfully!')
            self.close_voucher()
            if expected_posting:
                self.assert_posting_data(**expected_posting)
            transaction_references=self.assert_transaction_number_not_null()
            print(f'Transaction references DPT_RLS: {transaction_references}')
            account_number_out=self.fo_get_value_group('Account number')
            print(f'Account number: {account_number_out}')
            return transaction_references, account_number_out

    def dpt_rls_view(self, transaction_references, account_number=None, depositor_name=None, depositor_id=None, depositor_address=None, mobile_phone=None, nrc=None, description=None, account_holding_branch_name=None, block_reason=None, depositor_balance=None, depositor_currency=None, expired_date=None, expected_posting=None):
        self.transaction_view(transaction_references, '11843: Release block account')
        # compare value
        if account_number:
            self.fo_assert_value_group('Account number', self.deposit_account_number_mask(account_number))
        if depositor_name:
            self.fo_assert_text('Depositor name', depositor_name)
        if depositor_id:
            self.fo_assert_value('Depositor id', self.customer_code_mask(depositor_id))
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
        if block_reason:
            self.fo_assert_select('Block reason', block_reason)
        if depositor_balance:
            self.fo_assert_value('Depositor balance', depositor_balance)
        if depositor_currency:
            self.fo_assert_select('Depositor currency', depositor_currency)
        if expired_date:
            self.fo_assert_date('Expired date', expired_date)
        if expected_posting:
            self.assert_posting_data(**expected_posting)
        transaction_references=self.assert_transaction_number_not_null()
        print(f'F8: Transaction references DPT_RLS: {transaction_references}')
        account_number_out=self.fo_get_value_group('Account number')
        print(f'F8: Account number: {account_number_out}')
        return transaction_references, account_number_out

    # DPT_IFC: DPT-1169: Adjust Deposit Interest
    def dpt_ifc(self, account_number=None, ifc_code=None, adjustment_amount=None, description=None, account_holding_branch_name=None, customer_code=None, account_name=None, accrual_interest_amount=None, interest_due_amount=None, interest_repayable_amount=None, current_ifc_amount=None, ifc_type=None, new_ifc_amount=None, adjusted_accrual_interest=None, adjusted_due_interest=None, adjusted_payable_interest=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.open_fo('DPT_IFC', '1169')
        self.wait_for_button_available('Accept')
        self.assert_form_title('DPT-1169: Adjust Deposit Interest')
        # enter value
        if account_number:
            self.fo_write_group('Account number', self.no_mask(account_number))
            self.wait_loading()
        if ifc_code:
            self.lookup_data('IFC code', 'Code', ifc_code)
            self.wait_loading()
        if adjustment_amount:
            self.fo_write_number('Adjustment amount', adjustment_amount)
            self.wait_loading()
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_write_text('Description', description)
        if ifc_codes:
            self.add_fees(ifc_codes, values, total_fee)
        if account_holding_branch_name:
            self.fo_assert_text('Account holding branch name', account_holding_branch_name)
        if customer_code:
            self.fo_assert_value('Customer code', self.customer_code_mask(customer_code))
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
            self.check_notification('Saved successfully!')
            self.close_voucher()
            if expected_posting:
                self.assert_posting_data(**expected_posting)
            transaction_references=self.assert_transaction_number_not_null()
            print(f'Transaction references DPT_IFC: {transaction_references}')
            account_number_out=self.fo_get_value_group('Account number')
            print(f'Account number: {account_number_out}')
            return transaction_references, account_number_out

    def dpt_ifc_view(self, transaction_references, account_number=None, ifc_code=None, adjustment_amount=None, description=None, account_holding_branch_name=None, customer_code=None, account_name=None, accrual_interest_amount=None, interest_due_amount=None, interest_repayable_amount=None, current_ifc_amount=None, ifc_type=None, new_ifc_amount=None, adjusted_accrual_interest=None, adjusted_due_interest=None, adjusted_payable_interest=None, expected_posting=None):
        self.transaction_view(transaction_references, 'DPT-1169: Adjust Deposit Interest')
        # compare value
        if account_number:
            self.fo_assert_value_group('Account number', self.deposit_account_number_mask(account_number))
        if ifc_code:
            self.fo_assert_text_group('IFC code', ifc_code)
        if adjustment_amount:
            self.fo_assert_value('Adjustment amount', adjustment_amount)
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_assert_text('Description', description)
        if account_holding_branch_name:
            self.fo_assert_text('Account holding branch name', account_holding_branch_name)
        if customer_code:
            self.fo_assert_value('Customer code', self.customer_code_mask(customer_code))
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
        if expected_posting:
            self.assert_posting_data(**expected_posting)
        transaction_references=self.assert_transaction_number_not_null()
        print(f'F8: Transaction references DPT_IFC: {transaction_references}')
        account_number_out=self.fo_get_value_group('Account number')
        print(f'F8: Account number: {account_number_out}')
        return transaction_references, account_number_out

    # DPT_CIP: 1140: Interest payment by cash
    def dpt_cip(self, account_number=None, gross_paid_interest_amount=None, gross_paid_interest_amount_update=None, receiver_name=None, receiver_id=None, receiver_address=None, mobile_phone=None, nrc=None, description=None, account_holding_branch_name=None, passbook_number=None, interest_payable_receivable=None, interest_due=None, interest_overdue=None, interest_not_paid=None, interest_amount=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.open_fo('DPT_CIP', '1140')
        self.wait_for_button_available('Accept')
        self.assert_form_title('1140: Interest payment by cash')
        # enter value
        if account_number:
            self.fo_write_group('Account number', self.no_mask(account_number))
            self.wait_loading()
        if gross_paid_interest_amount_update:
            self.fo_write_number('Gross paid interest amount', gross_paid_interest_amount_update)
        if receiver_name:
            self.fo_write_text('Receiver name', receiver_name)
        if receiver_id:
            self.fo_write('Receiver id', receiver_id)
        if receiver_address:
            self.fo_write_text('Receiver address', receiver_address)
        if mobile_phone:
            self.fo_click_collap('Receiver description')
            self.fo_write_text_multi('Receiver description', 'Mobile phone', mobile_phone)
        if nrc:
            self.fo_click_collap('Receiver description')
            self.fo_write_text_multi('Receiver description', 'NRC', nrc)
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_write_text('Description', description)
        if ifc_codes:
            self.add_fees(ifc_codes, values, total_fee)
        if gross_paid_interest_amount:
            self.fo_assert_value('Gross paid interest amount', gross_paid_interest_amount)
        if account_holding_branch_name:
            self.fo_assert_text('Account holding branch name', account_holding_branch_name)
        if passbook_number:
            self.fo_assert_text('Passbook number', self.stock_number_no_mask(passbook_number))
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
            self.check_notification('Saved successfully!')
            self.close_voucher()
            if expected_posting:
                self.assert_posting_data(**expected_posting)
            transaction_references=self.assert_transaction_number_not_null()
            print(f'Transaction references DPT_CIP: {transaction_references}')
            account_number_out=self.fo_get_value_group('Account number')
            print(f'Account number: {account_number_out}')
            return transaction_references, account_number_out

    def dpt_cip_view(self, transaction_references, account_number=None, gross_paid_interest_amount=None, gross_paid_interest_amount_update=None, receiver_name=None, receiver_id=None, receiver_address=None, mobile_phone=None, nrc=None, description=None, account_holding_branch_name=None, passbook_number=None, interest_payable_receivable=None, interest_due=None, interest_overdue=None, interest_not_paid=None, interest_amount=None, expected_posting=None):
        self.transaction_view(transaction_references, '1140: Interest payment by cash')
        # compare value
        if account_number:
            self.fo_assert_value_group('Account number', self.deposit_account_number_mask(account_number))
        if gross_paid_interest_amount:
            self.fo_assert_value('Gross paid interest amount', gross_paid_interest_amount)
        if gross_paid_interest_amount_update:
            self.fo_assert_value('Gross paid interest amount', gross_paid_interest_amount_update)
        if receiver_name:
            self.fo_assert_text('Receiver name', receiver_name)
        if receiver_id:
            self.fo_assert_value('Receiver id', self.customer_code_mask(receiver_id))
        if receiver_address:
            self.fo_assert_text('Receiver address', receiver_address)
        if mobile_phone:
            self.fo_click_collap('Receiver description')
            self.fo_assert_text_multi('Receiver description', 'Mobile phone', mobile_phone)
        if nrc:
            self.fo_click_collap('Receiver description')
            self.fo_assert_text_multi('Receiver description', 'NRC', nrc)
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_assert_text('Description', description)
        if account_holding_branch_name:
            self.fo_assert_text('Account holding branch name', account_holding_branch_name)
        if passbook_number:
            self.fo_assert_text('Passbook number', self.stock_number_no_mask(passbook_number))
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
        if expected_posting:
            self.assert_posting_data(**expected_posting)
        self.fo_assert_checkbox('Caution!  There is no doubt that banks may be used as a means of Money Laundering/ Terrorist Financing/ Proliferation of Weapons of Mass Destruction.', True)
        transaction_references=self.assert_transaction_number_not_null()
        print(f'F8: Transaction references DPT_CIP: {transaction_references}')
        account_number_out=self.fo_get_value_group('Account number')
        print(f'F8: Account number: {account_number_out}')
        return transaction_references, account_number_out

    # DPT_DIP: 1141: Interest payment to deposit account
    def dpt_dip(self, deposit_account=None, cross_interest_amount=None, cross_interest_amount_update=None, paid_to_this_deposit_account=None, depositor_name=None, depositor_id=None, depositor_address=None, mobile_phone=None, nrc=None, description=None, account_holding_branch_name=None, passbook_number=None, interest_payble_receivable=None, interest_due=None, interest_overdue=None, interest_not_paid=None, interest_amount=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.open_fo('DPT_DIP', '1141')
        self.wait_for_button_available('Accept')
        self.assert_form_title('1141: Interest payment to deposit account')
        # enter value
        if deposit_account:
            self.fo_write_group('Deposit account', self.no_mask(deposit_account))
            self.wait_loading()
        if cross_interest_amount_update:
            self.fo_write_number('Cross interest amount', cross_interest_amount_update)
        if paid_to_this_deposit_account:
            self.fo_write_group('Paid to this deposit account', self.no_mask(paid_to_this_deposit_account))
            self.wait_loading()
        if depositor_name:
            self.fo_write_text('Depositor name', depositor_name)
        if depositor_id:
            self.fo_write('Depositor id', depositor_id)
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
        if ifc_codes:
            self.add_fees(ifc_codes, values, total_fee)
        if cross_interest_amount:
            self.fo_assert_value('Cross interest amount', cross_interest_amount)
        if account_holding_branch_name:
            self.fo_assert_text('Account holding branch name', account_holding_branch_name)
        if passbook_number:
            self.fo_assert_text('Passbook number', self.stock_number_no_mask(passbook_number))
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
            self.check_notification('Saved successfully!')
            self.close_voucher()
            if expected_posting:
                self.assert_posting_data(**expected_posting)
            transaction_references=self.assert_transaction_number_not_null()
            print(f'Transaction references DPT_DIP: {transaction_references}')
            deposit_account_out=self.fo_get_value_group('Deposit account')
            print(f'Deposit account: {deposit_account_out}')
            paid_to_this_deposit_account_out=self.fo_get_value_group('Paid to this deposit account')
            print(f'Paid to this deposit account: {paid_to_this_deposit_account_out}')
            return transaction_references, deposit_account_out, paid_to_this_deposit_account_out

    def dpt_dip_view(self, transaction_references, deposit_account=None, cross_interest_amount=None, cross_interest_amount_update=None, paid_to_this_deposit_account=None, depositor_name=None, depositor_id=None, depositor_address=None, mobile_phone=None, nrc=None, description=None, account_holding_branch_name=None, passbook_number=None, interest_payble_receivable=None, interest_due=None, interest_overdue=None, interest_not_paid=None, interest_amount=None, expected_posting=None):
        self.transaction_view(transaction_references, '1141: Interest payment to deposit account')
        # compare value
        if deposit_account:
            self.fo_assert_value_group('Deposit account', self.deposit_account_number_mask(deposit_account))
        if cross_interest_amount:
            self.fo_assert_value('Cross interest amount', cross_interest_amount)
        if cross_interest_amount_update:
            self.fo_assert_value('Cross interest amount', cross_interest_amount_update)
        if paid_to_this_deposit_account:
            self.fo_assert_value_group('Paid to this deposit account', self.deposit_account_number_mask(paid_to_this_deposit_account))
        if depositor_name:
            self.fo_assert_text('Depositor name', depositor_name)
        if depositor_id:
            self.fo_assert_value('Depositor id', self.customer_code_mask(depositor_id))
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
        if passbook_number:
            self.fo_assert_text('Passbook number', self.stock_number_no_mask(passbook_number))
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
        if expected_posting:
            self.assert_posting_data(**expected_posting)
        self.fo_assert_checkbox('Caution!  There is no doubt that banks may be used as a means of Money Laundering/ Terrorist Financing/ Proliferation of Weapons of Mass Destruction.', True)
        transaction_references=self.assert_transaction_number_not_null()
        print(f'F8: Transaction references DPT_DIP: {transaction_references}')
        deposit_account_out=self.fo_get_value_group('Deposit account')
        print(f'F8: Deposit account: {deposit_account_out}')
        paid_to_this_deposit_account_out=self.fo_get_value_group('Paid to this deposit account')
        print(f'F8: Paid to this deposit account: {paid_to_this_deposit_account_out}')
        return transaction_references, deposit_account_out, paid_to_this_deposit_account_out

    # DPT_MIP: 1142: Miscellaneous interest payment
    def dpt_mip(self, account_number=None, gross_interest_paid_out=None, gross_interest_paid_out_update=None, gl_account=None, depositor_name=None, depositor_id=None, depositor_address=None, mobile_phone=None, nrc=None, description=None, account_holding_branch_name=None, passbook_number=None, interest_payble_receivable=None, interest_due=None, interest_overdue=None, interest_suspense=None, interest_not_paid=None, interest_amount=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.open_fo('DPT_MIP', '1142')
        self.wait_for_button_available('Accept')
        self.assert_form_title('1142: Miscellaneous interest payment')
        # enter value
        if account_number:
            self.fo_write_group('Account number', self.no_mask(account_number))
            self.wait_loading()
        if gross_interest_paid_out_update:
            self.fo_write_number('Gross interest paid out', gross_interest_paid_out_update)
            self.wait_loading()
        if gl_account:
            self.fo_write_group('GL account', self.no_mask(gl_account))
            self.wait_loading()
        if depositor_name:
            self.fo_write_text('Depositor name', depositor_name)
        if depositor_id:
            self.fo_write('Depositor id', depositor_id)
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
        if ifc_codes:
            self.add_fees(ifc_codes, values, total_fee)
        if gross_interest_paid_out:
            self.fo_assert_value('Gross interest paid out', gross_interest_paid_out)
        if account_holding_branch_name:
            self.fo_assert_text('Account holding branch name', account_holding_branch_name)
        if passbook_number:
            self.fo_assert_text('Passbook number', self.stock_number_no_mask(passbook_number))
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
            self.check_notification('Saved successfully!')
            self.close_voucher()
            if expected_posting:
                self.assert_posting_data(**expected_posting)
            transaction_references=self.assert_transaction_number_not_null()
            print(f'Transaction references DPT_MIP: {transaction_references}')
            account_number_out=self.fo_get_value_group('Account number')
            print(f'Account number: {account_number_out}')
            gl_account_out=self.fo_get_value_group('GL account')
            print(f'GL account: {gl_account_out}')
            return transaction_references, account_number_out, gl_account_out

    def dpt_mip_view(self, transaction_references, account_number=None, gross_interest_paid_out=None, gross_interest_paid_out_update=None, gl_account=None, depositor_name=None, depositor_id=None, depositor_address=None, mobile_phone=None, nrc=None, description=None, account_holding_branch_name=None, passbook_number=None, interest_payble_receivable=None, interest_due=None, interest_overdue=None, interest_suspense=None, interest_not_paid=None, interest_amount=None, expected_posting=None):
        self.transaction_view(transaction_references, '1142: Miscellaneous interest payment')
        # compare value
        if account_number:
            self.fo_assert_value_group('Account number', self.deposit_account_number_mask(account_number))
        if gross_interest_paid_out:
            self.fo_assert_value('Gross interest paid out', gross_interest_paid_out)
        if gross_interest_paid_out_update:
            self.fo_assert_value('Gross interest paid out', gross_interest_paid_out_update)
        if gl_account:
            self.fo_assert_value_group('GL account', self.gl_account_number_mask(gl_account))
        if depositor_name:
            self.fo_assert_text('Depositor name', depositor_name)
        if depositor_id:
            self.fo_assert_value('Depositor id', self.customer_code_mask(depositor_id))
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
        if passbook_number:
            self.fo_assert_text('Passbook number', self.stock_number_no_mask(passbook_number))
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
        if expected_posting:
            self.assert_posting_data(**expected_posting)
        self.fo_assert_checkbox('Caution!  There is no doubt that banks may be used as a means of Money Laundering/ Terrorist Financing/ Proliferation of Weapons of Mass Destruction.', True)
        transaction_references=self.assert_transaction_number_not_null()
        print(f'F8: Transaction references DPT_MIP: {transaction_references}')
        account_number_out=self.fo_get_value_group('Account number')
        print(f'F8: Account number: {account_number_out}')
        gl_account_out=self.fo_get_value_group('GL account')
        print(f'F8: GL account: {gl_account_out}')
        return transaction_references, account_number_out, gl_account_out

    # DPT_IPR: DPT_IPR: Payment Interest For Prepaid Fixed Deposit
    def dpt_ipr(self, account_number=None, credit_account=None, prepaid_interest=None, prepaid_interest_update=None, description=None, fee_collect_method=None, ifc_code=None, account_number_for_fee=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.open_fo('DPT_IPR', 'Prepaid Fixed Deposit')
        self.wait_for_button_available('Accept')
        self.assert_form_title('DPT_IPR: Payment Interest For Prepaid Fixed Deposit')
        # enter value
        if account_number:
            self.fo_write_group('Account number', self.no_mask(account_number))
            self.wait_loading()
        if credit_account:
            self.fo_write_group('Credit account', self.no_mask(credit_account))
            self.wait_loading()
        if prepaid_interest_update:
            self.fo_write_number('Prepaid interest', prepaid_interest_update)
            self.wait_loading()
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_write_text('Description', description)
        self.key_escape()
        if fee_collect_method:
            self.fo_select('Fee collect method', fee_collect_method)
        if account_number_for_fee:
            self.fo_write_text_group('Account number for fee', self.no_mask(account_number_for_fee))
            self.wait_loading()
        if ifc_codes:
            self.add_fees(ifc_codes, values, total_fee)
        if prepaid_interest:
            self.fo_assert_value('Prepaid interest', prepaid_interest)
        if ifc_code:
            self.fo_assert_text('IFC code', ifc_code)
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
            self.check_notification('Saved successfully!')
            self.close_voucher()
            if expected_posting:
                self.assert_posting_data(**expected_posting)
            transaction_references=self.assert_transaction_number_not_null()
            print(f'Transaction references DPT_IPR: {transaction_references}')
            account_number_out=self.fo_get_value_group('Account number')
            print(f'Account number: {account_number_out}')
            credit_account_out=self.fo_get_value_group('Credit account')
            print(f'Credit account: {credit_account_out}')
            return transaction_references, account_number_out, credit_account_out

    def dpt_ipr_view(self, transaction_references, account_number=None, credit_account=None, prepaid_interest=None, prepaid_interest_update=None, description=None, fee_collect_method=None, ifc_code=None, account_number_for_fee=None, expected_posting=None):
        self.transaction_view(transaction_references, 'DPT_IPR: Payment Interest For Prepaid Fixed Deposit')
        # compare value
        if account_number:
            self.fo_assert_value_group('Account number', self.deposit_account_number_mask(account_number))
        if credit_account:
            self.fo_assert_value_group('Credit account', self.deposit_account_number_mask(credit_account))
        if prepaid_interest:
            self.fo_assert_value('Prepaid interest', prepaid_interest)
        if prepaid_interest_update:
            self.fo_assert_value('Prepaid interest', prepaid_interest_update)
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_assert_text('Description', description)
        if fee_collect_method:
            self.fo_assert_select('Fee collect method', fee_collect_method)
        if ifc_code:
            self.fo_assert_text('IFC code', ifc_code)
        if account_number_for_fee:
            self.fo_assert_text_group('Account number for fee', account_number_for_fee)
        if expected_posting:
            self.assert_posting_data(**expected_posting)
        self.fo_assert_checkbox('Caution!  There is no doubt that banks may be used as a means of Money Laundering/ Terrorist Financing/ Proliferation of Weapons of Mass Destruction.', True)
        transaction_references=self.assert_transaction_number_not_null()
        print(f'F8: Transaction references DPT_IPR: {transaction_references}')
        account_number_out=self.fo_get_value_group('Account number')
        print(f'F8: Account number: {account_number_out}')
        credit_account_out=self.fo_get_value_group('Credit account')
        print(f'F8: Credit account: {credit_account_out}')
        return transaction_references, account_number_out, credit_account_out

    # DPT_EMK: 1180:Hold balance
    def dpt_emk(self, account_number=None, hold_amount=None, reference_code=None, depositor_name=None, depositor_id=None, depositor_address=None, mobile_phone=None, nrc=None, description=None, expired_date=None, account_holding_branch_name=None, amount_currency=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.open_fo('DPT_EMK', '1180')
        self.wait_for_button_available('Accept')
        self.assert_form_title('1180:Hold balance')
        # enter value
        if account_number:
            self.fo_write_group('Account number', self.no_mask(account_number))
            self.wait_loading()
        if hold_amount:
            self.fo_write_number('Hold amount', hold_amount)
            self.wait_loading()
        self.key_escape()
        if reference_code:
            self.fo_select('Reference code', reference_code)
        if depositor_name:
            self.fo_write_text('Depositor name', depositor_name)
        if depositor_id:
            self.fo_write('Depositor id', depositor_id)
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
        if expired_date:
            self.fo_write_date('Expired date', expired_date)
        if ifc_codes:
            self.add_fees(ifc_codes, values, total_fee)
        if account_holding_branch_name:
            self.fo_assert_text('Account holding branch name', account_holding_branch_name)
        if amount_currency:
            self.fo_assert_select('Amount currency', amount_currency)
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
            self.check_notification('Saved successfully!')
            self.close_voucher()
            if expected_posting:
                self.assert_posting_data(**expected_posting)
            transaction_references=self.assert_transaction_number_not_null()
            print(f'Transaction references DPT_EMK: {transaction_references}')
            account_number_out=self.fo_get_value_group('Account number')
            print(f'Account number: {account_number_out}')
            return transaction_references, account_number_out

    def dpt_emk_view(self, transaction_references, account_number=None, hold_amount=None, reference_code=None, depositor_name=None, depositor_id=None, depositor_address=None, mobile_phone=None, nrc=None, description=None, expired_date=None, account_holding_branch_name=None, amount_currency=None, expected_posting=None):
        self.transaction_view(transaction_references, '1180:Hold balance')
        # compare value
        if account_number:
            self.fo_assert_value_group('Account number', self.deposit_account_number_mask(account_number))
        if hold_amount:
            self.fo_assert_value('Hold amount', hold_amount)
        if reference_code:
            self.fo_assert_select('Reference code', reference_code)
        if depositor_name:
            self.fo_assert_text('Depositor name', depositor_name)
        if depositor_id:
            self.fo_assert_value('Depositor id', self.customer_code_mask(depositor_id))
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
        if expired_date:
            self.fo_assert_date('Expired date', expired_date)
        if account_holding_branch_name:
            self.fo_assert_text('Account holding branch name', account_holding_branch_name)
        if amount_currency:
            self.fo_assert_select('Amount currency', amount_currency)
        if expected_posting:
            self.assert_posting_data(**expected_posting)
        transaction_references=self.assert_transaction_number_not_null()
        print(f'F8: Transaction references DPT_EMK: {transaction_references}')
        account_number_out=self.fo_get_value_group('Account number')
        print(f'F8: Account number: {account_number_out}')
        return transaction_references, account_number_out

    # DPT_ERL: 11851:Release hold balance
    def dpt_erl(self, account_number=None, reference_code=None, earmark_amount=None, earmark_amount_update=None, depositor_name=None, depositor_id=None, depositor_address=None, mobile_phone=None, nrc=None, description=None, account_holding_branch_name=None, holding_amount=None, expired_date=None, cash_currency=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.open_fo('DPT_ERL', '11851')
        self.wait_for_button_available('Accept')
        self.assert_form_title('11851:Release hold balance')
        # enter value
        if account_number:
            self.fo_write_group('Account number', self.no_mask(account_number))
            self.wait_loading()
        self.key_escape()
        if reference_code:
            self.fo_select('Reference code', reference_code)
            self.wait_loading()
        if earmark_amount_update:
            self.fo_write_number('Earmark amount', earmark_amount_update)
            self.wait_loading()
        if depositor_name:
            self.fo_write_text('Depositor name', depositor_name)
        if depositor_id:
            self.fo_write('Depositor id', depositor_id)
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
        if ifc_codes:
            self.add_fees(ifc_codes, values, total_fee)
        if earmark_amount:
            self.fo_assert_value('Earmark amount', earmark_amount)
            self.wait_loading()
        if account_holding_branch_name:
            self.fo_assert_text('Account holding branch name', account_holding_branch_name)
        if holding_amount:
            self.fo_assert_value('Holding amount', holding_amount)
        if expired_date:
            self.fo_assert_date('Expired date', expired_date)
        if cash_currency:
            self.fo_assert_select('Cash currency', cash_currency)
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
            self.check_notification('Saved successfully!')
            self.close_voucher()
            if expected_posting:
                self.assert_posting_data(**expected_posting)
            transaction_references=self.assert_transaction_number_not_null()
            print(f'Transaction references DPT_ERL: {transaction_references}')
            account_number_out=self.fo_get_value_group('Account number')
            print(f'Account number: {account_number_out}')
            return transaction_references, account_number_out

    def dpt_erl_view(self, transaction_references, account_number=None, reference_code=None, earmark_amount=None, earmark_amount_update=None, depositor_name=None, depositor_id=None, depositor_address=None, mobile_phone=None, nrc=None, description=None, account_holding_branch_name=None, holding_amount=None, expired_date=None, cash_currency=None, expected_posting=None):
        self.transaction_view(transaction_references, '11851:Release hold balance')
        # compare value
        if account_number:
            self.fo_assert_value_group('Account number', self.deposit_account_number_mask(account_number))
        if reference_code:
            self.fo_assert_select('Reference code', reference_code)
        if earmark_amount:
            self.fo_assert_value('Earmark amount', earmark_amount)
        if earmark_amount_update:
            self.fo_assert_value('Earmark amount', earmark_amount_update)
        if depositor_name:
            self.fo_assert_text('Depositor name', depositor_name)
        if depositor_id:
            self.fo_assert_value('Depositor id', self.customer_code_mask(depositor_id))
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
        if holding_amount:
            self.fo_assert_value('Holding amount', holding_amount)
        if expired_date:
            self.fo_assert_date('Expired date', expired_date)
        if cash_currency:
            self.fo_assert_select('Cash currency', cash_currency)
        if expected_posting:
            self.assert_posting_data(**expected_posting)
        transaction_references=self.assert_transaction_number_not_null()
        print(f'F8: Transaction references DPT_ERL: {transaction_references}')
        account_number_out=self.fo_get_value_group('Account number')
        print(f'F8: Account number: {account_number_out}')
        return transaction_references, account_number_out

    # DPT_FEE: 1185: Fee collection by transfer
    def dpt_fee(self, account_number=None, amount_for_fee_calculation=None, description=None, account_holding_branch_name=None, passbook_number=None, total_fee_amount=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.open_fo('DPT_FEE', '1185')
        self.wait_for_button_available('Accept')
        self.assert_form_title('1185: Fee collection by transfer')
        # enter value
        if account_number:
            self.fo_write_group('Account number', self.no_mask(account_number))
            self.wait_loading()
        if amount_for_fee_calculation:
            self.fo_write_number('Amount for fee calculation', amount_for_fee_calculation)
            self.wait_loading()
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_write_text('Description', description)
        if ifc_codes:
            self.add_fees(ifc_codes, values, total_fee)
        if account_holding_branch_name:
            self.fo_assert_text('Account holding branch name', account_holding_branch_name)
        if passbook_number:
            self.fo_assert_text('Passbook number', self.stock_number_no_mask(passbook_number))
        if total_fee_amount:
            self.fo_assert_value('Total fee amount', total_fee_amount)
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
            self.check_notification('Saved successfully!')
            self.close_voucher()
            if expected_posting:
                self.assert_posting_data(**expected_posting)
            transaction_references=self.assert_transaction_number_not_null()
            print(f'Transaction references DPT_FEE: {transaction_references}')
            account_number_out=self.fo_get_value_group('Account number')
            print(f'Account number: {account_number_out}')
            return transaction_references, account_number_out

    def dpt_fee_view(self, transaction_references, account_number=None, amount_for_fee_calculation=None, description=None, account_holding_branch_name=None, passbook_number=None, total_fee_amount=None, expected_posting=None):
        self.transaction_view(transaction_references, '1185: Fee collection by transfer')
        # compare value
        if account_number:
            self.fo_assert_value_group('Account number', self.deposit_account_number_mask(account_number))
        if amount_for_fee_calculation:
            self.fo_assert_value('Amount for fee calculation', amount_for_fee_calculation)
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_assert_text('Description', description)
        if account_holding_branch_name:
            self.fo_assert_text('Account holding branch name', account_holding_branch_name)
        if passbook_number:
            self.fo_assert_text('Passbook number', self.stock_number_no_mask(passbook_number))
        if total_fee_amount:
            self.fo_assert_value('Total fee amount', total_fee_amount)
        if expected_posting:
            self.assert_posting_data(**expected_posting)
        self.fo_assert_checkbox('Caution!  There is no doubt that banks may be used as a means of Money Laundering/ Terrorist Financing/ Proliferation of Weapons of Mass Destruction.', True)
        transaction_references=self.assert_transaction_number_not_null()
        print(f'F8: Transaction references DPT_FEE: {transaction_references}')
        account_number_out=self.fo_get_value_group('Account number')
        print(f'F8: Account number: {account_number_out}')
        return transaction_references, account_number_out

    # DPT_FOC: 1184: Fee collection by cash for DD
    def dpt_foc(self, account_number=None, amount_for_fee_calculation=None, description=None, account_holding_branch_name=None, total_fee_amount=None, customer_code=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.open_fo('DPT_FOC', '1184')
        self.wait_for_button_available('Accept')
        self.assert_form_title('1184: Fee collection by cash for DD')
        # enter value
        if account_number:
            self.fo_write_group('Account number', self.no_mask(account_number))
            self.wait_loading()
        if amount_for_fee_calculation:
            self.fo_write_number('Amount for fee calculation', amount_for_fee_calculation)
            self.wait_loading()
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_write_text('Description', description)
        if ifc_codes:
            self.add_fees(ifc_codes, values, total_fee)
        if account_holding_branch_name:
            self.fo_assert_text('Account holding branch name', account_holding_branch_name)
        if total_fee_amount:
            self.fo_assert_value('Total fee amount', total_fee_amount)
        if customer_code:
            self.fo_assert_value('Customer code', self.customer_code_mask(customer_code))
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
            self.check_notification('Saved successfully!')
            self.close_voucher()
            if expected_posting:
                self.assert_posting_data(**expected_posting)
            transaction_references=self.assert_transaction_number_not_null()
            print(f'Transaction references DPT_FOC: {transaction_references}')
            account_number_out=self.fo_get_value_group('Account number')
            print(f'Account number: {account_number_out}')
            return transaction_references, account_number_out

    def dpt_foc_view(self, transaction_references, account_number=None, amount_for_fee_calculation=None, description=None, account_holding_branch_name=None, total_fee_amount=None, customer_code=None, expected_posting=None):
        self.transaction_view(transaction_references, '1184: Fee collection by cash for DD')
        # compare value
        if account_number:
            self.fo_assert_value_group('Account number', self.deposit_account_number_mask(account_number))
        if amount_for_fee_calculation:
            self.fo_assert_value('Amount for fee calculation', amount_for_fee_calculation)
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_assert_text('Description', description)
        if account_holding_branch_name:
            self.fo_assert_text('Account holding branch name', account_holding_branch_name)
        if total_fee_amount:
            self.fo_assert_value('Total fee amount', total_fee_amount)
        if customer_code:
            self.fo_assert_value('Customer code', self.customer_code_mask(customer_code))
        if expected_posting:
            self.assert_posting_data(**expected_posting)
        self.fo_assert_checkbox('Caution!  There is no doubt that banks may be used as a means of Money Laundering/ Terrorist Financing/ Proliferation of Weapons of Mass Destruction.', True)
        transaction_references=self.assert_transaction_number_not_null()
        print(f'F8: Transaction references DPT_FOC: {transaction_references}')
        account_number_out=self.fo_get_value_group('Account number')
        print(f'F8: Account number: {account_number_out}')
        return transaction_references, account_number_out

    # DPT_RCTM: DPT - Change Deposit Account Name And Relation Customers
    def dpt_rctm(self, account_number=None, new_account_name=None, description=None, customer_type=None, old_account_name=None, old_relation_customers=None, new_relation_customers=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.open_fo('DPT_RCTM', 'Change Deposit Account Name And Relation Customers')
        self.wait_for_button_available('Accept')
        self.assert_form_title('DPT - Change Deposit Account Name And Relation Customers')
        # enter value
        if account_number:
            self.fo_write_group('Account number', self.no_mask(account_number))
            self.wait_loading()
        if new_account_name:
            self.fo_write_text('New account name', new_account_name)
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_write_text('Description', description)
        self.key_escape()
        if new_relation_customers:
            self.fo_select_multi('New relation customers', new_relation_customers)
        if ifc_codes:
            self.add_fees(ifc_codes, values, total_fee)
        if customer_type:
            self.fo_assert_select('Customer type', customer_type)
        if old_account_name:
            self.fo_assert_text('Old account name', old_account_name)
        if old_relation_customers:
            self.fo_assert_select_multi('Old relation customers', old_relation_customers)
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
            self.check_notification('Saved successfully!')
            self.close_voucher()
            if expected_posting:
                self.assert_posting_data(**expected_posting)
            transaction_references=self.assert_transaction_number_not_null()
            print(f'Transaction references DPT_RCTM: {transaction_references}')
            account_number_out=self.fo_get_value_group('Account number')
            print(f'Account number: {account_number_out}')
            return transaction_references, account_number_out

    def dpt_rctm_view(self, transaction_references, account_number=None, new_account_name=None, description=None, customer_type=None, old_account_name=None, old_relation_customers=None, new_relation_customers=None, expected_posting=None):
        self.transaction_view(transaction_references, 'DPT - Change Deposit Account Name And Relation Customers')
        # compare value
        if account_number:
            self.fo_assert_value_group('Account number', self.deposit_account_number_mask(account_number))
        if new_account_name:
            self.fo_assert_text('New account name', new_account_name)
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_assert_text('Description', description)
        if customer_type:
            self.fo_assert_select('Customer type', customer_type)
        if old_account_name:
            self.fo_assert_text('Old account name', old_account_name)
        if old_relation_customers:
            self.fo_assert_select_multi('Old relation customers', old_relation_customers)
        if new_relation_customers:
            self.fo_assert_select_multi('New relation customers', new_relation_customers)
        if expected_posting:
            self.assert_posting_data(**expected_posting)
        self.fo_assert_checkbox('Caution!  There is no doubt that banks may be used as a means of Money Laundering/ Terrorist Financing/ Proliferation of Weapons of Mass Destruction.', True)
        transaction_references=self.assert_transaction_number_not_null()
        print(f'F8: Transaction references DPT_RCTM: {transaction_references}')
        account_number_out=self.fo_get_value_group('Account number')
        print(f'F8: Account number: {account_number_out}')
        return transaction_references, account_number_out

    # DPT_CLS: 1193: Close deposit account
    def dpt_cls(self, account_number=None, gross_paid_interest_amount=None, gross_paid_interest_amount_update=None, depositor_name=None, depositor_id=None, depositor_address=None, mobile_phone=None, nrc=None, description=None, account_holding_branch_name=None, passbook_number=None, balance=None, interest_payable_receivable=None, interest_due=None, interest_re_calculate=None, penalty_fee=None, balance_received=None, balance_received_update=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.open_fo('DPT_CLS', '1193')
        self.wait_for_button_available('Accept')
        self.assert_form_title('1193: Close deposit account')
        # enter value
        if account_number:
            self.fo_write_group('Account number', self.no_mask(account_number))
            self.wait_loading()
        if gross_paid_interest_amount_update:
            self.fo_write_number('Gross paid interest amount', gross_paid_interest_amount_update)
            self.wait_loading()
        if depositor_name:
            self.fo_write_text('Depositor name', depositor_name)
        if depositor_id:
            self.fo_write('Depositor id', depositor_id)
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
        if ifc_codes:
            self.add_fees(ifc_codes, values, total_fee)
        if gross_paid_interest_amount:
            self.fo_assert_value('Gross paid interest amount', gross_paid_interest_amount)
        if account_holding_branch_name:
            self.fo_assert_text('Account holding branch name', account_holding_branch_name)
        if passbook_number:
            self.fo_assert_text('Passbook number', self.stock_number_no_mask(passbook_number))
        if balance:
            self.fo_assert_value('Balance', balance)
        if interest_payable_receivable:
            self.fo_assert_value('Interest payable/receivable', interest_payable_receivable)
        if interest_due:
            self.fo_assert_value('Interest due', interest_due)
        if interest_re_calculate:
            self.fo_assert_value('Interest re-calculate', interest_re_calculate)
        if penalty_fee:
            self.fo_assert_value('Penalty fee', penalty_fee)
        if balance_received:
            self.fo_assert_value('Balance received', balance_received)
        if balance_received_update:
            self.fo_assert_value('Balance received', balance_received_update)
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
            self.check_notification('Saved successfully!')
            self.close_voucher()
            if expected_posting:
                self.assert_posting_data(**expected_posting)
            transaction_references=self.assert_transaction_number_not_null()
            print(f'Transaction references DPT_CLS: {transaction_references}')
            account_number_out=self.fo_get_value_group('Account number')
            print(f'Account number: {account_number_out}')
            return transaction_references, account_number_out

    def dpt_cls_view(self, transaction_references, account_number=None, gross_paid_interest_amount=None, gross_paid_interest_amount_update=None, depositor_name=None, depositor_id=None, depositor_address=None, mobile_phone=None, nrc=None, description=None, account_holding_branch_name=None, passbook_number=None, balance=None, interest_payable_receivable=None, interest_due=None, interest_re_calculate=None, penalty_fee=None, balance_received=None, balance_received_update=None, expected_posting=None):
        self.transaction_view(transaction_references, '1193: Close deposit account')
        # compare value
        if account_number:
            self.fo_assert_value_group('Account number', self.deposit_account_number_mask(account_number))
        if gross_paid_interest_amount:
            self.fo_assert_value('Gross paid interest amount', gross_paid_interest_amount)
        if gross_paid_interest_amount_update:
            self.fo_assert_value('Gross paid interest amount', gross_paid_interest_amount_update)
        if depositor_name:
            self.fo_assert_text('Depositor name', depositor_name)
        if depositor_id:
            self.fo_assert_value('Depositor id', self.customer_code_mask(depositor_id))
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
        if passbook_number:
            self.fo_assert_text('Passbook number', self.stock_number_no_mask(passbook_number))
        if balance:
            self.fo_assert_value('Balance', balance)
        if interest_payable_receivable:
            self.fo_assert_value('Interest payable/receivable', interest_payable_receivable)
        if interest_due:
            self.fo_assert_value('Interest due', interest_due)
        if interest_re_calculate:
            self.fo_assert_value('Interest re-calculate', interest_re_calculate)
        if penalty_fee:
            self.fo_assert_value('Penalty fee', penalty_fee)
        if balance_received:
            self.fo_assert_value('Balance received', balance_received)
        if balance_received_update:
            self.fo_assert_value('Balance received', balance_received_update)
        if expected_posting:
            self.assert_posting_data(**expected_posting)
        self.fo_assert_checkbox('Caution!  There is no doubt that banks may be used as a means of Money Laundering/ Terrorist Financing/ Proliferation of Weapons of Mass Destruction.', True)
        transaction_references=self.assert_transaction_number_not_null()
        print(f'F8: Transaction references DPT_CLS: {transaction_references}')
        account_number_out=self.fo_get_value_group('Account number')
        print(f'F8: Account number: {account_number_out}')
        return transaction_references, account_number_out

    def dpt_cls_error(self, account_number=None, gross_paid_interest_amount=None, error_message=None, list_error_message=None):
        # open form
        self.close_all_form()
        self.open_fo('DPT_CLS', '1193')
        self.wait_for_button_available('Accept')
        self.assert_form_title('1193: Close deposit account')
        # enter value
        if account_number:
            self.fo_write_group('Account number', self.no_mask(account_number))
            self.wait_loading()
        # verify error
        if error_message:
            self.wait_loading()
            self.assert_notification(error_message)
            self.assert_button_disable('Accept')
            print('Transaction verify alert failed!')
        if list_error_message:
            self.wait_loading()
            if gross_paid_interest_amount:
                self.fo_write_number('Gross paid interest amount', gross_paid_interest_amount)
            self.wait_loading()
            self.fo_click_checkbox('Caution!  There is no doubt that banks may be used as a means of Money Laundering/ Terrorist Financing/ Proliferation of Weapons of Mass Destruction.')
            self.wait_loading()
            # click 'Accept'
            self.click_button('Accept')
            self.assert_error_message()
            self.assert_list_error_message(list_error_message)
            print('Transaction verify accept failed!')

    # DPT_DLS: 1190: Close deposit account by deposit
    def dpt_dls(self, account_number=None, gross_paid_interest_amount=None, gross_paid_interest_amount_update=None, another_deposit_account=None, depositor_name=None, depositor_id=None, depositor_address=None, mobile_phone=None, nrc=None, description=None, account_holding_branch_name=None, passbook_number=None, balance=None, interest_payable_receivable=None, interest_due=None, interest_re_calculate=None, penalty_fee=None, balance_received=None, balance_received_update=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.open_fo('DPT_DLS', '1190')
        self.wait_for_button_available('Accept')
        self.assert_form_title('1190: Close deposit account by deposit')
        # enter value
        if account_number:
            self.fo_write_group('Account number', self.no_mask(account_number))
            self.wait_loading()
        if gross_paid_interest_amount_update:
            self.fo_write_number('Gross interest paid out', gross_paid_interest_amount_update)
            self.wait_loading()
        if another_deposit_account:
            self.fo_write_group('Another deposit account', self.no_mask(another_deposit_account))
            self.wait_loading()
        if depositor_name:
            self.fo_write_text('Depositor name', depositor_name)
        if depositor_id:
            self.fo_write('Depositor id', depositor_id)
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
        if ifc_codes:
            self.add_fees(ifc_codes, values, total_fee)
        if gross_paid_interest_amount:
            self.fo_assert_value('Gross interest paid out', gross_paid_interest_amount)
        if account_holding_branch_name:
            self.fo_assert_text('Account holding branch name', account_holding_branch_name)
        if passbook_number:
            self.fo_assert_text('Passbook number', self.stock_number_no_mask(passbook_number))
        if balance:
            self.fo_assert_value('Balance', balance)
        if interest_payable_receivable:
            self.fo_assert_value('Interest payable/receivable', interest_payable_receivable)
        if interest_due:
            self.fo_assert_value('Interest due', interest_due)
        if interest_re_calculate:
            self.fo_assert_value('Interest re-calculate', interest_re_calculate)
        if penalty_fee:
            self.fo_assert_value('Penalty fee', penalty_fee)
        if balance_received:
            self.fo_assert_value('Balance received', balance_received)
        if balance_received_update:
            self.fo_assert_value('Balance received', balance_received_update)
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
            self.check_notification('Saved successfully!')
            self.close_voucher()
            if expected_posting:
                self.assert_posting_data(**expected_posting)
            transaction_references=self.assert_transaction_number_not_null()
            print(f'Transaction references DPT_DLS: {transaction_references}')
            account_number_out=self.fo_get_value_group('Account number')
            print(f'Account number: {account_number_out}')
            another_deposit_account_out=self.fo_get_value_group('Another deposit account')
            print(f'Another deposit account: {another_deposit_account_out}')
            return transaction_references, account_number_out, another_deposit_account_out

    def dpt_dls_view(self, transaction_references, account_number=None, gross_paid_interest_amount=None, gross_paid_interest_amount_update=None, another_deposit_account=None, depositor_name=None, depositor_id=None, depositor_address=None, mobile_phone=None, nrc=None, description=None, account_holding_branch_name=None, passbook_number=None, balance=None, interest_payable_receivable=None, interest_due=None, interest_re_calculate=None, penalty_fee=None, balance_received=None, balance_received_update=None, expected_posting=None):
        self.transaction_view(transaction_references, '1190: Close deposit account by deposit')
        # compare value
        if account_number:
            self.fo_assert_value_group('Account number', self.deposit_account_number_mask(account_number))
        if gross_paid_interest_amount:
            self.fo_assert_value('Gross interest paid out', gross_paid_interest_amount)
        if gross_paid_interest_amount_update:
            self.fo_assert_value('Gross interest paid out', gross_paid_interest_amount_update)
        if another_deposit_account:
            self.fo_assert_value_group('Another deposit account', self.deposit_account_number_mask(another_deposit_account))
        if depositor_name:
            self.fo_assert_text('Depositor name', depositor_name)
        if depositor_id:
            self.fo_assert_value('Depositor id', self.customer_code_mask(depositor_id))
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
        if passbook_number:
            self.fo_assert_text('Passbook number', self.stock_number_no_mask(passbook_number))
        if balance:
            self.fo_assert_value('Balance', balance)
        if interest_payable_receivable:
            self.fo_assert_value('Interest payable/receivable', interest_payable_receivable)
        if interest_due:
            self.fo_assert_value('Interest due', interest_due)
        if interest_re_calculate:
            self.fo_assert_value('Interest re-calculate', interest_re_calculate)
        if penalty_fee:
            self.fo_assert_value('Penalty fee', penalty_fee)
        if balance_received:
            self.fo_assert_value('Balance received', balance_received)
        if balance_received_update:
            self.fo_assert_value('Balance received', balance_received_update)
        if expected_posting:
            self.assert_posting_data(**expected_posting)
        self.fo_assert_checkbox('Caution!  There is no doubt that banks may be used as a means of Money Laundering/ Terrorist Financing/ Proliferation of Weapons of Mass Destruction.', True)
        transaction_references=self.assert_transaction_number_not_null()
        print(f'F8: Transaction references DPT_DLS: {transaction_references}')
        account_number_out=self.fo_get_value_group('Account number')
        print(f'F8: Account number: {account_number_out}')
        another_deposit_account_out=self.fo_get_value_group('Another deposit account')
        print(f'F8: Another deposit account: {another_deposit_account_out}')
        return transaction_references, account_number_out, another_deposit_account_out

    def dpt_dls_error(self, account_number=None, another_deposit_account=None, error_message=None, list_error_message=None):
        # open form
        self.close_all_form()
        self.open_fo('DPT_DLS', '1190')
        self.wait_for_button_available('Accept')
        self.assert_form_title('1190: Close deposit account by deposit')
        # enter value
        if account_number:
            self.fo_write_group('Account number', self.no_mask(account_number))
            self.wait_loading()
        # verify error
        if error_message:
            self.wait_loading()
            self.assert_notification(error_message)
            self.assert_button_disable('Accept')
            print('Transaction verify alert failed!')
        if list_error_message:
            self.wait_loading()
            if another_deposit_account:
                self.fo_write_group('Another deposit account', self.no_mask(another_deposit_account))
            self.wait_loading()
            self.fo_click_checkbox('Caution!  There is no doubt that banks may be used as a means of Money Laundering/ Terrorist Financing/ Proliferation of Weapons of Mass Destruction.')
            self.wait_loading()
            # click 'Accept'
            self.click_button('Accept')
            self.assert_error_message()
            self.assert_list_error_message(list_error_message)
            print('Transaction verify accept failed!')

    # DPT_MLS: 1191: Close deposit account by miscellaneous
    def dpt_mls(self, account_number=None, gross_paid_interest_amount=None, gross_paid_interest_amount_update=None, depositor_name=None, depositor_id=None, depositor_address=None, mobile_phone=None, nrc=None, description=None, accounting_number=None, account_holding_branch_name=None, passbook_number=None, balance=None, interest_payable_receivable=None, interest_due=None, interest_re_calculate=None, penalty_fee=None, balance_received=None, balance_received_update=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.open_fo('DPT_MLS', '1191')
        self.wait_for_button_available('Accept')
        self.assert_form_title('1191: Close deposit account by miscellaneous')
        # enter value
        if account_number:
            self.fo_write_group('Account number', self.no_mask(account_number))
            self.wait_loading()
        if gross_paid_interest_amount_update:
            self.fo_write_number('Interest amount', gross_paid_interest_amount_update)
            self.wait_loading()
        if depositor_name:
            self.fo_write_text('Depositor name', depositor_name)
        if depositor_id:
            self.fo_write('Depositor id', depositor_id)
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
        if accounting_number:
            self.fo_write_group('Accounting number', str(accounting_number).replace('-', ''))
            self.wait_loading()
        if ifc_codes:
            self.add_fees(ifc_codes, values, total_fee)
        if gross_paid_interest_amount:
            self.fo_assert_value('Interest amount', gross_paid_interest_amount)
            self.wait_loading()
        if account_holding_branch_name:
            self.fo_assert_text('Account holding branch name', account_holding_branch_name)
        if passbook_number:
            self.fo_assert_text('Passbook number', self.stock_number_no_mask(passbook_number))
        if balance:
            self.fo_assert_value('Balance', balance)
        if interest_payable_receivable:
            self.fo_assert_value('Interest payable/receivable', interest_payable_receivable)
        if interest_due:
            self.fo_assert_value('Interest due', interest_due)
        if interest_re_calculate:
            self.fo_assert_value('Interest re-calculate', interest_re_calculate)
        if penalty_fee:
            self.fo_assert_value('Penalty fee', penalty_fee)
        if balance_received:
            self.fo_assert_value('Balance received', balance_received)
        if balance_received_update:
            self.fo_assert_value('Balance received', balance_received_update)
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
            self.check_notification('Saved successfully!')
            self.close_voucher()
            if expected_posting:
                self.assert_posting_data(**expected_posting)
            transaction_references=self.assert_transaction_number_not_null()
            print(f'Transaction references DPT_MLS: {transaction_references}')
            account_number_out=self.fo_get_value_group('Account number')
            print(f'Account number: {account_number_out}')
            accounting_number_out=self.fo_get_value_group('Accounting number')
            print(f'Accounting number: {accounting_number_out}')
            return transaction_references, account_number_out, accounting_number_out

    def dpt_mls_view(self, transaction_references, account_number=None, gross_paid_interest_amount=None, gross_paid_interest_amount_update=None, depositor_name=None, depositor_id=None, depositor_address=None, mobile_phone=None, nrc=None, description=None, accounting_number=None, account_holding_branch_name=None, passbook_number=None, balance=None, interest_payable_receivable=None, interest_due=None, interest_re_calculate=None, penalty_fee=None, balance_received=None, balance_received_update=None, expected_posting=None):
        self.transaction_view(transaction_references, '1191: Close deposit account by miscellaneous')
        # compare value
        if account_number:
            self.fo_assert_value_group('Account number', self.deposit_account_number_mask(account_number))
        if gross_paid_interest_amount:
            self.fo_assert_value('Interest amount', gross_paid_interest_amount)
        if gross_paid_interest_amount_update:
            self.fo_assert_value('Interest amount', gross_paid_interest_amount_update)
        if depositor_name:
            self.fo_assert_text('Depositor name', depositor_name)
        if depositor_id:
            self.fo_assert_value('Depositor id', self.customer_code_mask(depositor_id))
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
        if accounting_number:
            self.fo_assert_value_group('Accounting number', self.gl_account_number_mask(accounting_number))
        if account_holding_branch_name:
            self.fo_assert_text('Account holding branch name', account_holding_branch_name)
        if passbook_number:
            self.fo_assert_text('Passbook number', self.stock_number_no_mask(passbook_number))
        if balance:
            self.fo_assert_value('Balance', balance)
        if interest_payable_receivable:
            self.fo_assert_value('Interest payable/receivable', interest_payable_receivable)
        if interest_due:
            self.fo_assert_value('Interest due', interest_due)
        if interest_re_calculate:
            self.fo_assert_value('Interest re-calculate', interest_re_calculate)
        if penalty_fee:
            self.fo_assert_value('Penalty fee', penalty_fee)
        if balance_received:
            self.fo_assert_value('Balance received', balance_received)
        if balance_received_update:
            self.fo_assert_value('Balance received', balance_received_update)
        if expected_posting:
            self.assert_posting_data(**expected_posting)
        self.fo_assert_checkbox('Caution!  There is no doubt that banks may be used as a means of Money Laundering/ Terrorist Financing/ Proliferation of Weapons of Mass Destruction.', True)
        transaction_references=self.assert_transaction_number_not_null()
        print(f'F8: Transaction references DPT_MLS: {transaction_references}')
        account_number_out=self.fo_get_value_group('Account number')
        print(f'F8: Account number: {account_number_out}')
        accounting_number_out=self.fo_get_value_group('Accounting number')
        print(f'F8: Accounting number: {accounting_number_out}')
        return transaction_references, account_number_out, accounting_number_out

    def dpt_mls_error(self, account_number=None, accounting_number=None, error_message=None, list_error_message=None):
        # open form
        self.close_all_form()
        self.open_fo('DPT_MLS', '1191')
        self.wait_for_button_available('Accept')
        self.assert_form_title('1191: Close deposit account by miscellaneous')
        # enter value
        if account_number:
            self.fo_write_group('Account number', self.no_mask(account_number))
            self.wait_loading()
        # verify error
        if error_message:
            self.wait_loading()
            self.assert_notification(error_message)
            self.assert_button_disable('Accept')
            print('Transaction verify alert failed!')
        if list_error_message:
            self.wait_loading()
            if accounting_number:
                self.fo_write_group('Accounting number', self.no_mask(accounting_number))
            self.wait_loading()
            self.fo_click_checkbox('Caution!  There is no doubt that banks may be used as a means of Money Laundering/ Terrorist Financing/ Proliferation of Weapons of Mass Destruction.')
            self.wait_loading()
            # click 'Accept'
            self.click_button('Accept')
            self.assert_error_message()
            self.assert_list_error_message(list_error_message)
            print('Transaction verify accept failed!')

    # DPT_HIS: 1160: Transaction history inquiry
    def dpt_his(self, account_number, from_date=None, to_date=None, transaction_codes=None, expected_debits=None, expected_credits=None, expected_balances=None, expected_channels=None, expected_transaction_code=None, expected_transaction_codes=None, expected_debit=None, expected_credit=None, expected_balance=None, expected_channel=None, transaction_numbers=None, expected_transaction_number=None, expected_transaction_dates=None, expected_transaction_date=None, expected_created_bys=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.open_fo('DPT_HIS', '1160')
        self.wait_for_button_available('Accept')
        self.assert_form_title('1160: Transaction history inquiry')
        # enter value
        self.fo_write_group('Account number', self.no_mask(account_number))
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
            self.check_notification('Saved successfully!')
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
            transaction_references=self.assert_transaction_number_not_null()
            print(f'Transaction references DPT_HIS: {transaction_references}')
            deposit_account_mask=self.fo_get_value_group('Account number')
            print(f'Account number: {deposit_account_mask}')
            return transaction_references, deposit_account_mask

# -------------------------- handle BO - DEPOSIT --------------------------
    # DPT-IFC Item Definition
    def deposit_ifc_item_definition_simple_search(self, text):
        self.close_all_form()
        self.click_menu('Deposit', 'IFC', 'IFC Item Definition')
        self.wait_for_button_available('Search')
        self.assert_form_title('DPT-IFC Item Definition-Search')
        self.simple_search(text=text, placeholder='Search text')
        self.wait_loading()

    def deposit_ifc_item_definition_advanced_search(self, ifc_code_from=None, ifc_code_to=None, ifc_name=None, value_type=None, ifc_type=None, value_from=None, value_to=None, tenor_from=None, tenor_to=None, tenor_unit=None, active_condition=None, status=None):
        self.close_all_form()
        self.click_menu('Deposit', 'IFC', 'IFC Item Definition')
        self.wait_for_button_available('Search')
        self.assert_form_title('DPT-IFC Item Definition-Search')
        if ifc_code_from:
            self.adv_search_group('IFC code from', ifc_code_from)
        if ifc_code_to:
            self.adv_search_group('IFC code to', ifc_code_to)
        if ifc_name:
            self.adv_search_text('IFC name', ifc_name)
        self.key_escape()
        if value_type:
            self.adv_search_select('Value type', value_type)
        self.key_escape()
        if ifc_type:
            self.adv_search_select('IFC type', ifc_type)
        if value_from:
            self.adv_search_group('Value from', value_from)
        if value_to:
            self.adv_search_group('Value to', value_to)
        if tenor_from:
            self.adv_search_group('Tenor from', tenor_from)
        if tenor_to:
            self.adv_search_group('Tenor to', tenor_to)
        self.key_escape()
        if tenor_unit:
            self.adv_search_select('Tenor unit', tenor_unit)
        if active_condition:
            self.adv_search_text('Active condition', active_condition)
        self.key_escape()
        if status:
            self.adv_search_select('Status', status)
        self.click_button_search_advanced()
        self.wait_loading()

    def deposit_ifc_item_definition_add(self, ifc_code=None, ifc_name=None, ifc_type=None, ifc_sub_type=None, val_base=None, is_linked=None, value=None, ifc_linkage=None, ifc_operator=None, margin_value=None, value_type=None, currency_code=None, floor_value=None, ceiling_value=None, value_basis=None, tenor=None, tenor_unit=None, active_condition=None, rounding_rule=None, rounding_basis=None, rounding_num=None, share_fee=None, ifc_status=None, effect_date=None, effect_value=None, sys_account_names=None, account_aliass=None, list_transaction=None, list_error_message=None):
        # open form
        self.close_all_form()
        self.click_menu('Deposit', 'IFC', 'IFC Item Definition')
        self.wait_for_button_available('Add')
        self.click_button('Add')
        self.wait_for_button_available('Save')
        self.assert_form_title('DPT-IFC Item Definition-Add')
        # enter value
        self.bo_click_tab('General information')
        if ifc_name:
            self.bo_write_text('IFC name', ifc_name)
        self.key_escape()
        if ifc_type:
            self.bo_select('IFC type', ifc_type)
        self.key_escape()
        if ifc_sub_type:
            self.bo_select('IFC sub type', ifc_sub_type)
        self.key_escape()
        if val_base:
            self.bo_select('Val base', val_base)
        self.key_escape()
        if is_linked:
            self.bo_select('Is Linked', is_linked)
        if value:
            self.bo_write_number('Value', value)
        if ifc_linkage:
            self.bo_write_text_group('IFC linkage', ifc_linkage)
        self.key_escape()
        if ifc_operator:
            self.bo_select('IFC Operator', ifc_operator)
        if margin_value:
            self.bo_write_number('Margin value', margin_value)
        self.key_escape()
        if value_type:
            self.bo_select('Value type', value_type)
        self.key_escape()
        if currency_code:
            self.bo_select('Currency code', currency_code)
        if floor_value:
            self.bo_write_number('Floor value', floor_value)
        if ceiling_value:
            self.bo_write_number('Ceiling value', ceiling_value)
        if value_basis:
            self.bo_write_text('Value basis', value_basis)
        if tenor:
            self.bo_write_number_group('Tenor', tenor)
        self.key_escape()
        if tenor_unit:
            self.bo_select_group('Tenor unit', tenor_unit)
        if active_condition:
            self.bo_write_text('Active condition', active_condition)
        self.key_escape()
        if rounding_rule:
            self.bo_select('Rounding rule', rounding_rule)
        self.key_escape()
        if rounding_basis:
            self.bo_select('Rounding basis', rounding_basis)
        if rounding_num:
            self.bo_write_number('Rounding num', rounding_num)
        self.key_escape()
        if share_fee:
            self.bo_select('Share fee', share_fee)
        self.key_escape()
        if ifc_status:
            self.bo_select('IFC status', ifc_status)
        if effect_date:
            self.bo_write_date('Effect Date', effect_date)
        if effect_value:
            self.bo_write_number('Effect Value', effect_value)
        self.bo_click_tab('GLs information')
        if sys_account_names:
            count = len(sys_account_names)
            if not all(
                len(lst) == count for lst in [
                    account_aliass
                ]
            ):
                raise ValueError("All input lists must have the same length or be None.")
            for i in range(count):
                self.add_gls_entry(i, sys_account_names, account_aliass)
        self.bo_click_tab('List Transaction')
        self.key_escape()
        if list_transaction:
            self.bo_select_multi('List transaction', list_transaction)
        # assert value
        self.bo_click_tab('General information')
        if ifc_code:
            self.bo_assert_value('IFC code', ifc_code)
        self.wait_loading()
        # click 'Save'
        self.click_button('Save')
        if list_error_message:
        # verify error
            self.assert_error_message()
            self.assert_list_error_message(list_error_message)
            print('Action add failed!')
        else:
        # verify success
            self.assert_button_disable('Save')
            self.check_notification('Saved successfully!')
            self.bo_click_tab('General information')
            ifc_code_out=self.bo_get_value('IFC code')
            print(f'IFC code: {ifc_code_out}')
            return ifc_code_out

    def deposit_ifc_item_definition_view(self, ifc_code=None, ifc_name=None, ifc_type=None, ifc_sub_type=None, val_base=None, is_linked=None, value=None, ifc_linkage=None, ifc_operator=None, margin_value=None, value_type=None, currency_code=None, floor_value=None, ceiling_value=None, value_basis=None, tenor=None, tenor_unit=None, active_condition=None, rounding_rule=None, rounding_basis=None, rounding_num=None, share_fee=None, ifc_status=None, created_by=None, approved_by=None, effect_date=None, effect_value=None, expected_gls_sys_account_names=None, expected_gls_account_aliass=None, list_transaction=None):
        # search
        self.deposit_ifc_item_definition_advanced_search(ifc_code_from=ifc_code, ifc_code_to=ifc_code)
        self.assert_table_data('IFC code', 1, ifc_code)
        # view
        self.click_table_menu('View', 1)
        self.wait_for_button_available('Modify')
        self.assert_form_title('DPT-IFC Item Definition-View')
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

    def deposit_ifc_item_definition_update(self, ifc_code=None, ifc_name=None, ifc_type=None, ifc_sub_type=None, val_base=None, is_linked=None, value=None, ifc_linkage=None, ifc_operator=None, margin_value=None, value_type=None, currency_code=None, floor_value=None, ceiling_value=None, value_basis=None, tenor=None, tenor_unit=None, active_condition=None, rounding_rule=None, rounding_basis=None, rounding_num=None, share_fee=None, ifc_status=None, created_by=None, approved_by=None, effect_date=None, effect_value=None, list_transaction=None, list_error_message=None):
        # view
        self.deposit_ifc_item_definition_view(ifc_code=ifc_code)
        self.click_button('Modify')
        self.wait_loading()
        # update value
        self.bo_click_tab('General information')
        if ifc_name:
            self.bo_write_text('IFC name', ifc_name)
        self.key_escape()
        if ifc_sub_type:
            self.bo_select('IFC sub type', ifc_sub_type)
        self.key_escape()
        if val_base:
            self.bo_select('Val base', val_base)
        self.key_escape()
        if is_linked:
            self.bo_select('Is Linked', is_linked)
        if value:
            self.bo_write_number('Value', value)
        if ifc_linkage:
            self.bo_write_text_group('IFC linkage', ifc_linkage)
        self.key_escape()
        if ifc_operator:
            self.bo_select('IFC Operator', ifc_operator)
        if margin_value:
            self.bo_write_number('Margin value', margin_value)
        self.key_escape()
        if currency_code:
            self.bo_select('Currency code', currency_code)
        if floor_value:
            self.bo_write_number('Floor value', floor_value)
        if ceiling_value:
            self.bo_write_number('Ceiling value', ceiling_value)
        if value_basis:
            self.bo_write_text('Value basis', value_basis)
        if tenor:
            self.bo_write_number_group('Tenor', tenor)
        self.key_escape()
        if tenor_unit:
            self.bo_select_group('Tenor', tenor_unit)
        if active_condition:
            self.bo_write_text('Active condition', active_condition)
        self.key_escape()
        if rounding_rule:
            self.bo_select('Rounding rule', rounding_rule)
        self.key_escape()
        if rounding_basis:
            self.bo_select('Rounding basis', rounding_basis)
        if rounding_num:
            self.bo_write_number('Rounding num', rounding_num)
        self.key_escape()
        if share_fee:
            self.bo_select('Share fee', share_fee)
        self.key_escape()
        if ifc_status:
            self.bo_select('IFC status', ifc_status)
        if effect_date:
            self.bo_write_date('Effect Date', effect_date)
        if effect_value:
            self.bo_write_number('Effect Value', effect_value)
        self.bo_click_tab('List Transaction')
        self.key_escape()
        if list_transaction:
            self.bo_select_multi('List transaction', list_transaction)
        # assert value
        self.bo_click_tab('General information')
        if ifc_code:
            self.bo_assert_value('IFC code', ifc_code)
        if ifc_type:
            self.bo_assert_select('IFC type', ifc_type)
        if value_type:
            self.bo_assert_select('Value type', value_type)
        if created_by:
            self.bo_assert_text_group('Created by', created_by)
        if approved_by:
            self.bo_assert_text_group('Approved by', approved_by)
        self.wait_loading()
        # click 'Save'
        self.click_button('Save')
        if list_error_message:
        # verify error
            self.assert_error_message()
            self.assert_list_error_message(list_error_message)
            print('Action update failed!')
        else:
        # verify success
            self.assert_button_disable('Save')
            self.check_notification('Saved successfully!')
            self.bo_click_tab('General information')
            ifc_code_out=self.bo_get_value('IFC code')
            print(f'IFC code: {ifc_code_out}')
            return ifc_code_out

    def deposit_ifc_item_definition_delete(self, ifc_code, list_error_message=None, expected_message=None):
        # search
        self.deposit_ifc_item_definition_advanced_search(ifc_code_from=ifc_code, ifc_code_to=ifc_code)
        self.assert_table_data('IFC code', 1, ifc_code)
        # delete
        self.click_table_menu('Delete', 1)
        self.wait_loading()
        self.click_button_in_popup('Yes')
        if list_error_message:
        # verify error
            self.assert_error_message()
            self.assert_list_error_message(list_error_message)
            print(f"Action delete '{ifc_code}' failed!")
        else:
        # verify success
            if expected_message:
                self.assert_notification(expected_message)
            print(f'Deleted: {ifc_code}')
            return ifc_code

    # DPT-IFC Auto Fee
    def deposit_ifc_auto_fee_simple_search(self, text):
        self.close_all_form()
        self.click_menu('Deposit', 'IFC', 'IFC Auto Fee')
        self.wait_for_button_available('Search')
        self.assert_form_title('DPT-IFC Auto Fee-Search')
        self.simple_search(text=text, placeholder='Search text')
        self.wait_loading()

    def deposit_ifc_auto_fee_advanced_search(self, transaction_code=None, transaction_name=None, ifc_code=None, ifc_name=None):
        self.close_all_form()
        self.click_menu('Deposit', 'IFC', 'IFC Auto Fee')
        self.wait_for_button_available('Search')
        self.assert_form_title('DPT-IFC Auto Fee-Search')
        if transaction_code:
            self.adv_search_text('Transaction code', transaction_code)
        if transaction_name:
            self.adv_search_text('Transaction name', transaction_name)
        if ifc_code:
            self.adv_search_text('IFC code', ifc_code)
        if ifc_name:
            self.adv_search_text('IFC name', ifc_name)
        self.click_button_search_advanced()
        self.wait_loading()

    def deposit_ifc_auto_fee_add(self, transaction_code=None, ifc_code=None, condition=None, active=None, exchange=None, list_error_message=None):
        # open form
        self.close_all_form()
        self.click_menu('Deposit', 'IFC', 'IFC Auto Fee')
        self.wait_for_button_available('Add')
        self.click_button('Add')
        self.wait_for_button_available('Save')
        self.assert_form_title('DPT-IFC Auto Fee-Add')
        # enter value
        if transaction_code:
            self.bo_write_group_single('Transaction code', transaction_code)
        if ifc_code:
            self.bo_write_text_group_single('IFC code', ifc_code)
        if condition:
            self.bo_write_text_single('Condition', condition)
        if active is True:
            self.bo_click_checkbox_single('Active')
        if active is False:
            self.bo_click_uncheckbox_single('Active')
        if exchange is True:
            self.bo_click_checkbox_single('Exchange')
        if exchange is False:
            self.bo_click_uncheckbox_single('Exchange')
        # assert value
        self.wait_loading()
        # click 'Save'
        self.click_button('Save')
        if list_error_message:
        # verify error
            self.assert_error_message()
            self.assert_list_error_message(list_error_message)
            print('Action add failed!')
        else:
        # verify success
            self.assert_button_disable('Save')
            self.check_notification('Saved successfully!')
            transaction_code_out=self.bo_get_value_group_single('Transaction code')
            print(f'Transaction code: {transaction_code_out}')
            ifc_code_out=self.bo_get_text_group_single('IFC code')
            print(f'IFC code: {ifc_code_out}')
            return transaction_code_out, ifc_code_out

    def deposit_ifc_auto_fee_view(self, transaction_code=None, ifc_code=None, condition=None, active=None, exchange=None):
        # search
        self.deposit_ifc_auto_fee_advanced_search(transaction_code=transaction_code, ifc_code=ifc_code)
        if transaction_code:
            self.assert_table_data('Transaction code', 1, transaction_code)
        if ifc_code:
            self.assert_table_data('IFC code', 1, ifc_code)
        # view
        self.click_table_menu('View', 1)
        self.wait_for_button_available('Modify')
        self.assert_form_title('DPT-IFC Auto Fee-View')
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

    def deposit_ifc_auto_fee_update(self, transaction_code=None, ifc_code=None, condition=None, active=None, exchange=None, list_error_message=None):
        # view
        self.deposit_ifc_auto_fee_view(transaction_code=transaction_code, ifc_code=ifc_code)
        self.click_button('Modify')
        self.wait_loading()
        # update value
        self.bo_click_tab('General information')
        if condition:
            self.bo_write_text('Condition', condition)
        if active is True:
            self.bo_click_checkbox('Active')
        if active is False:
            self.bo_click_uncheckbox('Active')
        if exchange is True:
            self.bo_click_checkbox('Exchange')
        if exchange is False:
            self.bo_click_uncheckbox('Exchange')
        # assert value
        self.bo_click_tab('General information')
        if transaction_code:
            self.bo_assert_value_group('Transaction code', transaction_code)
        if ifc_code:
            self.bo_assert_text_group('IFC code', ifc_code)
        self.wait_loading()
        # click 'Save'
        self.click_button('Save')
        if list_error_message:
        # verify error
            self.assert_error_message()
            self.assert_list_error_message(list_error_message)
            print('Action update failed!')
        else:
        # verify success
            self.assert_button_disable('Save')
            self.check_notification('Saved successfully!')
            self.bo_click_tab('General information')
            transaction_code_out=self.bo_get_value_group('Transaction code')
            print(f'Transaction code: {transaction_code_out}')
            ifc_code_out=self.bo_get_text_group('IFC code')
            print(f'IFC code: {ifc_code_out}')
            return transaction_code_out, ifc_code_out

    def deposit_ifc_auto_fee_delete(self, transaction_code, ifc_code, list_error_message=None, expected_message=None):
        # search
        self.deposit_ifc_auto_fee_advanced_search(transaction_code=transaction_code, ifc_code=ifc_code)
        if transaction_code:
            self.assert_table_data('Transaction code', 1, transaction_code)
        if ifc_code:
            self.assert_table_data('IFC code', 1, ifc_code)
        # delete
        self.click_table_menu('Delete', 1)
        self.wait_loading()
        self.click_button_in_popup('Yes')
        if list_error_message:
        # verify error
            self.assert_error_message()
            self.assert_list_error_message(list_error_message)
            print(f"Action delete '{transaction_code}' and '{ifc_code}' failed!")
        else:
        # verify success
            if expected_message:
                self.assert_notification(expected_message)
            print(f"Deleted: '{transaction_code}' and '{ifc_code}'")
            return transaction_code, ifc_code

    # DPT-Catalogue Definition
    def deposit_catalogue_definition_simple_search(self, text):
        self.close_all_form()
        self.click_menu('Deposit', 'Catalogue Definition')
        self.wait_for_button_available('Search')
        self.assert_form_title('DPT-Catalogue Definition-Search')
        self.simple_search(text=text, placeholder='Search text')
        self.wait_loading()

    def deposit_catalogue_definition_advanced_search(self, catalogue_code=None, catalogue_name=None, currency_code=None, deposit_type=None, passbook_or_statement=None, tenor_from=None, tenor_to=None, tenor_unit=None, status=None):
        self.close_all_form()
        self.click_menu('Deposit', 'Catalogue Definition')
        self.wait_for_button_available('Search')
        self.assert_form_title('DPT-Catalogue Definition-Search')
        if catalogue_code:
            self.adv_search_text('Catalogue code', catalogue_code)
        if catalogue_name:
            self.adv_search_text('Catalogue name', catalogue_name)
        if currency_code:
            self.adv_search_text('Currency code', currency_code)
        self.key_escape()
        if deposit_type:
            self.adv_search_select('Deposit type', deposit_type)
        self.key_escape()
        if passbook_or_statement:
            self.adv_search_select('Passbook or statement', passbook_or_statement)
        if tenor_from:
            self.adv_search('Tenor from', tenor_from)
        if tenor_to:
            self.adv_search('Tenor to', tenor_to)
        self.key_escape()
        if tenor_unit:
            self.adv_search_select('Tenor unit', tenor_unit)
        self.key_escape()
        if status:
            self.adv_search_select('Status', status)
        self.click_button_search_advanced()
        self.wait_loading()

    def deposit_catalogue_definition_add(self, catalogue_code=None, catalogue_name=None, currency_code=None, deposit_type=None, deposit_sub_type=None, deposit_purpose=None, deposit_classification=None, passbook_or_statement_or_receipt=None, minimum_deposit_amount=None, catalogue_status=None, interest_payment_restrictions=None, debit_accounting=None, debit_cash=None, debit_deposit=None, credit_accounting=None, credit_cash=None, credit_deposit=None, tenor_1=None, tenor_unit_1=None, tenor_2=None, tenor_unit_2=None, deposit_tenor=None, deposit_tenor_unit=None, interest_tenor=None, interest_tenor_unit=None, minimum_tenor=None, minimum_tenor_unit=None, multiple_deposit_allow=None, multiple_withdrawal_allow=None, early_withdrawal=None, minimum_tenor_allow_early_withdrawal=None, minimum_tenor_allow_early_withdrawal_unit=None, credit_interest_y_n=None, credit_interest_tenor=None, credit_interest_tenor_unit=None, the_day_of_tenor_for_crediting_interest=None, minimum_dormant_amount=None, dormant_period=None, type_of_dormant_period=None, rollover_option=None, rollover_to_catalogue=None, initial_deposit_amount=None, ifc_codes=None, sys_account_names=None, coa_accounts=None, account_aliass=None, replace_code=None, replace_bys=None, system_account_names=None, customer_sectors=None, customer_resident_statuss=None, business_lines=None, sub_products=None, bank_identifications=None, list_error_message=None):
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
        if catalogue_name:
            self.bo_write_text('Name', catalogue_name)
        self.key_escape()
        if currency_code:
            self.bo_select('Currency code', currency_code)
        self.key_escape()
        if deposit_type:
            self.bo_select('Deposit type', deposit_type)
        self.key_escape()
        if deposit_sub_type:
            self.bo_select('Deposit sub type', deposit_sub_type)
        self.key_escape()
        if deposit_purpose:
            self.bo_select('Deposit purpose', deposit_purpose)
        self.key_escape()
        if deposit_classification:
            self.bo_select('Deposit classification', deposit_classification)
        self.key_escape()
        if passbook_or_statement_or_receipt:
            self.bo_select('Passbook or statement or receipt', passbook_or_statement_or_receipt)
        if minimum_deposit_amount:
            self.bo_write_number('Minimum deposit amount', minimum_deposit_amount)
        self.key_escape()
        if catalogue_status:
            self.bo_select('Catalogue status', catalogue_status)
        self.key_escape()
        if interest_payment_restrictions:
            self.bo_select_multi('Interest payment restriction', interest_payment_restrictions)
        self.bo_click_collap('Debit With')
        if debit_accounting is True:
            self.bo_click_checkbox_multi('Debit With', 'Accounting')
        if debit_accounting is False:
            self.bo_click_uncheckbox_multi('Debit With', 'Accounting')
        if debit_cash is True:
            self.bo_click_checkbox_multi('Debit With', 'Cash')
        if debit_cash is False:
            self.bo_click_uncheckbox_multi('Debit With', 'Cash')
        if debit_deposit is True:
            self.bo_click_checkbox_multi('Debit With', 'Deposit')
        if debit_deposit is False:
            self.bo_click_uncheckbox_multi('Debit With', 'Deposit')
        self.bo_click_collap('Credit With')
        if credit_accounting is True:
            self.bo_click_checkbox_multi('Credit With', 'Accounting')
        if credit_accounting is False:
            self.bo_click_uncheckbox_multi('Credit With', 'Accounting')
        if credit_cash is True:
            self.bo_click_checkbox_multi('Credit With', 'Cash')
        if credit_cash is False:
            self.bo_click_uncheckbox_multi('Credit With', 'Cash')
        if credit_deposit is True:
            self.bo_click_checkbox_multi('Credit With', 'Deposit')
        if credit_deposit is False:
            self.bo_click_uncheckbox_multi('Credit With', 'Deposit')
        self.bo_click_tab('Tenor and relative information')
        if tenor_1:
            self.bo_write_group('Tenor 1', tenor_1)
        self.key_escape()
        if tenor_unit_1:
            self.bo_select_group('Tenor unit 1', tenor_unit_1)
        if tenor_2:
            self.bo_write_group('Tenor 2', tenor_2)
        self.key_escape()
        if tenor_unit_2:
            self.bo_select_group('Tenor unit 2', tenor_unit_2)
        if deposit_tenor:
            self.bo_write_group('Deposit tenor', deposit_tenor)
        self.key_escape()
        if deposit_tenor_unit:
            self.bo_select_group('Deposit tenor unit', deposit_tenor_unit)
        if interest_tenor:
            self.bo_write('Interest tenor', interest_tenor)
        self.key_escape()
        if interest_tenor_unit:
            self.bo_select('Interest tenor unit', interest_tenor_unit)
        if minimum_tenor:
            self.bo_write_group('Minimum tenor', minimum_tenor)
        self.key_escape()
        if minimum_tenor_unit:
            self.bo_select_group('Minimum tenor unit', minimum_tenor_unit)
        self.key_escape()
        if multiple_deposit_allow:
            self.bo_select('Multiple deposit allow', multiple_deposit_allow)
        self.key_escape()
        if multiple_withdrawal_allow:
            self.bo_select('Multiple withdrawal allow', multiple_withdrawal_allow)
        self.key_escape()
        if early_withdrawal:
            self.bo_select('Early withdrawal', early_withdrawal)
        if minimum_tenor_allow_early_withdrawal:
            self.bo_write_group('Minimum tenor allow early withdrawal', minimum_tenor_allow_early_withdrawal)
        self.key_escape()
        if minimum_tenor_allow_early_withdrawal_unit:
            self.bo_select_group('Minimum tenor allow early withdrawal unit', minimum_tenor_allow_early_withdrawal_unit)
        self.key_escape()
        if credit_interest_y_n:
            self.bo_select('Credit interest (Y/N)', credit_interest_y_n)
        if credit_interest_tenor:
            self.bo_write_group('Credit interest tenor', credit_interest_tenor)
        self.key_escape()
        if credit_interest_tenor_unit:
            self.bo_select_group('Credit interest tenor unit', credit_interest_tenor_unit)
        if the_day_of_tenor_for_crediting_interest:
            self.bo_write('The day of tenor for crediting interest', the_day_of_tenor_for_crediting_interest)
        if minimum_dormant_amount:
            self.bo_write_number('Minimum Dormant amount', minimum_dormant_amount)
        if dormant_period:
            self.bo_write_group('Dormant period', dormant_period)
        self.key_escape()
        if type_of_dormant_period:
            self.bo_select_group('Type of dormant period', type_of_dormant_period)
        self.key_escape()
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
                self.wait_loading()
                self.select('IFC Code', ifc_code)
                self.click_button_in_tab('Apply')
                self.wait_loading()
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
        self.wait_loading()
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
            self.check_notification('Saved successfully!')
            self.bo_click_tab('General information')
            catalogue_code = self.bo_get_value('Catalogue code')
            print('Catalogue code: ' + catalogue_code)
            return catalogue_code

    def deposit_catalogue_definition_view(self, catalogue_code, catalogue_name=None, currency_code=None, deposit_type=None, deposit_sub_type=None, deposit_purpose=None, deposit_classification=None, passbook_or_statement_or_receipt=None, minimum_deposit_amount=None, catalogue_status=None, interest_payment_restrictions=None, created_by=None, approved_by=None, debit_accounting=None, debit_cash=None, debit_deposit=None, credit_accounting=None, credit_cash=None, credit_deposit=None, tenor_1=None, tenor_unit_1=None, tenor_2=None, tenor_unit_2=None, deposit_tenor=None, deposit_tenor_unit=None, interest_tenor_unit=None, interest_tenor=None, minimum_tenor=None, minimum_tenor_unit=None, multiple_deposit_allow=None, multiple_withdrawal_allow=None, early_withdrawal=None, minimum_tenor_allow_early_withdrawal=None, minimum_tenor_allow_early_withdrawal_unit=None, credit_interest_y_n=None, credit_interest_tenor=None, credit_interest_tenor_unit=None, the_day_of_tenor_for_crediting_interest=None, minimum_dormant_amount=None, dormant_period=None, type_of_dormant_period=None, rollover_option=None, rollover_to_catalogue=None, initial_deposit_amount=None, expected_ifc_list_codes=None, expected_ifc_names=None, expected_ifc_values=None, expected_ifc_types=None, expected_ifc_tenors=None, expected_ifc_tenor_units=None, expected_ifc_statuss=None, expected_gls_sys_account_names=None, expected_gls_account_aliass=None, expected_extension_sys_account_names=None, expected_extension_conditions=None, expected_extension_replace_bys=None):
        # search
        self.deposit_catalogue_definition_simple_search(catalogue_code)
        self.assert_table_data('Catalogue code', 1, catalogue_code)
        # view
        self.click_table_menu('View', 1)
        self.wait_for_button_available('Modify')
        self.assert_form_title('DPT-Catalogue Definition-View')
        # verify value
        self.bo_click_tab('General information')
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
        if rollover_to_catalogue or rollover_to_catalogue == '':
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
        print('View catalogue code: ' + catalogue_code)
        return catalogue_code

    def deposit_catalogue_definition_update(self, catalogue_code, catalogue_name=None, currency_code=None, deposit_type=None, deposit_sub_type=None, deposit_purpose=None, deposit_classification=None, passbook_or_statement_or_receipt=None, minimum_deposit_amount=None, catalogue_status=None, interest_payment_restrictions=None, debit_accounting=None, debit_cash=None, debit_deposit=None, credit_accounting=None, credit_cash=None, credit_deposit=None, minimum_tenor_unit=None, multiple_deposit_allow=None, multiple_withdrawal_allow=None, credit_interest_y_n=None, credit_interest_tenor=None, credit_interest_tenor_unit=None, the_day_of_tenor_for_crediting_interest=None, minimum_dormant_amount=None, dormant_period=None, type_of_dormant_period=None, initial_deposit_amount=None, list_error_message=None):
        self.deposit_catalogue_definition_view(catalogue_code)
        self.wait_loading()
        self.click_button('Modify')
        # update value
        self.bo_click_tab('General information')
        if catalogue_name or catalogue_name == '':
            self.bo_write_text('Name', catalogue_name)
        self.key_escape()
        if currency_code:
            self.bo_select('Currency code', currency_code)
        self.key_escape()
        if deposit_type:
            self.bo_select('Deposit type', deposit_type)
        self.key_escape()
        if deposit_sub_type:
            self.bo_select('Deposit sub type', deposit_sub_type)
        self.key_escape()
        if deposit_purpose:
            self.bo_select('Deposit purpose', deposit_purpose)
        self.key_escape()
        if deposit_classification:
            self.bo_select('Deposit classification', deposit_classification)
        self.key_escape()
        if passbook_or_statement_or_receipt:
            self.bo_select('Passbook or statement or receipt', passbook_or_statement_or_receipt)
        if minimum_deposit_amount:
            self.bo_write_number('Minimum deposit amount', minimum_deposit_amount)
        self.key_escape()
        if catalogue_status:
            self.bo_select('Catalogue status', catalogue_status)
        self.key_escape()
        if interest_payment_restrictions:
            self.bo_select_multi('Interest payment restriction', interest_payment_restrictions)
        self.bo_click_collap('Debit with ')
        if debit_accounting is True:
            self.bo_click_checkbox_multi('Debit with ', 'Accounting')
        if debit_accounting is False:
            self.bo_click_uncheckbox_multi('Debit with ', 'Accounting')
        if debit_cash is True:
            self.bo_click_checkbox_multi('Debit with ', 'Cash')
        if debit_cash is False:
            self.bo_click_uncheckbox_multi('Debit with ', 'Cash')
        if debit_deposit is True:
            self.bo_click_checkbox_multi('Debit with ', 'Deposit')
        if debit_deposit is False:
            self.bo_click_uncheckbox_multi('Debit with ', 'Deposit')
        self.bo_click_collap('Credit with')
        if credit_accounting is True:
            self.bo_click_checkbox_multi('Credit with', 'Accounting')
        if credit_accounting is False:
            self.bo_click_uncheckbox_multi('Credit with', 'Accounting')
        if credit_cash is True:
            self.bo_click_checkbox_multi('Credit with', 'Cash')
        if credit_cash is False:
            self.bo_click_uncheckbox_multi('Credit with', 'Cash')
        if credit_deposit is True:
            self.bo_click_checkbox_multi('Credit with', 'Deposit')
        if credit_deposit is False:
            self.bo_click_uncheckbox_multi('Credit with', 'Deposit')
        self.bo_click_tab('Tenor and relative information')
        self.key_escape()
        if minimum_tenor_unit:
            self.bo_select_group('Minimum tenor unit', minimum_tenor_unit)
        self.key_escape()
        if multiple_deposit_allow:
            self.bo_select('Multiple deposit allow', multiple_deposit_allow)
        self.key_escape()
        if multiple_withdrawal_allow:
            self.bo_select('Multiple withdrawal allow', multiple_withdrawal_allow)
        self.key_escape()
        if credit_interest_y_n:
            self.bo_select('Credit interest (Y/N)', credit_interest_y_n)
        if credit_interest_tenor:
            self.bo_write_number_group('Credit interest tenor', credit_interest_tenor)
        self.key_escape()
        if credit_interest_tenor_unit:
            self.bo_select_group('Credit interest tenor unit', credit_interest_tenor_unit)
        if the_day_of_tenor_for_crediting_interest:
            self.bo_write_number('The day of tenor for crediting interest', the_day_of_tenor_for_crediting_interest)
        if minimum_dormant_amount:
            self.bo_write_number('Minimum Dormant amount', minimum_dormant_amount)
        if dormant_period:
            self.bo_write_number_group('Dormant period', dormant_period)
        self.key_escape()
        if type_of_dormant_period:
            self.bo_select_group('Type of dormant period', type_of_dormant_period)
        if initial_deposit_amount:
            self.bo_write_number('Initial deposit amount', initial_deposit_amount)
        # click 'Save'
        self.click_button('Save')
        if list_error_message:
        # verify error
            self.assert_error_message()
            self.assert_list_error_message(list_error_message)
            print(f"Update: '{catalogue_code}' failed!")
        else:
        # verify success
            self.assert_button_disable('Save')
            self.check_notification('Saved successfully!')
            self.bo_click_tab('General information')
            catalogue_code = self.bo_get_value('Catalogue code')
            print(f"Updated: '{catalogue_code}'")
            return catalogue_code

    def deposit_catalogue_definition_delete(self, catalogue_code, list_error_message=None, expected_message=None):
        # search
        self.deposit_catalogue_definition_simple_search(catalogue_code)
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
            print(f"Action delete '{catalogue_code}' failed!")
        else:
        # verify success
            if expected_message:
                self.assert_notification(expected_message)
            print(f"Deleted: '{catalogue_code}'")
            return catalogue_code

    # DPT-Account Information
    def deposit_account_simple_search(self, text):
        self.close_all_form()
        self.click_menu('Deposit', 'Account Information')
        self.wait_for_button_available('Add')
        self.assert_form_title('DPT-Account Information-Search')
        self.simple_search(text)

    def deposit_account_advanced_search(self, account_number=None, account_name=None, currency_code=None, customer_code=None, customer_type=None, catalogue_code=None, status=None, deposit_sub_type=None, deposit_type=None, old_a_c_no=None, open_date_from=None, open_date_to=None, overdraft_contract=None, surplus_account=None, deficit_account=None, sweeping_status=None):
        self.close_all_form()
        self.click_menu('Deposit', 'Account Information')
        self.wait_for_button_available('Add')
        self.assert_form_title('DPT-Account Information-Search')
        if account_number:
            self.adv_search_text('Account number', str(account_number).replace('-', ''))
        if account_name:
            self.adv_search_text('Account name', account_name)
        if currency_code:
            self.adv_search_text('Currency code', currency_code)
        if customer_code:
            self.adv_search('Customer code', str(customer_code).replace('-', ''))
        self.key_escape()
        if customer_type:
            self.adv_search_select('Customer type', customer_type)
        if catalogue_code:
            self.adv_search_text('Catalogue code', catalogue_code)
        self.key_escape()
        if status:
            self.adv_search_select('Status', status)
        self.key_escape()
        if deposit_sub_type:
            self.adv_search_select('Deposit sub type ', deposit_sub_type)
        self.key_escape()
        if deposit_type:
            self.adv_search_select('Deposit type', deposit_type)
        if old_a_c_no:
            self.adv_search_text('Old a/c no', old_a_c_no)
        if open_date_from:
            self.adv_search_group('Open date from', open_date_from)
        if open_date_to:
            self.adv_search_group('Open date to ', open_date_to)
        if overdraft_contract:
            self.adv_search_text('Overdraft contract', str(overdraft_contract).replace('-', ''))
        if surplus_account:
            self.adv_search('Surplus account', str(surplus_account).replace('-', ''))
        if deficit_account:
            self.adv_search('Deficit account', str(deficit_account).replace('-', ''))
        self.key_escape()
        if sweeping_status:
            self.adv_search_select('Sweeping status', sweeping_status)
        self.click_button_search_advanced()
        self.wait_loading()

    def deposit_account_view(self, account_number, passbook_or_receipt_number=None, linkage_account_number=None, account_name=None, currency_code=None, account_holder_type=None, account_holder=None, branch_id=None, account_status=None, catalogue_code=None, deposit_type=None, deposit_sub_type=None, begin_of_tenor=None, end_of_tenor=None, open_date=None, close_date=None, last_transaction_date=None, last_date_system_transfer_interest_to_due=None, dormant_date=None, last_change_dormant_to_normal_date=None, created_by=None, approved_by=None, account_manager_staff_code=None, agent_hub_referral=None, relation_customers=None, business_purpose_code=None, is_restricted=None, current_balance=None, available_balance=None, minimum_deposit_amount=None, minimum_amount_to_dormant=None, earmark_block_amount=None, initial_deposit_amount=None, interest_accrual=None, interest_receivable=None, interest_prepaid=None, interest_due=None, interest_not_paid=None, interest_paid=None, deposit_amount=None, withdraw_amount=None, deposit_tenor=None, interest_tenor=None, minimum_tenor=None, multiple_deposit_allow=None, multiple_withdrawal_allow=None, early_withdrawal=None, minimum_tenor_allow_early_withdrawal=None, credit_interest=None, credit_interest_tenor=None, the_day_of_tenor_for_crediting_interest=None, dormant_period=None, rollover_option=None, rollover_to_catalogue=None, employer_organization_name=None, reference_id=None, reason_of_account_opening=None, safe_deposit_locker_number=None, relationship_manager=None, expected_account_gl_names=None, expected_account_gl_numbers=None, expected_account_gl_name=None, expected_account_gl_number=None, expected_ifc_codes=None, expected_ifc_gl_names=None, expected_ifc_gl_numbers=None, expected_ifc_list_codes=None, expected_ifc_code=None, expected_ifc_names=None, expected_ifc_base_values=None, expected_ifc_is_linkeds=None, expected_ifc_values=None, expected_ifc_margin_values=None, expected_ifc_statuses=None, expected_ifc_outstandings=None, expected_ifc_paids=None, expected_ifc_basic_balances=None, expected_ifc_name=None, expected_ifc_base_value=None, expected_ifc_is_linked=None, expected_ifc_value=None, expected_ifc_margin_value=None, expected_ifc_status=None, expected_ifc_outstanding=None, expected_ifc_paid=None, expected_ifc_basic_balance=None):
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
        if linkage_account_number is not None:
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
            self.bo_assert_value_group('Business Purpose Code', business_purpose_code)
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
        if safe_deposit_locker_number:
            self.bo_assert_text('Safe Deposit Locker Number', safe_deposit_locker_number)
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

    def deposit_account_update(self, account_number, agent_hub_referral=None, is_restricted=None, rollover_option=None, rollover_to_catalogue=None, reason_of_account_opening=None, safe_deposit_locker_number=None, list_error_message=None):
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
        if safe_deposit_locker_number:
            self.bo_write_text('Safe Deposit Locker Number', safe_deposit_locker_number)
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
            self.check_notification('Saved successfully!')
            self.bo_click_tab('General information')
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
            self.check_notification('Deleted successfully')
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
    def deposit_account_modify_simple_search(self, text):
        self.close_all_form()
        self.click_menu('Deposit', 'Approve Account Modification')
        self.wait_for_button_available('Search')
        self.assert_form_title('DPT-Approve Account Modification-Search')
        self.simple_search(text=text, placeholder='Search text')
        self.wait_loading()

    def deposit_account_modify_advanced_search(self, account_number=None, account_name=None, currency_code=None, customer_code=None, customer_type=None, catalogue_code=None, status=None, deposit_type=None, old_a_c_no=None):
        self.close_all_form()
        self.click_menu('Deposit', 'Approve Account Modification')
        self.wait_for_button_available('Search')
        self.assert_form_title('DPT-Approve Account Modification-Search')
        if account_number:
            self.adv_search_text('Account number', str(account_number).replace('-', ''))
        if account_name:
            self.adv_search_text('Account name', account_name)
        if currency_code:
            self.adv_search_text('Currency code', currency_code)
        if customer_code:
            self.adv_search_text('Customer code', str(customer_code).replace('-', ''))
        self.key_escape()
        if customer_type:
            self.adv_search_select('Customer type', customer_type)
        if catalogue_code:
            self.adv_search_text('Catalogue code', catalogue_code)
        self.key_escape()
        if status:
            self.adv_search_select('Status', status)
        self.key_escape()
        if deposit_type:
            self.adv_search_select('Deposit type', deposit_type)
        if old_a_c_no:
            self.adv_search_text('Old a/c no', old_a_c_no)
        self.click_button_search_advanced()
        self.wait_loading()

    def deposit_account_modify_view(self, account_number):
        # search deposit account modify
        self.deposit_account_modify_simple_search(str(account_number).replace('-', ''))
        self.assert_table_data('Account number', 1, self.deposit_account_number_mask(account_number))
        # view deposit account modify
        self.click_table_menu(row=1)
        self.wait_for_button_available('View Modification')
        self.assert_form_title('DPT-Approve Account Modification-View')
        # verify value tab 'General information'
        self.bo_assert_value('Account number', self.deposit_account_number_mask(account_number))

    def deposit_account_modify_approve(self, account_number):
        self.deposit_account_modify_view(account_number)
        self.click_button('View Modification')
        self.wait_loading()
        self.click_button('Approve')
        self.wait_loading()
        self.check_notification('Action successful')
        # back to tab 'General information'
        self.bo_click_tab('General information')
        self.bo_assert_value('Account number', account_number)
        account_number_actual = self.bo_get_value('Account number')
        print('Account number: ' + account_number_actual)
        self.deposit_account_modify_simple_search(str(account_number_actual).replace('-', ''))
        self.assert_search_not_found()
        return account_number_actual

    def deposit_account_modify_reject(self, account_number):
        self.deposit_account_modify_view(account_number)
        self.click_button('View Modification')
        self.wait_loading()
        self.click_button('Reject')
        self.wait_loading()
        self.check_notification('Action successful')
        # back to tab 'General information'
        self.bo_click_tab('General information')
        self.bo_assert_value('Account number', account_number)
        account_number_actual = self.bo_get_value('Account number')
        print('Account number: ' + account_number_actual)
        self.deposit_account_modify_simple_search(str(account_number_actual).replace('-', ''))
        self.assert_search_not_found()
        return account_number_actual

    # DPT-Stock Inventory
    def stock_inventory_simple_search(self, text):
        self.close_all_form()
        self.click_menu('Deposit', 'Stock Inventory')
        self.wait_for_button_available('Add')
        self.assert_form_title('DPT-Stock Inventory-Search')
        self.simple_search(text)

    def stock_inventory_advanced_search(self, stock_prefix=None, from_serial=None, to_serial=None, stock_type=None, from_serial_to=None, to_serial_from=None, stock_no=None, book_status=None, confirm_status=None, branch=None, user_create=None, status_of_stock_leaves=None, account_number=None, amount=None, stock_balance=None, currency=None, user_approved=None, stock_holding_user=None):
        self.close_all_form()
        self.click_menu('Deposit', 'Stock Inventory')
        self.wait_for_button_available('Add')
        self.assert_form_title('DPT-Stock Inventory-Search')
        if stock_no:
            self.adv_search_text('Stock no', stock_no)
        if stock_prefix:
            self.adv_search_text('Stock prefix', stock_prefix)
        if from_serial:
            if len(from_serial) != 6:
                from_serial = self.get_serial_number_no_refix(from_serial)
            self.adv_search_group('From serial from', from_serial)
        if from_serial_to:
            if len(from_serial_to) != 6:
                from_serial_to = self.get_serial_number_no_refix(from_serial_to)
            self.adv_search_group('From serial to', from_serial_to)
        if to_serial_from:
            if len(to_serial_from) != 6:
                to_serial_from = self.get_serial_number_no_refix(to_serial_from)
            self.adv_search_group('To serial from', to_serial_from)
        if to_serial:
            if len(to_serial) != 6:
                to_serial = self.get_serial_number_no_refix(to_serial)
            self.adv_search_group('To serial to', to_serial)
        self.key_escape()
        if book_status:
            self.adv_search_select('Book status', book_status)
        self.key_escape()
        if confirm_status:
            self.adv_search_select('Confirm status', confirm_status)
        if branch:
            self.adv_search_text('Branch', branch)
        if user_create:
            self.adv_search_text('User create', user_create)
        self.key_escape()
        if status_of_stock_leaves:
            self.adv_search_select('Status of stock leaves', status_of_stock_leaves)
        self.key_escape()
        if stock_type:
            self.adv_search_select('Stock type', stock_type)
        if account_number:
            self.adv_search_text('Account number', account_number)
        if amount:
            self.adv_search('Amount', amount)
        if stock_balance:
            self.adv_search('Stock balance', stock_balance)
        if currency:
            self.adv_search_text('Currency', currency)
        if user_approved:
            self.adv_search_text('User approved', user_approved)
        if stock_holding_user:
            self.adv_search_text('Stock holding user', stock_holding_user)
        self.click_button_search_advanced()
        self.wait_loading()

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
            self.check_notification('Deleted successfully')
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
        self.simple_search(text=text, placeholder='Search text')
        self.wait_loading()

    def dpt_account_linkage_advanced_search(self, master_module_name=None, master_account_number=None, master_account_name=None):
        self.close_all_form()
        self.click_menu('Payment', 'Account Linkage')
        self.wait_for_button_available('Search')
        self.assert_form_title('DPT-Account Linkage-Search')
        self.key_escape()
        if master_module_name:
            self.adv_search_select('Master module name', master_module_name)
        if master_account_number:
            self.adv_search_text('Master account number', str(master_account_number).replace('-', ''))
        if master_account_name:
            self.adv_search_text('Master account name', master_account_name)
        self.click_button_search_advanced()
        self.wait_loading()

    def dpt_opal(self, master_module_name=None, master_account_code=None, linkage_module_name=None, linkage_account_code=None, linkage_type=None, linkage_classification=None, linkage_description=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None, currency_for_fee=None, description=None, fee_collect_method=None, account_number_for_fee=None, amount_for_fee_calculation=None):
        # open form
        self.close_all_form()
        self.open_fo('DPT_OPAL', 'DPT-Account Linkage-Add')
        self.wait_for_button_available('Accept')
        self.assert_form_title('DPT-Account Linkage-Add')
        # enter value
        self.key_escape()
        if master_module_name:
            self.select('Master module name', master_module_name)
        if master_account_code:
            master_account_code_value = self.no_mask(master_account_code)
            self.fo_write_data('Master account code', master_account_code_value, need_tab='Y')
            self.wait_loading()
        if currency_for_fee:
            self.fo_assert_select('Currency (for fee)', currency_for_fee)
        # add list linkage
        self.click_button('Add', 1)
        self.wait_loading()
        self.key_escape()
        if linkage_module_name:
            self.select('Linkage module name', linkage_module_name)
        if linkage_account_code:
            linkage_account_code_value = self.no_mask(linkage_account_code)
            self.fo_write_data('Linkage account  code', linkage_account_code_value, need_tab='Y')
            self.wait_loading()
        self.key_escape()
        if linkage_type:
            self.select('Linkage type', linkage_type)
        self.key_escape()
        if linkage_classification:
            self.select('Linkage classification', linkage_classification)
        if linkage_description:
            self.fo_write_text('Linkage description', linkage_description)
        self.click_button('Apply', 1)
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_write_text('Description', description)
        self.key_escape()
        if fee_collect_method:
            self.fo_select('Fee collect method', fee_collect_method)
        if account_number_for_fee:
            account_number_for_fee_value = self.no_mask(account_number_for_fee)
            self.fo_write_text_data('Account number for fee', account_number_for_fee_value, need_tab='Y')
        if amount_for_fee_calculation:
            self.fo_write_number('Amount for fee calculation', amount_for_fee_calculation)
        if ifc_codes:
            self.add_fees(ifc_codes, values, total_fee, 2)
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
            self.check_notification('Saved successfully!')
            self.close_voucher()
            if expected_posting:
                self.assert_posting_data(**expected_posting)
            transaction_references=self.assert_transaction_number_not_null()
            print(f'Transaction references DPT_OPAL: {transaction_references}')
            master_account_code=self.fo_get_value_group('Master account code')
            print(f'Master account number: {master_account_code}')
            linkage_account_code=self.get_text_table_data('Linkage account code', 1)
            print(f'Linkage account code: {linkage_account_code}')
            return transaction_references

    def dpt_opal_lookup(self, master_module_name=None, master_account_code=None, linkage_module_name=None, linkage_account_code=None, linkage_type=None, linkage_classification=None, linkage_description=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None, currency_for_fee=None, description=None, fee_collect_method=None, account_number_for_fee=None, amount_for_fee_calculation=None):
        # open form
        self.close_all_form()
        self.click_menu('Payment', 'Account Linkage')
        self.wait_for_button_available('Add')
        self.assert_form_title('DPT-Account Linkage-Search')
        self.click_button('Add')
        self.wait_for_button_available('Accept')
        self.assert_form_title('DPT-Account Linkage-Add')
        # enter value
        self.key_escape()
        if master_module_name:
            self.select('Master module name', master_module_name)
        if master_account_code:
            master_account_code_value = self.no_mask(master_account_code)
            self.lookup_data_text(
                title='Master account code',
                value_search_code=master_account_code_value,
                value_code=master_account_code_value
            )
            self.wait_loading()
        if currency_for_fee:
            self.fo_assert_select('Currency (for fee)', currency_for_fee)
        # add list linkage
        self.click_button('Add', 1)
        self.wait_loading()
        self.key_escape()
        if linkage_module_name:
            self.select('Linkage module name', linkage_module_name)
        if linkage_account_code:
            linkage_account_code_value = self.no_mask(linkage_account_code)
            self.lookup_data_text(
                title='Linkage account  code',
                value_search_code=linkage_account_code_value,
                value_code=linkage_account_code_value
            )
            self.wait_loading()
        self.key_escape()
        if linkage_type:
            self.select('Linkage type', linkage_type)
        self.key_escape()
        if linkage_classification:
            self.select('Linkage classification', linkage_classification)
        if linkage_description:
            self.fo_write_text('Linkage description', linkage_description)
        self.click_button('Apply', 1)
        self.wait_loading()
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_write_text('Description', description)
        self.key_escape()
        if fee_collect_method:
            self.fo_select('Fee collect method', fee_collect_method)
        if account_number_for_fee:
            account_number_for_fee_value = self.no_mask(account_number_for_fee)
            self.lookup_data_text(
                title='Account number for fee',
                value_search_code=account_number_for_fee_value,
                value_code=account_number_for_fee_value,
            )
        if amount_for_fee_calculation:
            self.fo_write_number('Amount for fee calculation', amount_for_fee_calculation)
        if ifc_codes:
            self.add_fees_lookup(ifc_codes, values, total_fee, index=2)
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
            self.check_notification('Saved successfully!')
            self.close_voucher()
            if expected_posting:
                self.assert_posting_data(**expected_posting)
            transaction_references=self.assert_transaction_number_not_null()
            print(f'Transaction references DPT_OPAL: {transaction_references}')
            master_account_code=self.fo_get_value_group('Master account code')
            print(f'Master account number: {master_account_code}')
            linkage_account_code=self.get_text_table_data('Linkage account code', 1)
            print(f'Linkage account code: {linkage_account_code}')
            return transaction_references

    def dpt_opal_view(self, transaction_references, master_module_name=None, master_account_code=None, linkage_module_name=None, linkage_account_code=None, linkage_type=None, linkage_classification=None, linkage_description=None, ifc_codes=None, values=None, total_fee=None, currency_for_fee=None, description=None, fee_collect_method=None, account_number_for_fee=None, amount_for_fee_calculation=None, expected_posting=None, linkage_account_name=None):
        self.transaction_view(transaction_references, 'DPT-Account Linkage-Add')
        # compare value
        if master_module_name:
            self.fo_assert_value_data('Master module name', master_module_name)
        if master_account_code:
            self.fo_assert_value_data('Master account code', self.no_mask(master_account_code))
        # compare list linkage
        if linkage_module_name:
            if linkage_account_code:
                self.fo_assert_text_table('Linkage module name', linkage_module_name, 'Linkage account code', self.no_mask(linkage_account_code))
            if linkage_account_name:
                self.fo_assert_text_table('Linkage module name', linkage_module_name, 'Linkage account name', linkage_account_name)
            if linkage_description:
                self.fo_assert_text_table('Linkage module name', linkage_module_name, 'Linkage description', linkage_description)
            if linkage_type:
                self.fo_assert_text_table('Linkage module name', linkage_module_name, 'Linkage type', linkage_type)
            if linkage_classification:
                self.fo_assert_text_table('Linkage module name', linkage_module_name, 'Linkage class', linkage_classification)
        # compare value
        if fee_collect_method:
            self.fo_assert_value_data('Fee collect method', fee_collect_method)
        if account_number_for_fee:
            self.fo_assert_text_data('Account number for fee', self.no_mask(account_number_for_fee))
        if amount_for_fee_calculation:
            self.fo_assert_value_data('Amount for fee calculation', amount_for_fee_calculation)
        if ifc_codes:
            self.assert_fees(ifc_codes, values, total_fee)
        if expected_posting:
            self.assert_posting_data(**expected_posting)
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_assert_text_data('Description', description)

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
                self.check_notification('Saved successfully!')
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
                self.check_notification('Saved successfully!')
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
                self.check_notification('Saved successfully!')
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
        self.check_notification('Deleted successfully')
        # search and verify
        self.wait_loading()
        self.dpt_account_linkage_simple_search(master_account_number)
        self.assert_search_not_found()
        print('Delete master account number: ' + master_account_number)
        return master_account_number

# -------------------------- handle BO approval - DEPOSIT --------------------------
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

