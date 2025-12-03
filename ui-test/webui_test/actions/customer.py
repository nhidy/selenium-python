from webui_test.case import *

class CustomerActions(TestCase):

# -------------------------- handle FO - CUSTOMER --------------------------
    # CTM_APR: Approve customer
    def ctm_apr(self, customer_code=None, description=None, customer_name=None, created_by=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.open_fo('CTM_APR', 'Approve customer')
        self.wait_for_button_available('Accept')
        self.assert_form_title('Approve customer')
        # enter value
        if customer_code:
            self.fo_write('Customer code', str(customer_code).replace('-', ''))
            self.wait_loading()
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_write_text('Description', description)
        if ifc_codes:
            self.add_fees(ifc_codes, values, total_fee)
        if customer_name:
            self.fo_assert_text('Customer name', customer_name)
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
            print(f'Transaction references CTM_APR: {transaction_references}')
            customer_code_out=self.fo_get_value('Customer code')
            print(f'Customer code: {customer_code_out}')
            return transaction_references, customer_code_out

    def ctm_apr_view(self, transaction_references, customer_code=None, description=None, customer_name=None, created_by=None, expected_posting=None):
        self.transaction_view(transaction_references, 'Approve customer')
        # compare value
        if customer_code:
            self.fo_assert_value('Customer code', self.customer_code_mask(customer_code))
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_assert_text('Description', description)
        if customer_name:
            self.fo_assert_text('Customer name', customer_name)
        if created_by:
            self.fo_assert_select('Created by', created_by)
        if expected_posting:
            self.assert_posting_data(**expected_posting)
        transaction_references=self.assert_transaction_number_not_null()
        print(f'F8: Transaction references CTM_APR: {transaction_references}')
        customer_code_out=self.fo_get_value('Customer code')
        print(f'F8: Customer code: {customer_code_out}')
        return transaction_references, customer_code_out

    # CTM_CCN: Change Customer Name
    def ctm_ccn(self, customer_code=None, new_first_name_en=None, new_last_name_en=None, new_father_name=None, new_full_name=None, description=None, old_first_name_en=None, old_last_name_en=None, old_father_name=None, old_full_name=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.open_fo('CTM_CCN', 'Change customer name')
        self.wait_for_button_available('Accept')
        self.assert_form_title('Change Customer Name')
        # enter value
        if customer_code:
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
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_write_text('Description', description)
        if ifc_codes:
            self.add_fees(ifc_codes, values, total_fee)
        if old_first_name_en:
            self.fo_assert_text('Old First Name (en)', old_first_name_en)
        if old_last_name_en:
            self.fo_assert_text('Old Last Name (en)', old_last_name_en)
        if old_father_name:
            self.fo_assert_text('Old Father Name', old_father_name)
        if old_full_name:
            self.fo_assert_text('Old Full Name', old_full_name)
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
            print(f'Transaction references CTM_CCN: {transaction_references}')
            customer_code_out=self.fo_get_value('Customer code')
            print(f'Customer code: {customer_code_out}')
            return transaction_references, customer_code_out

    def ctm_ccn_view(self, transaction_references, customer_code=None, new_first_name_en=None, new_last_name_en=None, new_father_name=None, new_full_name=None, description=None, old_first_name_en=None, old_last_name_en=None, old_father_name=None, old_full_name=None, expected_posting=None):
        self.transaction_view(transaction_references, 'Change Customer Name')
        # compare value
        if customer_code:
            self.fo_assert_value('Customer code', self.customer_code_mask(customer_code))
        if new_first_name_en:
            self.fo_assert_text('New First Name (en)', new_first_name_en)
        if new_last_name_en:
            self.fo_assert_text('New Last Name (en)', new_last_name_en)
        if new_father_name:
            self.fo_assert_text('New Father Name', new_father_name)
        if new_full_name:
            self.fo_assert_text('New Full Name', new_full_name)
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_assert_text('Description', description)
        if old_first_name_en:
            self.fo_assert_text('Old First Name (en)', old_first_name_en)
        if old_last_name_en:
            self.fo_assert_text('Old Last Name (en)', old_last_name_en)
        if old_father_name:
            self.fo_assert_text('Old Father Name', old_father_name)
        if old_full_name:
            self.fo_assert_text('Old Full Name', old_full_name)
        if expected_posting:
            self.assert_posting_data(**expected_posting)
        transaction_references=self.assert_transaction_number_not_null()
        print(f'F8: Transaction references CTM_CCN: {transaction_references}')
        customer_code_out=self.fo_get_value('Customer code')
        print(f'F8: Customer code: {customer_code_out}')
        return transaction_references, customer_code_out

    # CTM_CPN: Change Customer Paper Number
    def ctm_cpn(self, customer_code=None, paper_type=None, state=None, district=None, type=None, registration_no=None, paper_number=None, description=None, old_paper_type=None, old_paper_number=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.open_fo('CTM_CPN', 'Change customer paper number')
        self.wait_for_button_available('Accept')
        self.assert_form_title('Change Customer Paper Number')
        # enter value
        if customer_code:
            self.fo_write('Customer code', str(customer_code).replace('-', ''))
            self.wait_loading()
        self.key_escape()
        if paper_type:
            self.fo_select('Paper type', paper_type)
        self.key_escape()
        if state:
            self.fo_select('State', state)
        self.key_escape()
        if district:
            self.fo_select('District', district)
        self.key_escape()
        if type:
            self.fo_select('Type', type)
        if registration_no:
            self.fo_write('Registration No', registration_no)
        if paper_number:
            if paper_type=='NRC':
                self.fo_assert_text('Paper number', paper_number)
            else:
                self.fo_write_text('Paper number', paper_number)
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_write_text('Description', description)
        if ifc_codes:
            self.add_fees(ifc_codes, values, total_fee)
        if old_paper_type:
            self.fo_assert_select('Old paper type', old_paper_type)
        if old_paper_number:
            self.fo_assert_text('Old paper number ', old_paper_number)
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
            print(f'Transaction references CTM_CPN: {transaction_references}')
            customer_code_out=self.fo_get_value('Customer code')
            print(f'Customer code: {customer_code_out}')
            return transaction_references, customer_code_out

    def ctm_cpn_view(self, transaction_references, customer_code=None, paper_type=None, state=None, district=None, type=None, registration_no=None, paper_number=None, description=None, old_paper_type=None, old_paper_number=None, expected_posting=None):
        self.transaction_view(transaction_references, 'Change Customer Paper Number')
        # compare value
        if customer_code:
            self.fo_assert_value('Customer code', self.customer_code_mask(customer_code))
        if paper_type:
            self.fo_assert_select('Paper type', paper_type)
        if state:
            self.fo_assert_select('State', state)
        if district:
            self.fo_assert_select('District', district)
        if type:
            self.fo_assert_select('Type', type)
        if registration_no:
            self.fo_assert_value('Registration No', registration_no)
        if paper_number:
            self.fo_assert_text('Paper number', paper_number)
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_assert_text('Description', description)
        if old_paper_type:
            self.fo_assert_select('Old paper type', old_paper_type)
        if old_paper_number:
            self.fo_assert_text('Old paper number ', old_paper_number)
        if expected_posting:
            self.assert_posting_data(**expected_posting)
        transaction_references=self.assert_transaction_number_not_null()
        print(f'F8: Transaction references CTM_CPN: {transaction_references}')
        customer_code_out=self.fo_get_value('Customer code')
        print(f'F8: Customer code: {customer_code_out}')
        return transaction_references, customer_code_out

    # CTM_CAS: Change customer status
    def ctm_cas(self, customer_code=None, new_status=None, description=None, current_status=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.open_fo('CTM_CAS', 'Change customer status')
        self.wait_for_button_available('Accept')
        self.assert_form_title('Change customer status')
        # enter value
        if customer_code:
            self.fo_write_group('Customer code', str(customer_code).replace('-', ''))
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
        if current_status:
            self.fo_assert_select('Current status', current_status)
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
            print(f'Transaction references CTM_CAS: {transaction_references}')
            customer_code_out=self.fo_get_value_group('Customer code')
            print(f'Customer code: {customer_code_out}')
            return transaction_references, customer_code_out

    def ctm_cas_view(self, transaction_references, customer_code=None, new_status=None, description=None, current_status=None, expected_posting=None):
        self.transaction_view(transaction_references, 'Change customer status')
        # compare value
        if customer_code:
            self.fo_assert_value_group('Customer code', self.customer_code_mask(customer_code))
        if new_status:
            self.fo_assert_select('New status', new_status)
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_assert_text('Description', description)
        if current_status:
            self.fo_assert_select('Current status', current_status)
        if expected_posting:
            self.assert_posting_data(**expected_posting)
        transaction_references=self.assert_transaction_number_not_null()
        print(f'F8: Transaction references CTM_CAS: {transaction_references}')
        customer_code_out=self.fo_get_value_group('Customer code')
        print(f'F8: Customer code: {customer_code_out}')
        return transaction_references, customer_code_out

    # CTM_CPA: Change Customer Phone, Email And Address
    def ctm_cpa(self, customer_code=None, home_01=None, street_01=None, ward_01=None, township_01=None, province_01=None, home_02=None, street_02=None, ward_02=None, township_02=None, province_02=None, home_phone=None, mobile_phone=None, email_address=None, description=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.open_fo('CTM_CPA', 'Change customer phone, email and address')
        self.wait_for_button_available('Accept')
        self.assert_form_title('Change Customer Phone, Email And Address')
        # enter value
        if customer_code:
            self.fo_write_group('Customer code', str(customer_code).replace('-', ''))
            self.wait_loading()
        self.key_escape()
        if home_01:
            self.fo_click_collap('Legal address')
            self.fo_write_text_multi('Legal address', 'Home', home_01)
            self.wait_loading()
        if street_01:
            self.fo_click_collap('Legal address')
            self.fo_write_text_multi('Legal address', 'Street', street_01)
            self.wait_loading()
        if ward_01:
            self.fo_click_collap('Legal address')
            self.fo_write_text_multi('Legal address', 'Ward', ward_01)
            self.wait_loading()
        if township_01:
            self.fo_click_collap('Legal address')
            self.fo_write_text_multi('Legal address', 'Township', township_01)
            self.wait_loading()
        if province_01:
            self.fo_click_collap('Legal address')
            self.fo_write_text_multi('Legal address', 'Province', province_01)
            self.wait_loading()
        if home_02:
            self.fo_click_collap('Contact local address')
            self.fo_write_text_multi('Contact local address', 'Home', home_02)
            self.wait_loading()
        if street_02:
            self.fo_click_collap('Contact local address')
            self.fo_write_text_multi('Contact local address', 'Street', street_02)
            self.wait_loading()
        if ward_02:
            self.fo_click_collap('Contact local address')
            self.fo_write_text_multi('Contact local address', 'Ward', ward_02)
            self.wait_loading()
        if township_02:
            self.fo_click_collap('Contact local address')
            self.fo_write_text_multi('Contact local address', 'Township', township_02)
            self.wait_loading()
        if province_02:
            self.fo_click_collap('Contact local address')
            self.fo_write_text_multi('Contact local address', 'Province', province_02)
            self.wait_loading()
        if home_phone:
            self.fo_write_text('Home phone', home_phone)
        if mobile_phone:
            self.fo_write_text('Mobile phone', mobile_phone)
        if email_address:
            self.fo_write('Email address', email_address)
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_write_text('Description', description)
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
            self.check_notification('Saved successfully!')
            self.close_voucher()
            if expected_posting:
                self.assert_posting_data(**expected_posting)
            transaction_references=self.assert_transaction_number_not_null()
            print(f'Transaction references CTM_CPA: {transaction_references}')
            customer_code_out=self.fo_get_value_group('Customer code')
            print(f'Customer code: {customer_code_out}')
            return transaction_references, customer_code_out

    def ctm_cpa_view(self, transaction_references, customer_code=None, home_01=None, street_01=None, ward_01=None, township_01=None, province_01=None, home_02=None, street_02=None, ward_02=None, township_02=None, province_02=None, home_phone=None, mobile_phone=None, email_address=None, description=None, expected_posting=None):
        self.transaction_view(transaction_references, 'Change Customer Phone, Email And Address')
        # compare value
        if customer_code:
            self.fo_assert_value_group('Customer code', self.customer_code_mask(customer_code))
        if home_01:
            self.fo_assert_text_multi('Legal address', 'Home', home_01)
        if street_01:
            self.fo_assert_text_multi('Legal address', 'Street', street_01)
        if ward_01:
            self.fo_assert_text_multi('Legal address', 'Ward', ward_01)
        if township_01:
            self.fo_assert_text_multi('Legal address', 'Township', township_01)
        if province_01:
            self.fo_assert_text_multi('Legal address', 'Province', province_01)
        if home_02:
            self.fo_assert_text_multi('Contact local address', 'Home', home_02)
        if street_02:
            self.fo_assert_text_multi('Contact local address', 'Street', street_02)
        if ward_02:
            self.fo_assert_text_multi('Contact local address', 'Ward', ward_02)
        if township_02:
            self.fo_assert_text_multi('Contact local address', 'Township', township_02)
        if province_02:
            self.fo_assert_text_multi('Contact local address', 'Province', province_02)
        if home_phone:
            self.fo_assert_text('Home phone', home_phone)
        if mobile_phone:
            self.fo_assert_text('Mobile phone', mobile_phone)
        if email_address:
            self.fo_assert_value('Email address', email_address)
        if description:
            self.fo_assert_text('Description', description)
        if expected_posting:
            self.assert_posting_data(**expected_posting)
        transaction_references=self.assert_transaction_number_not_null()
        print(f'F8: Transaction references CTM_CPA: {transaction_references}')
        customer_code_out=self.fo_get_value_group('Customer code')
        print(f'F8: Customer code: {customer_code_out}')
        return transaction_references, customer_code_out

# -------------------------- handle BO - CUSTOMER --------------------------
    # CTM-Customer Profile
    def customer_profile_simple_search(self, text):
        self.close_all_form()
        self.click_menu('Customer', 'Customer Profile')
        self.wait_for_button_available('Search')
        self.assert_form_title('CTM-Customer Profile-Search')
        self.simple_search(text=text, placeholder='Search text')
        self.wait_loading()

    def customer_profile_advanced_search(self, customer_code=None, full_name=None, paper_number=None, date_of_birth_from=None, date_of_birth_to=None, gender=None, customer_status=None, nationality=None, resident_status=None, address=None, approver=None, old_id_of_customer=None, open_date_from=None, open_date_to=None, branch_code=None):
        self.close_all_form()
        self.click_menu('Customer', 'Customer Profile')
        self.wait_for_button_available('Search')
        self.assert_form_title('CTM-Customer Profile-Search')
        if customer_code:
            self.adv_search('Customer code', str(customer_code).replace('-', ''))
        if full_name:
            self.adv_search_text('Full name', full_name)
        if paper_number:
            self.adv_search_text('Paper number', paper_number)
        if date_of_birth_from:
            self.adv_search_group('Date of birth from', date_of_birth_from)
        if date_of_birth_to:
            self.adv_search_group('Date of birth to', date_of_birth_to)
        self.key_escape()
        if gender:
            self.adv_search_select('Gender', gender)
        self.key_escape()
        if customer_status:
            self.adv_search_select('Customer status', customer_status)
        self.key_escape()
        if nationality:
            self.adv_search_select('Nationality', nationality)
        self.key_escape()
        if resident_status:
            self.adv_search_select('Resident status', resident_status)
        if address:
            self.adv_search_text('Address', address)
        if approver:
            self.adv_search_text('Approver', approver)
        if old_id_of_customer:
            self.adv_search_text('Old id of customer', old_id_of_customer)
        if open_date_from:
            self.adv_search_group('Open date from', open_date_from)
        if open_date_to:
            self.adv_search_group('Open date to', open_date_to)
        self.key_escape()
        if branch_code:
            self.adv_search_select('Branch code', branch_code)
        self.click_button_search_advanced()
        self.wait_loading()

    def customer_profile_add(self, customer_code=None, business_line=None, title=None, title_of_organization=None, customer_type=None, customer_sub_type=None, first_name_en=None, last_name_en=None, full_name=None, suffix=None, father_name=None, gender=None, starting_date_of_company=None, date_of_birth=None, place_of_birth=None, country_of_company=None, nationality=None, paper_type=None, reason_for_other_paper_type=None, state_nrc=None, district_nrc=None, type_nrc=None, registration_no_nrc=None, paper_number=None, tin_number=None, issue_date_of_paper=None, issue_place_of_paper=None, expire_date_of_paper=None, group_type=None, group_sub_type=None, economic_sector=None, reason_for_other_economic_sector=None, sub_economic_sector=None, reason_for_other_sub_economic_sector=None, customer_segment=None, resident_status=None, bank_identification=None, fdi_info=None, home_01=None, street_01=None, ward_01=None, township_01=None, province_01=None, home_02=None, street_02=None, ward_02=None, township_02=None, province_02=None, name_01=None, account_no_01=None, name_02=None, account_no_02=None, home_phone=None, mobile_phone=None, email_address=None, education=None, marital_status=None, employer_name=None, occupation=None, reason_for_other_occupation=None, financial_institute=None, business_type=None, reason_for_other_business_type=None, isic_code=None, managing_branch_code=None, status=None, classification=None, country_of_income=None, government_organization_id=None, international_organization_and_oversea_government_id=None, oversea_juristic_id=None, gfmis_code=None, staff_care=None, account_owner_referral_rm=None, account_operations=None, remark_field_to_add=None, position=None, income=None, credit_line=None, currency=None, mm_limit=None, currency_mm=None, fx_limit=None, currency_fx=None, list_error_message=None):
        # open form
        self.close_all_form()
        self.click_menu('Customer', 'Customer Profile')
        self.wait_for_button_available('Add')
        self.assert_form_title('CTM-Customer Profile-Search')
        self.click_button('Add')
        self.wait_for_button_available('Save')
        self.assert_form_title('CTM-Customer Profile-Add')
        # enter value
        self.bo_click_tab('General information')
        self.key_escape()
        if business_line:
            self.bo_select('Business line', business_line)
        self.key_escape()
        if title:
            self.bo_select('Title', title)
        self.key_escape()
        if title_of_organization:
            self.bo_select('Title of organization', title_of_organization)
        self.key_escape()
        if customer_type:
            self.bo_select('Customer type', customer_type)
        self.key_escape()
        if customer_sub_type:
            self.bo_select('Customer sub type', customer_sub_type)
        if first_name_en:
            self.bo_write_text('First name (en)', first_name_en)
        if last_name_en:
            self.bo_write_text('Last name (en)', last_name_en)
        if full_name:
            if self.bo_get_select('Business line') == 'Personal':
                self.key_tab()
                self.bo_assert_text('Full name', full_name)
            else:
                self.bo_write_text('Full name', full_name)
        self.key_escape()
        if suffix:
            self.bo_select('Suffix', suffix)
        if father_name:
            self.bo_write_text('Father name', father_name)
        self.key_escape()
        if gender:
            self.bo_select('Gender', gender)
        if starting_date_of_company:
            self.bo_write_date('Starting date of company', starting_date_of_company)
        if date_of_birth:
            self.bo_write_date('Date of birth', date_of_birth)
        if place_of_birth:
            self.bo_write_text('Place of birth', place_of_birth)
        self.key_escape()
        if country_of_company:
            self.bo_select('Country of company', country_of_company)
        self.key_escape()
        if nationality:
            self.bo_select('Nationality', nationality)
        self.key_escape()
        if paper_type:
            self.bo_select('Paper type', paper_type)
        if reason_for_other_paper_type:
            self.bo_write_text('Reason for Other (Paper type)', reason_for_other_paper_type)
        self.key_escape()
        if state_nrc:
            self.bo_select('State', state_nrc)
        self.key_escape()
        if district_nrc:
            self.bo_select('District', district_nrc)
        self.key_escape()
        if type_nrc:
            self.bo_select('Type', type_nrc)
        if registration_no_nrc:
            self.bo_write('Registration No', registration_no_nrc)
        if paper_number:
            if self.bo_get_select('Paper type') == 'NRC':
                self.bo_assert_text('Paper number', paper_number)
            else:
                self.bo_write_text('Paper number', paper_number)
        if tin_number:
            self.bo_write('TIN number', tin_number)
        if issue_date_of_paper:
            self.bo_write_date('Issue date of paper', issue_date_of_paper)
        if issue_place_of_paper:
            self.bo_write_text('Issue place of paper', issue_place_of_paper)
        if expire_date_of_paper:
            self.bo_write_date('Expire date of paper', expire_date_of_paper)
        self.key_escape()
        if group_type:
            self.bo_select('Group type', group_type)
        self.key_escape()
        if group_sub_type:
            self.bo_select('Group sub type', group_sub_type)
        self.key_escape()
        if economic_sector:
            self.bo_select('Economic sector', economic_sector)
        if reason_for_other_economic_sector:
            self.bo_write_text('Reason for Other (Economic sector)', reason_for_other_economic_sector)
        self.key_escape()
        if sub_economic_sector:
            self.bo_select('Sub economic sector', sub_economic_sector)
        if reason_for_other_sub_economic_sector:
            self.bo_write_text('Reason for Other (Sub economic sector)', reason_for_other_sub_economic_sector)
        self.key_escape()
        if customer_segment:
            self.bo_select('Customer segment', customer_segment)
        self.key_escape()
        if resident_status:
            self.bo_select('Resident status', resident_status)
        self.key_escape()
        if bank_identification:
            self.bo_select('Bank Identification', bank_identification)
        if fdi_info:
            self.bo_write_text('FDI info', fdi_info)
        if home_01:
            self.bo_click_collap('Legal address')
            self.bo_write_text_multi('Legal address', 'Home', home_01)
        if street_01:
            self.bo_click_collap('Legal address')
            self.bo_write_text_multi('Legal address', 'Street', street_01)
        if ward_01:
            self.bo_click_collap('Legal address')
            self.bo_write_text_multi('Legal address', 'Ward', ward_01)
        if township_01:
            self.bo_click_collap('Legal address')
            self.bo_write_text_multi('Legal address', 'Township', township_01)
        if province_01:
            self.bo_click_collap('Legal address')
            self.bo_write_text_multi('Legal address', 'Province', province_01)
        if home_02:
            self.bo_click_collap('Contact local address')
            self.bo_write_text_multi('Contact local address', 'Home', home_02)
        if street_02:
            self.bo_click_collap('Contact local address')
            self.bo_write_text_multi('Contact local address', 'Street', street_02)
        if ward_02:
            self.bo_click_collap('Contact local address')
            self.bo_write_text_multi('Contact local address', 'Ward', ward_02)
        if township_02:
            self.bo_click_collap('Contact local address')
            self.bo_write_text_multi('Contact local address', 'Township', township_02)
        if province_02:
            self.bo_click_collap('Contact local address')
            self.bo_write_text_multi('Contact local address', 'Province', province_02)
        if name_01:
            self.bo_click_collap('Introducer 1')
            self.bo_write_text_multi('Introducer 1', 'Name', name_01)
        if account_no_01:
            self.bo_click_collap('Introducer 1')
            self.bo_write_multi('Introducer 1', 'Account No', account_no_01)
        if name_02:
            self.bo_click_collap('Introducer 2')
            self.bo_write_text_multi('Introducer 2', 'Name', name_02)
        if account_no_02:
            self.bo_click_collap('Introducer 2')
            self.bo_write_multi('Introducer 2', 'Account No', account_no_02)
        if home_phone:
            self.bo_write_text('Home phone', home_phone)
        if mobile_phone:
            self.bo_write_text('Mobile phone', mobile_phone)
        if email_address:
            self.bo_write('Email address', email_address)
        self.key_escape()
        if education:
            self.bo_select('Education', education)
        self.key_escape()
        if marital_status:
            self.bo_select('Marital status', marital_status)
        if employer_name:
            self.bo_write_text('Employer Name', employer_name)
        self.key_escape()
        if occupation:
            self.bo_select('Occupation', occupation)
        if reason_for_other_occupation:
            self.bo_write_text('Reason for Other (Occupation)', reason_for_other_occupation)
        self.key_escape()
        if financial_institute:
            self.bo_select('Financial Institute', financial_institute)
        self.key_escape()
        if business_type:
            self.bo_select('Business Type', business_type)
        if reason_for_other_business_type:
            self.bo_write_text('Reason for Other (Business Type)', reason_for_other_business_type)
        if isic_code:
            self.bo_write_group('ISIC Code', isic_code)
        self.bo_click_tab('Other information')
        self.key_escape()
        if classification:
            self.bo_select('Classification', classification)
        self.key_escape()
        if country_of_income:
            self.bo_select('Country of Income', country_of_income)
        if government_organization_id:
            self.bo_write_text('Government Organization ID', government_organization_id)
        if international_organization_and_oversea_government_id:
            self.bo_write_text('International Organization and Oversea Government ID', international_organization_and_oversea_government_id)
        if oversea_juristic_id:
            self.bo_write_text('Oversea Juristic ID', oversea_juristic_id)
        if gfmis_code:
            self.bo_write_text('GFMIS Code', gfmis_code)
        self.key_escape()
        if staff_care:
            self.bo_select('Staff care', staff_care)
        self.key_escape()
        if account_owner_referral_rm:
            self.bo_select('Account Owner/Referral/RM', account_owner_referral_rm)
        self.key_escape()
        if account_operations:
            self.bo_select('Account Operations', account_operations)
        if remark_field_to_add:
            self.bo_write_text('Remark field to add', remark_field_to_add)
        if position:
            self.bo_write_text('Position ', position)
        self.key_escape()
        if income:
            self.bo_select('Income', income)
        self.bo_click_tab('Credit line information')
        if credit_line:
            self.bo_write_number_group('Credit line', credit_line)
        self.key_escape()
        if currency:
            self.bo_select_group('Currency', currency)
        if mm_limit:
            self.bo_write_number_group('MM limit', mm_limit)
        self.key_escape()
        if currency_mm:
            self.bo_select_group('Currency MM', currency_mm)
        if fx_limit:
            self.bo_write_number_group('FX limit', fx_limit)
        self.key_escape()
        if currency_fx:
            self.bo_select_group('Currency FX', currency_fx)
        # assert value
        self.bo_click_tab('General information')
        if customer_code:
            self.bo_assert_value('Customer code', self.customer_code_mask(customer_code))
        if managing_branch_code:
            self.bo_assert_value_group('Managing branch code', managing_branch_code)
        if status:
            self.bo_assert_select('Status', status)
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
            self.check_notification('Save successfully')
            self.bo_click_tab('General information')
            customer_code_out=self.bo_get_value('Customer code')
            print(f'Customer code: {customer_code_out}')
            return customer_code_out

    def customer_profile_view(self, customer_code=None, business_line=None, title=None, title_of_organization=None, customer_type=None, customer_sub_type=None, suffix=None, first_name_en=None, last_name_en=None, full_name=None, father_name=None, gender=None, date_of_birth_starting_date_of_company=None, place_of_birth=None, nationality=None, country_of_company=None, paper_type=None, reason_for_other_paper_type=None, paper_number=None, tin_number=None, issue_date_of_paper=None, issue_place_of_paper=None, expire_date_of_paper=None, group_type=None, group_sub_type=None, economic_sector=None, reason_for_other_economic_sector=None, sub_economic_sector=None, reason_for_other_sub_economic_sector=None, customer_segment=None, resident_status=None, bank_identification=None, fdi_info=None, home_01=None, street_01=None, ward_01=None, township_01=None, province_01=None, home_02=None, street_02=None, ward_02=None, township_02=None, province_02=None, name_01=None, account_no_01=None, name_02=None, account_no_02=None, home_phone=None, mobile_phone=None, email_address=None, education=None, marital_status=None, employer_name=None, occupation=None, reason_for_other_occupation=None, financial_institute=None, business_type=None, reason_for_other_business_type=None, isic_code=None, managing_branch_code=None, status=None, classification=None, country_of_income=None, government_organization_id=None, international_organization_and_oversea_government_id=None, oversea_juristic_id=None, gfmis_code=None, open_date=None, approve_date=None, last_date=None, branch_code=None, created_by=None, approved_by=None, account_owner_referral_rm=None, account_operations=None, remark_field_to_add=None, position=None, income=None, last_modify_user=None, last_approve_modify_user=None, credit_line=None, currency=None, mm_limit=None, currency_mm=None, fx_limit=None, currency_fx=None):
        # search
        self.customer_profile_simple_search(str(customer_code).replace('-', ''))
        self.assert_table_data('Customer code', 1, self.customer_code_mask(customer_code))
        # view
        self.click_table_menu('View', 1)
        self.wait_for_button_available('Modify')
        self.assert_form_title('CTM-Customer Profile-View')
        # verify value
        self.bo_click_tab('General information')
        if customer_code:
            self.bo_assert_value('Customer code', self.customer_code_mask(customer_code))
        if business_line:
            self.bo_assert_select('Business line', business_line)
        if title:
            self.bo_assert_select('Title', title)
        if title_of_organization:
            self.bo_assert_select('Title of organization', title_of_organization)
        if customer_type:
            self.bo_assert_select('Customer type', customer_type)
        if customer_sub_type:
            self.bo_assert_select('Customer sub type', customer_sub_type)
        if suffix:
            self.bo_assert_select('Suffix', suffix)
        if first_name_en:
            self.bo_assert_text('First name (en)', first_name_en)
        if last_name_en:
            self.bo_assert_text('Last name (en)', last_name_en)
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
        if country_of_company:
            self.bo_assert_select('Country of company', country_of_company)
        if paper_type:
            self.bo_assert_select('Paper type', paper_type)
        if reason_for_other_paper_type:
            self.bo_assert_text('Reason for Other (Paper type)', reason_for_other_paper_type)
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
        if group_type:
            self.bo_assert_select('Group type', group_type)
        if group_sub_type:
            self.bo_assert_select('Group sub type', group_sub_type)
        if economic_sector:
            self.bo_assert_select('Economic sector', economic_sector)
        if reason_for_other_economic_sector:
            self.bo_assert_text('Reason for Other (Economic sector)', reason_for_other_economic_sector)
        if sub_economic_sector:
            self.bo_assert_select('Sub economic sector', sub_economic_sector)
        if reason_for_other_sub_economic_sector:
            self.bo_assert_text('Reason for Other (Sub economic sector)', reason_for_other_sub_economic_sector)
        if customer_segment:
            self.bo_assert_select('Customer segment', customer_segment)
        if resident_status:
            self.bo_assert_select('Resident status', resident_status)
        if bank_identification:
            self.bo_assert_select('Bank Identification', bank_identification)
        if fdi_info:
            self.bo_assert_text('FDI info', fdi_info)
        if home_01:
            self.bo_click_collap('Legal address')
            self.bo_assert_text_multi('Legal address', 'Home', home_01)
        if street_01:
            self.bo_click_collap('Legal address')
            self.bo_assert_text_multi('Legal address', 'Street', street_01)
        if ward_01:
            self.bo_click_collap('Legal address')
            self.bo_assert_text_multi('Legal address', 'Ward', ward_01)
        if township_01:
            self.bo_click_collap('Legal address')
            self.bo_assert_text_multi('Legal address', 'Township', township_01)
        if province_01:
            self.bo_click_collap('Legal address')
            self.bo_assert_text_multi('Legal address', 'Province', province_01)
        if home_02:
            self.bo_click_collap('Contact local address')
            self.bo_assert_text_multi('Contact local address', 'Home', home_02)
        if street_02:
            self.bo_click_collap('Contact local address')
            self.bo_assert_text_multi('Contact local address', 'Street', street_02)
        if ward_02:
            self.bo_click_collap('Contact local address')
            self.bo_assert_text_multi('Contact local address', 'Ward', ward_02)
        if township_02:
            self.bo_click_collap('Contact local address')
            self.bo_assert_text_multi('Contact local address', 'Township', township_02)
        if province_02:
            self.bo_click_collap('Contact local address')
            self.bo_assert_text_multi('Contact local address', 'Province', province_02)
        if name_01:
            self.bo_click_collap('Introducer 1')
            self.bo_assert_text_multi('Introducer 1', 'Name', name_01)
        if account_no_01:
            self.bo_click_collap('Introducer 1')
            self.bo_assert_value_multi('Introducer 1', 'Account No', account_no_01)
        if name_02:
            self.bo_click_collap('Introducer 2')
            self.bo_assert_text_multi('Introducer 2', 'Name', name_02)
        if account_no_02:
            self.bo_click_collap('Introducer 2')
            self.bo_assert_value_multi('Introducer 2', 'Account No', account_no_02)
        if home_phone:
            self.bo_assert_text('Home phone', home_phone)
        if mobile_phone:
            self.bo_assert_text('Mobile phone', mobile_phone)
        if email_address:
            self.bo_assert_value('Email address', email_address)
        if education:
            self.bo_assert_select('Education', education)
        if marital_status:
            self.bo_assert_select('Marital status', marital_status)
        if employer_name:
            self.bo_assert_text('Employer Name', employer_name)
        if occupation:
            self.bo_assert_select('Occupation', occupation)
        if reason_for_other_occupation:
            self.bo_assert_text('Reason for Other (Occupation)', reason_for_other_occupation)
        if financial_institute:
            self.bo_assert_select('Financial Institute', financial_institute)
        if business_type:
            self.bo_assert_select('Business Type', business_type)
        if reason_for_other_business_type:
            self.bo_assert_text('Reason for Other (Business Type)', reason_for_other_business_type)
        if isic_code:
            self.bo_assert_value_group('ISIC Code', isic_code)
        if managing_branch_code:
            self.bo_assert_value_group('Managing branch code', managing_branch_code)
        if status:
            self.bo_assert_select('Status', status)
        self.bo_click_tab('Other information')
        if classification:
            self.bo_assert_select('Classification', classification)
        if country_of_income:
            self.bo_assert_select('Country of Income', country_of_income)
        if government_organization_id:
            self.bo_assert_text('Government Organization ID', government_organization_id)
        if international_organization_and_oversea_government_id:
            self.bo_assert_text('International Organization and Oversea Government ID', international_organization_and_oversea_government_id)
        if oversea_juristic_id:
            self.bo_assert_text('Oversea Juristic ID', oversea_juristic_id)
        if gfmis_code:
            self.bo_assert_text('GFMIS Code', gfmis_code)
        if open_date:
            self.bo_assert_date('Open date', open_date)
        if approve_date:
            self.bo_assert_date('Approve date', approve_date)
        if last_date:
            self.bo_assert_date('Last date', last_date)
        if branch_code:
            self.bo_assert_value_group('Branch code', branch_code)
        if created_by:
            self.bo_assert_value_group('Created by', created_by)
        if approved_by:
            self.bo_assert_value_group('Approved by', approved_by)
        if account_owner_referral_rm:
            self.bo_assert_select('Account Owner/Referral/RM', account_owner_referral_rm)
        if account_operations:
            self.bo_assert_select('Account Operations', account_operations)
        if remark_field_to_add:
            self.bo_assert_text('Remark field to add', remark_field_to_add)
        if position:
            self.bo_assert_text('Position', position)
        if income:
            self.bo_assert_select('Income', income)
        if last_modify_user:
            self.bo_assert_text('Last modify user', last_modify_user)
        if last_approve_modify_user:
            self.bo_assert_text('Last approve modify user', last_approve_modify_user)
        self.bo_click_tab('Credit line information')
        if credit_line:
            self.bo_assert_value_group('Credit line', credit_line)
        if currency:
            self.bo_assert_select_group('Currency', currency)
        if mm_limit:
            self.bo_assert_value_group('MM limit ', mm_limit)
        if currency_mm:
            self.bo_assert_select_group('Currency MM', currency_mm)
        if fx_limit:
            self.bo_assert_value_group('FX limit', fx_limit)
        if currency_fx:
            self.bo_assert_select_group('Currency FX ', currency_fx)

    def customer_profile_update(self, customer_code=None, business_line=None, title=None, title_of_organization=None, customer_type=None, customer_sub_type=None, suffix=None, first_name_en=None, last_name_en=None, full_name=None, father_name=None, gender=None, date_of_birth_starting_date_of_company=None, place_of_birth=None, nationality=None, country_of_company=None, paper_type=None, reason_for_other_paper_type=None, paper_number=None, tin_number=None, issue_date_of_paper=None, issue_place_of_paper=None, expire_date_of_paper=None, group_type=None, group_sub_type=None, economic_sector=None, reason_for_other_economic_sector=None, sub_economic_sector=None, reason_for_other_sub_economic_sector=None, customer_segment=None, resident_status=None, bank_identification=None, fdi_info=None, home_01=None, street_01=None, ward_01=None, township_01=None, province_01=None, home_02=None, street_02=None, ward_02=None, township_02=None, province_02=None, name_01=None, account_no_01=None, name_02=None, account_no_02=None, home_phone=None, mobile_phone=None, email_address=None, education=None, marital_status=None, employer_name=None, occupation=None, reason_for_other_occupation=None, financial_institute=None, business_type=None, reason_for_other_business_type=None, isic_code=None, managing_branch_code=None, status=None, classification=None, country_of_income=None, government_organization_id=None, international_organization_and_oversea_government_id=None, oversea_juristic_id=None, gfmis_code=None, open_date=None, approve_date=None, last_date=None, branch_code=None, created_by=None, approved_by=None, account_owner_referral_rm=None, account_operations=None, remark_field_to_add=None, position=None, income=None, last_modify_user=None, last_approve_modify_user=None, credit_line=None, currency=None, mm_limit=None, currency_mm=None, fx_limit=None, currency_fx=None, list_error_message=None):
        # view
        self.customer_profile_view(customer_code=customer_code)
        self.bo_click_tab('General information')
        self.click_button('Modify')
        self.wait_loading()
        if self.bo_get_select('Status') == 'Pending Approval':
            # update value
            self.bo_click_tab('General information')
            self.key_escape()
            if title:
                self.bo_select('Title', title)
            self.key_escape()
            if title_of_organization:
                self.bo_select('Title of organization', title_of_organization)
            self.key_escape()
            if customer_sub_type:
                self.bo_select('Customer sub type', customer_sub_type)
            self.key_escape()
            if suffix:
                self.bo_select('Suffix', suffix)
            if first_name_en:
                self.bo_write_text('First name (en)', first_name_en)
            if last_name_en:
                self.bo_write_text('Last name (en)', last_name_en)
            if full_name:
                self.bo_write_text('Full name', full_name)
            if father_name:
                self.bo_write_text('Father name', father_name)
            self.key_escape()
            if gender:
                self.bo_select('Gender', gender)
            if date_of_birth_starting_date_of_company:
                self.bo_write_date('Date of birth/Starting date of company', date_of_birth_starting_date_of_company)
            if place_of_birth:
                self.bo_write_text('Place of birth', place_of_birth)
            self.key_escape()
            if nationality:
                self.bo_select('Nationality', nationality)
            self.key_escape()
            if country_of_company:
                self.bo_select('Country of company', country_of_company)
            self.key_escape()
            if paper_type:
                self.bo_select('Paper type', paper_type)
            if reason_for_other_paper_type:
                self.bo_write_text('Reason for Other (Paper type)', reason_for_other_paper_type)
            if paper_number:
                self.bo_write_text('Paper number', paper_number)
            if tin_number:
                self.bo_write('TIN number', tin_number)
            if issue_date_of_paper:
                self.bo_write_date('Issue date of paper', issue_date_of_paper)
            if issue_place_of_paper:
                self.bo_write_text('Issue place of paper', issue_place_of_paper)
            if expire_date_of_paper:
                self.bo_write_date('Expire date of paper', expire_date_of_paper)
            self.key_escape()
            if group_type:
                self.bo_select('Group type', group_type)
            self.key_escape()
            if group_sub_type:
                self.bo_select('Group sub type', group_sub_type)
            self.key_escape()
            if economic_sector:
                self.bo_select('Economic sector', economic_sector)
            if reason_for_other_economic_sector:
                self.bo_write_text('Reason for Other (Economic sector)', reason_for_other_economic_sector)
            self.key_escape()
            if sub_economic_sector:
                self.bo_select('Sub economic sector', sub_economic_sector)
            if reason_for_other_sub_economic_sector:
                self.bo_write_text('Reason for Other (Sub economic sector)', reason_for_other_sub_economic_sector)
            self.key_escape()
            if customer_segment:
                self.bo_select('Customer segment', customer_segment)
            self.key_escape()
            if resident_status:
                self.bo_select('Resident status', resident_status)
            self.key_escape()
            if bank_identification:
                self.bo_select('Bank Identification', bank_identification)
            if fdi_info:
                self.bo_write_text('FDI info', fdi_info)
            if home_01:
                self.bo_click_collap('Legal address')
                self.bo_write_text_multi('Legal address', 'Home', home_01)
            if street_01:
                self.bo_click_collap('Legal address')
                self.bo_write_text_multi('Legal address', 'Street', street_01)
            if ward_01:
                self.bo_click_collap('Legal address')
                self.bo_write_text_multi('Legal address', 'Ward', ward_01)
            if township_01:
                self.bo_click_collap('Legal address')
                self.bo_write_text_multi('Legal address', 'Township', township_01)
            if province_01:
                self.bo_click_collap('Legal address')
                self.bo_write_text_multi('Legal address', 'Province', province_01)
            if home_02:
                self.bo_click_collap('Contact local address')
                self.bo_write_text_multi('Contact local address', 'Home', home_02)
            if street_02:
                self.bo_click_collap('Contact local address')
                self.bo_write_text_multi('Contact local address', 'Street', street_02)
            if ward_02:
                self.bo_click_collap('Contact local address')
                self.bo_write_text_multi('Contact local address', 'Ward', ward_02)
            if township_02:
                self.bo_click_collap('Contact local address')
                self.bo_write_text_multi('Contact local address', 'Township', township_02)
            if province_02:
                self.bo_click_collap('Contact local address')
                self.bo_write_text_multi('Contact local address', 'Province', province_02)
            if name_01:
                self.bo_click_collap('Introducer 1')
                self.bo_write_text_multi('Introducer 1', 'Name', name_01)
            if account_no_01:
                self.bo_click_collap('Introducer 1')
                self.bo_write_multi('Introducer 1', 'Account No', account_no_01)
            if name_02:
                self.bo_click_collap('Introducer 2')
                self.bo_write_text_multi('Introducer 2', 'Name', name_02)
            if account_no_02:
                self.bo_click_collap('Introducer 2')
                self.bo_write_multi('Introducer 2', 'Account No', account_no_02)
            if home_phone:
                self.bo_write_text('Home phone', home_phone)
            if mobile_phone:
                self.bo_write_text('Mobile phone', mobile_phone)
            if email_address:
                self.bo_write('Email address', email_address)
            self.key_escape()
            if education:
                self.bo_select('Education', education)
            self.key_escape()
            if marital_status:
                self.bo_select('Marital status', marital_status)
            if employer_name:
                self.bo_write_text('Employer Name', employer_name)
            self.key_escape()
            if occupation:
                self.bo_select('Occupation', occupation)
            if reason_for_other_occupation:
                self.bo_write_text('Reason for Other (Occupation)', reason_for_other_occupation)
            self.key_escape()
            if financial_institute:
                self.bo_select('Financial Institute', financial_institute)
            self.key_escape()
            if business_type:
                self.bo_select('Business Type', business_type)
            if reason_for_other_business_type:
                self.bo_write_text('Reason for Other (Business Type)', reason_for_other_business_type)
            if isic_code:
                self.bo_write_group('ISIC Code', isic_code)
            self.bo_click_tab('Other information')
            self.key_escape()
            if classification:
                self.bo_select('Classification', classification)
            self.key_escape()
            if country_of_income:
                self.bo_select('Country of Income', country_of_income)
            if government_organization_id:
                self.bo_write_text('Government Organization ID', government_organization_id)
            if international_organization_and_oversea_government_id:
                self.bo_write_text('International Organization and Oversea Government ID', international_organization_and_oversea_government_id)
            if oversea_juristic_id:
                self.bo_write_text('Oversea Juristic ID', oversea_juristic_id)
            if gfmis_code:
                self.bo_write_text('GFMIS Code', gfmis_code)
            self.key_escape()
            if account_owner_referral_rm:
                self.bo_select('Account Owner/Referral/RM', account_owner_referral_rm)
            self.key_escape()
            if account_operations:
                self.bo_select('Account Operations', account_operations)
            if remark_field_to_add:
                self.bo_write_text('Remark field to add', remark_field_to_add)
            if position:
                self.bo_write_text('Position', position)
            self.key_escape()
            if income:
                self.bo_select('Income', income)
            self.bo_click_tab('Credit line information')
            if credit_line:
                self.bo_write_number_group('Credit line', credit_line)
            self.key_escape()
            if currency:
                self.bo_select_group('Currency', currency)
            if mm_limit:
                self.bo_write_number_group('MM limit ', mm_limit)
            self.key_escape()
            if currency_mm:
                self.bo_select_group('Currency MM', currency_mm)
            if fx_limit:
                self.bo_write_number_group('FX limit', fx_limit)
            self.key_escape()
            if currency_fx:
                self.bo_select_group('Currency FX ', currency_fx)
            # assert value
            self.bo_click_tab('General information')
            if customer_code:
                self.bo_assert_value('Customer code', self.customer_code_mask(customer_code))
            if business_line:
                self.bo_assert_select('Business line', business_line)
            if customer_type:
                self.bo_assert_select('Customer type', customer_type)
            if managing_branch_code:
                self.bo_assert_value_group('Managing branch code', managing_branch_code)
            if status:
                self.bo_assert_select('Status', status)
            self.bo_click_tab('Other information')
            if open_date:
                self.bo_assert_date('Open date', open_date)
            if approve_date:
                self.bo_assert_date('Approve date', approve_date)
            if last_date:
                self.bo_assert_date('Last date', last_date)
            if branch_code:
                self.bo_assert_value_group('Branch code', branch_code)
            if created_by:
                self.bo_assert_value_group('Created by', created_by)
            if approved_by:
                self.bo_assert_value_group('Approved by', approved_by)
            if last_modify_user:
                self.bo_assert_text('Last modify user', last_modify_user)
            if last_approve_modify_user:
                self.bo_assert_text('Last approve modify user', last_approve_modify_user)
        else:
            # update value
            self.bo_click_tab('General information')
            self.key_escape()
            if title:
                self.bo_select('Title', title)
            self.key_escape()
            if title_of_organization:
                self.bo_select('Title of organization', title_of_organization)
            self.key_escape()
            if customer_sub_type:
                self.bo_select('Customer sub type', customer_sub_type)
            self.key_escape()
            if suffix:
                self.bo_select('Suffix', suffix)
            self.key_escape()
            if gender:
                self.bo_select('Gender', gender)
            if date_of_birth_starting_date_of_company:
                self.bo_write_date('Date of birth/Starting date of company', date_of_birth_starting_date_of_company)
            if place_of_birth:
                self.bo_write_text('Place of birth', place_of_birth)
            self.key_escape()
            if nationality:
                self.bo_select('Nationality', nationality)
            self.key_escape()
            if country_of_company:
                self.bo_select('Country of company', country_of_company)
            self.key_escape()
            if paper_type:
                self.bo_select('Paper type', paper_type)
            if reason_for_other_paper_type:
                self.bo_write_text('Reason for Other (Paper type)', reason_for_other_paper_type)
            if tin_number:
                self.bo_write('TIN number', tin_number)
            if issue_date_of_paper:
                self.bo_write_date('Issue date of paper', issue_date_of_paper)
            if issue_place_of_paper:
                self.bo_write_text('Issue place of paper', issue_place_of_paper)
            if expire_date_of_paper:
                self.bo_write_date('Expire date of paper', expire_date_of_paper)
            self.key_escape()
            if group_type:
                self.bo_select('Group type', group_type)
            self.key_escape()
            if group_sub_type:
                self.bo_select('Group sub type', group_sub_type)
            self.key_escape()
            if economic_sector:
                self.bo_select('Economic sector', economic_sector)
            if reason_for_other_economic_sector:
                self.bo_write_text('Reason for Other (Economic sector)', reason_for_other_economic_sector)
            self.key_escape()
            if sub_economic_sector:
                self.bo_select('Sub economic sector', sub_economic_sector)
            if reason_for_other_sub_economic_sector:
                self.bo_write_text('Reason for Other (Sub economic sector)', reason_for_other_sub_economic_sector)
            self.key_escape()
            if customer_segment:
                self.bo_select('Customer segment', customer_segment)
            self.key_escape()
            if resident_status:
                self.bo_select('Resident status', resident_status)
            self.key_escape()
            if bank_identification:
                self.bo_select('Bank Identification', bank_identification)
            if fdi_info:
                self.bo_write_text('FDI info', fdi_info)
            if name_01:
                self.bo_click_collap('Introducer 1')
                self.bo_write_text_multi('Introducer 1', 'Name', name_01)
            if account_no_01:
                self.bo_click_collap('Introducer 1')
                self.bo_write_multi('Introducer 1', 'Account No', account_no_01)
            if name_02:
                self.bo_click_collap('Introducer 2')
                self.bo_write_text_multi('Introducer 2', 'Name', name_02)
            if account_no_02:
                self.bo_click_collap('Introducer 2')
                self.bo_write_multi('Introducer 2', 'Account No', account_no_02)
            if home_phone:
                self.bo_write_text('Home phone', home_phone)
            self.key_escape()
            if education:
                self.bo_select('Education', education)
            self.key_escape()
            if marital_status:
                self.bo_select('Marital status', marital_status)
            if employer_name:
                self.bo_write_text('Employer Name', employer_name)
            self.key_escape()
            if occupation:
                self.bo_select('Occupation', occupation)
            if reason_for_other_occupation:
                self.bo_write_text('Reason for Other (Occupation)', reason_for_other_occupation)
            self.key_escape()
            if financial_institute:
                self.bo_select('Financial Institute', financial_institute)
            self.key_escape()
            if business_type:
                self.bo_select('Business Type', business_type)
            if reason_for_other_business_type:
                self.bo_write_text('Reason for Other (Business Type)', reason_for_other_business_type)
            if isic_code:
                self.bo_write_group('ISIC Code', isic_code)
            self.bo_click_tab('Other information')
            self.key_escape()
            if classification:
                self.bo_select('Classification', classification)
            self.key_escape()
            if country_of_income:
                self.bo_select('Country of Income', country_of_income)
            if government_organization_id:
                self.bo_write_text('Government Organization ID', government_organization_id)
            if international_organization_and_oversea_government_id:
                self.bo_write_text('International Organization and Oversea Government ID', international_organization_and_oversea_government_id)
            if oversea_juristic_id:
                self.bo_write_text('Oversea Juristic ID', oversea_juristic_id)
            if gfmis_code:
                self.bo_write_text('GFMIS Code', gfmis_code)
            self.key_escape()
            if account_owner_referral_rm:
                self.bo_select('Account Owner/Referral/RM', account_owner_referral_rm)
            self.key_escape()
            if account_operations:
                self.bo_select('Account Operations', account_operations)
            if remark_field_to_add:
                self.bo_write_text('Remark field to add', remark_field_to_add)
            if position:
                self.bo_write_text('Position', position)
            self.key_escape()
            if income:
                self.bo_select('Income', income)
            self.bo_click_tab('Credit line information')
            if credit_line:
                self.bo_write_number_group('Credit line', credit_line)
            self.key_escape()
            if currency:
                self.bo_select_group('Currency', currency)
            if mm_limit:
                self.bo_write_number_group('MM limit ', mm_limit)
            self.key_escape()
            if currency_mm:
                self.bo_select_group('Currency MM', currency_mm)
            if fx_limit:
                self.bo_write_number_group('FX limit', fx_limit)
            self.key_escape()
            if currency_fx:
                self.bo_select_group('Currency FX ', currency_fx)
            # assert value
            self.bo_click_tab('General information')
            if customer_code:
                self.bo_assert_value('Customer code', self.customer_code_mask(customer_code))
            if business_line:
                self.bo_assert_select('Business line', business_line)
            if customer_type:
                self.bo_assert_select('Customer type', customer_type)
            if first_name_en:
                self.bo_assert_text('First name (en)', first_name_en)
            if last_name_en:
                self.bo_assert_text('Last name (en)', last_name_en)
            if full_name:
                self.bo_assert_text('Full name', full_name)
            if father_name:
                self.bo_assert_text('Father name', father_name)
            if paper_number:
                self.bo_assert_text('Paper number', paper_number)
            if home_01:
                self.bo_click_collap('Legal address')
                self.bo_assert_text_multi('Legal address', 'Home', home_01)
            if street_01:
                self.bo_click_collap('Legal address')
                self.bo_assert_text_multi('Legal address', 'Street', street_01)
            if ward_01:
                self.bo_click_collap('Legal address')
                self.bo_assert_text_multi('Legal address', 'Ward', ward_01)
            if township_01:
                self.bo_click_collap('Legal address')
                self.bo_assert_text_multi('Legal address', 'Township', township_01)
            if province_01:
                self.bo_click_collap('Legal address')
                self.bo_assert_text_multi('Legal address', 'Province', province_01)
            if home_02:
                self.bo_click_collap('Contact local address')
                self.bo_assert_text_multi('Contact local address', 'Home', home_02)
            if street_02:
                self.bo_click_collap('Contact local address')
                self.bo_assert_text_multi('Contact local address', 'Street', street_02)
            if ward_02:
                self.bo_click_collap('Contact local address')
                self.bo_assert_text_multi('Contact local address', 'Ward', ward_02)
            if township_02:
                self.bo_click_collap('Contact local address')
                self.bo_assert_text_multi('Contact local address', 'Township', township_02)
            if province_02:
                self.bo_click_collap('Contact local address')
                self.bo_assert_text_multi('Contact local address', 'Province', province_02)
            if mobile_phone:
                self.bo_assert_text('Mobile phone', mobile_phone)
            if email_address:
                self.bo_assert_value('Email address', email_address)
            if managing_branch_code:
                self.bo_assert_value_group('Managing branch code', managing_branch_code)
            if status:
                self.bo_assert_select('Status', status)
            self.bo_click_tab('Other information')
            if open_date:
                self.bo_assert_date('Open date', open_date)
            if approve_date:
                self.bo_assert_date('Approve date', approve_date)
            if last_date:
                self.bo_assert_date('Last date', last_date)
            if branch_code:
                self.bo_assert_value_group('Branch code', branch_code)
            if created_by:
                self.bo_assert_value_group('Created by', created_by)
            if approved_by:
                self.bo_assert_value_group('Approved by', approved_by)
            if last_modify_user:
                self.bo_assert_text('Last modify user', last_modify_user)
            if last_approve_modify_user:
                self.bo_assert_text('Last approve modify user', last_approve_modify_user)
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
            self.check_notification('Save successfully')
            self.bo_click_tab('General information')
            customer_code_out=self.bo_get_value('Customer code')
            print(f'Customer code: {customer_code_out}')
            return customer_code_out

    def customer_profile_delete(self, customer_code, list_error_message=None):
        # search
        self.customer_profile_simple_search(str(customer_code).replace('-', ''))
        self.assert_table_data('Customer code', 1, self.customer_code_mask(customer_code))
        # delete
        self.click_table_menu('Delete', 1)
        self.wait_loading()
        self.click_button_in_popup('Yes')
        if list_error_message:
        # verify error
            self.assert_error_message()
            self.assert_list_error_message(list_error_message)
            print(f"Action delete '{customer_code}' failed!")
        else:
        # verify success
            self.check_notification('Deleted successfully')
            self.wait_loading()
            self.customer_profile_simple_search(str(customer_code).replace('-', ''))
            self.assert_search_not_found()
            print(f'Deleted: {customer_code}')
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
    def customer_approve_profile_modification_simple_search(self, text):
        self.close_all_form()
        self.click_menu('Customer', 'Approve Modify Customer')
        self.wait_for_button_available('Search')
        self.assert_form_title('CTM-Approve Profile Modification-Search')
        self.simple_search(text=text, placeholder='Search text')
        self.wait_loading()

    def customer_approve_profile_modification_advanced_search(self, customer_code=None, full_name=None, paper_number=None, date_of_birth_from=None, date_of_birth_to=None, gender=None, customer_status=None, nationality=None, resident_status=None, address=None, approver=None, old_id_of_customer=None, branch_code=None):
        self.close_all_form()
        self.click_menu('Customer', 'Approve Modify Customer')
        self.wait_for_button_available('Search')
        self.assert_form_title('CTM-Approve Profile Modification-Search')
        if customer_code:
            self.adv_search('Customer code', str(customer_code).replace('-', ''))
        if full_name:
            self.adv_search_text('Full name', full_name)
        if paper_number:
            self.adv_search_text('Paper number', paper_number)
        if date_of_birth_from:
            self.adv_search_group('Date of birth from', date_of_birth_from)
        if date_of_birth_to:
            self.adv_search_group('Date of birth to', date_of_birth_to)
        self.key_escape()
        if gender:
            self.adv_search_select('Gender', gender)
        self.key_escape()
        if customer_status:
            self.adv_search_select('Customer status', customer_status)
        self.key_escape()
        if nationality:
            self.adv_search_select('Nationality', nationality)
        self.key_escape()
        if resident_status:
            self.adv_search_select('Resident status', resident_status)
        if address:
            self.adv_search_text('Address', address)
        if approver:
            self.adv_search_text('Approver', approver)
        if old_id_of_customer:
            self.adv_search_text('Old id of customer', old_id_of_customer)
        self.key_escape()
        if branch_code:
            self.adv_search_select('Branch code', branch_code)
        self.click_button_search_advanced()
        self.wait_loading()

    def customer_approve_profile_modification_view(self, customer_code=None, business_line=None, customer_type=None, customer_sub_type=None, ctmsubtype_modification=None, title=None, title_modification=None, title_of_organization=None, titleorg_modification=None, suffix=None, suffix_modification=None, first_name_en=None, last_name_en=None, full_name=None, father_name=None, gender=None, gender_modification=None, date_of_birth=None, dob_modification=None, starting_date_of_company=None, dob1_modification=None, place_of_birth=None, nationality=None, nation_modification=None, country_of_company=None, country_modification=None, paper_type=None, repidtype_modification=None, reason_for_other_paper_type=None, paper_number=None, tin_number=None, issue_date_of_paper=None, iddt_modification=None, issue_place_of_paper=None, expire_date_of_paper=None, idexpdt_modification=None, repidtypes_modification=None, iddts_modification=None, group_type=None, grptypec_modification=None, group_sub_type=None, grpstypec_modification=None, sector_modification=None, reason_for_other_economic_sector=None, subsector_modification=None, reason_for_other_sub_economic_sector=None, customer_segment=None, ctmsize_modification=None, resident_status=None, resident_modification=None, bank_identification=None, bank_identification_modification=None, fdi_info=None, home_phone=None, mobile_phone=None, email_address=None, education=None, educd_modification=None, marital_status=None, mstatus_modification=None, employer_name=None, occupation=None, profession_modification=None, reason_for_other_occupation=None, financial_institute=None, ficd_modification=None, business_type=None, bucd_modification=None, reason_for_other_business_type=None, isic_code=None, managing_branch_code=None, status=None, classification=None, classify_modification=None, polists_modification=None, repolists_modification=None, country_of_income=None, ctnincome_modification=None, fatcasts_modification=None, open_date=None, opndt_modification=None, approve_date=None, aprdt_modification=None, last_date=None, government_organization_id=None, international_organization_and_oversea_government_id=None, oversea_juristic_id=None, gfmis_code=None, branch_code=None, created_by=None, approved_by=None, account_owner_referral_rm=None, referral_field_modification_copy=None, account_operations=None, introducer_modification=None, remark_field_to_add=None, position=None, income=None, income_modification=None, last_modify_user=None, last_approve_modify_user=None, credit_line=None, ctmline_modification=None, currency=None, ccrcd_modification=None, mm_limit=None, mm_limit_modify=None, currency_mm=None, currency_mm_modify=None, fx_limit=None, fx_limit_modify=None, currency_fx=None, currency_fx_modify=None):
        # search
        self.customer_approve_profile_modification_simple_search(str(customer_code).replace('-', ''))
        self.assert_table_data('Customer code', 1, self.customer_code_mask(customer_code))
        # view
        self.click_table_menu(row=1)
        self.wait_for_button_available('View Modification')
        self.assert_form_title('CTM-Approve Profile Modification-View')
        # verify value
        self.bo_click_tab('General information')
        if customer_code:
            self.bo_assert_value('Customer code', self.customer_code_mask(customer_code))
        if business_line:
            self.bo_assert_select('Business line', business_line)
        if customer_type:
            self.bo_assert_select('Customer type', customer_type)
        if customer_sub_type:
            self.bo_assert_select_group('Customer sub type', customer_sub_type)
        if ctmsubtype_modification:
            self.bo_assert_select_group('ctmsubtype_modification', ctmsubtype_modification)
        if title:
            self.bo_assert_select_group('Title', title)
        if title_modification:
            self.bo_assert_select_group('title_modification', title_modification)
        if title_of_organization:
            self.bo_assert_select_group('Title of organization', title_of_organization)
        if titleorg_modification:
            self.bo_assert_select_group('titleorg_modification', titleorg_modification)
        if suffix:
            self.bo_assert_select_group('Suffix ', suffix)
        if suffix_modification:
            self.bo_assert_select_group('suffix_modification', suffix_modification)
        if first_name_en:
            self.bo_assert_text_group('First name (en)', first_name_en)
        if last_name_en:
            self.bo_assert_text_group('Last name (en)', last_name_en)
        if full_name:
            self.bo_assert_text_group('Full name', full_name)
        if father_name:
            self.bo_assert_text_group('Father name', father_name)
        if gender:
            self.bo_assert_select_group('Gender', gender)
        if gender_modification:
            self.bo_assert_select_group('gender_modification', gender_modification)
        if date_of_birth:
            self.bo_assert_date_group('Date of birth', date_of_birth)
        if dob_modification:
            self.bo_assert_date_group('dob_modification', dob_modification)
        if starting_date_of_company:
            self.bo_assert_date_group('Starting date of company', starting_date_of_company)
        if dob1_modification:
            self.bo_assert_date_group('dob1_modification', dob1_modification)
        if place_of_birth:
            self.bo_assert_text_group('Place of birth', place_of_birth)
        if nationality:
            self.bo_assert_select_group('Nationality', nationality)
        if nation_modification:
            self.bo_assert_select_group('nation_modification', nation_modification)
        if country_of_company:
            self.bo_assert_select_group('Country of Company', country_of_company)
        if country_modification:
            self.bo_assert_select_group('country_modification', country_modification)
        if paper_type:
            self.bo_assert_select_group('Paper type', paper_type)
        if repidtype_modification:
            self.bo_assert_select_group('repidtype_modification', repidtype_modification)
        if reason_for_other_paper_type:
            self.bo_assert_text_group('Reason for Other (Paper type)', reason_for_other_paper_type)
        if paper_number:
            self.bo_assert_text_group('Paper number', paper_number)
        if tin_number:
            self.bo_assert_value_group('TIN number', tin_number)
        if issue_date_of_paper:
            self.bo_assert_date_group('Issue date of paper', issue_date_of_paper)
        if iddt_modification:
            self.bo_assert_date_group('iddt_modification', iddt_modification)
        if issue_place_of_paper:
            self.bo_assert_text_group('Issue place of paper', issue_place_of_paper)
        if expire_date_of_paper:
            self.bo_assert_date_group('Expire date of paper', expire_date_of_paper)
        if idexpdt_modification:
            self.bo_assert_date_group('idexpdt_modification', idexpdt_modification)
        if repidtypes_modification:
            self.bo_assert_select_group('repidtypes_modification', repidtypes_modification)
        if iddts_modification:
            self.bo_assert_date_group('iddts_modification', iddts_modification)
        if group_type:
            self.bo_assert_select_group('Group type', group_type)
        if grptypec_modification:
            self.bo_assert_select_group('grptypec_modification', grptypec_modification)
        if group_sub_type:
            self.bo_assert_select_group('Group sub type', group_sub_type)
        if grpstypec_modification:
            self.bo_assert_select_group('grpstypec_modification', grpstypec_modification)
        if sector_modification:
            self.bo_assert_select_group('sector_modification', sector_modification)
        if reason_for_other_economic_sector:
            self.bo_assert_text_group('Reason for Other (Economic sector)', reason_for_other_economic_sector)
        if subsector_modification:
            self.bo_assert_select_group('subsector_modification', subsector_modification)
        if reason_for_other_sub_economic_sector:
            self.bo_assert_text_group('Reason for Other (Sub economic sector)', reason_for_other_sub_economic_sector)
        if customer_segment:
            self.bo_assert_select_group('Customer segment', customer_segment)
        if ctmsize_modification:
            self.bo_assert_select_group('ctmsize_modification', ctmsize_modification)
        if resident_status:
            self.bo_assert_select_group('Resident status', resident_status)
        if resident_modification:
            self.bo_assert_select_group('resident_modification', resident_modification)
        if bank_identification:
            self.bo_assert_select_group('Bank Identification', bank_identification)
        if bank_identification_modification:
            self.bo_assert_select_group('bank_identification_modification', bank_identification_modification)
        if fdi_info:
            self.bo_assert_text_group('FDI info', fdi_info)
        if home_phone:
            self.bo_assert_text_group('Home phone', home_phone)
        if mobile_phone:
            self.bo_assert_text_group('Mobile Phone', mobile_phone)
        if email_address:
            self.bo_assert_value_group('Email address', email_address)
        if education:
            self.bo_assert_select_group('Education', education)
        if educd_modification:
            self.bo_assert_select_group('educd_modification', educd_modification)
        if marital_status:
            self.bo_assert_select_group('Marital status', marital_status)
        if mstatus_modification:
            self.bo_assert_select_group('mstatus_modification', mstatus_modification)
        if employer_name:
            self.bo_assert_text_group('Employer Name', employer_name)
        if occupation:
            self.bo_assert_select_group('Occupation', occupation)
        if profession_modification:
            self.bo_assert_select_group('profession_modification', profession_modification)
        if reason_for_other_occupation:
            self.bo_assert_text_group('Reason for Other (Occupation)', reason_for_other_occupation)
        if financial_institute:
            self.bo_assert_select_group('Financial Institute', financial_institute)
        if ficd_modification:
            self.bo_assert_select_group('ficd_modification', ficd_modification)
        if business_type:
            self.bo_assert_select_group('Business Type', business_type)
        if bucd_modification:
            self.bo_assert_select_group('bucd_modification', bucd_modification)
        if reason_for_other_business_type:
            self.bo_assert_text_group('Reason for Other (Business Type)', reason_for_other_business_type)
        if isic_code:
            self.bo_assert_text_group('ISIC Code', isic_code)
        if managing_branch_code:
            self.bo_assert_value_group('Managing branch code', managing_branch_code)
        if status:
            self.bo_assert_select('Status', status)
        self.bo_click_tab('Other information')
        if classification:
            self.bo_assert_select_group('Classification', classification)
        if classify_modification:
            self.bo_assert_select_group('classify_modification', classify_modification)
        if polists_modification:
            self.bo_assert_select_group('polists_modification', polists_modification)
        if repolists_modification:
            self.bo_assert_select_group('repolists_modification', repolists_modification)
        if country_of_income:
            self.bo_assert_select_group('Country of Income', country_of_income)
        if ctnincome_modification:
            self.bo_assert_select_group('ctnincome_modification', ctnincome_modification)
        if fatcasts_modification:
            self.bo_assert_select_group('fatcasts_modification', fatcasts_modification)
        if open_date:
            self.bo_assert_date_group('Open date', open_date)
        if opndt_modification:
            self.bo_assert_date_group('opndt_modification', opndt_modification)
        if approve_date:
            self.bo_assert_date_group('Approve date', approve_date)
        if aprdt_modification:
            self.bo_assert_date_group('aprdt_modification', aprdt_modification)
        if last_date:
            self.bo_assert_date('Last date', last_date)
        if government_organization_id:
            self.bo_assert_text_group('Government Organization ID', government_organization_id)
        if international_organization_and_oversea_government_id:
            self.bo_assert_text_group('International Organization and Oversea Government ID', international_organization_and_oversea_government_id)
        if oversea_juristic_id:
            self.bo_assert_text_group('Oversea Juristic ID', oversea_juristic_id)
        if gfmis_code:
            self.bo_assert_text_group('GFMIS Code', gfmis_code)
        if branch_code:
            self.bo_assert_value_group('Branch code', branch_code)
        if created_by:
            self.bo_assert_value_group('Created by', created_by)
        if approved_by:
            self.bo_assert_value_group('Approved by', approved_by)
        if account_owner_referral_rm:
            self.bo_assert_select_group('Account Owner/Referral/RM', account_owner_referral_rm)
        if referral_field_modification_copy:
            self.bo_assert_select_group('referral_field_modification Copy', referral_field_modification_copy)
        if account_operations:
            self.bo_assert_select_group('Account Operations', account_operations)
        if introducer_modification:
            self.bo_assert_select_group('introducer_modification', introducer_modification)
        if remark_field_to_add:
            self.bo_assert_text_group('Remark field to add', remark_field_to_add)
        if position:
            self.bo_assert_text_group('Position', position)
        if income:
            self.bo_assert_select_group('Income', income)
        if income_modification:
            self.bo_assert_select_group('income_modification', income_modification)
        if last_modify_user:
            self.bo_assert_text('Last modify user', last_modify_user)
        if last_approve_modify_user:
            self.bo_assert_text('Last approve modify user', last_approve_modify_user)
        self.bo_click_tab('Credit line information')
        if credit_line:
            self.bo_assert_value_group('Credit line', credit_line)
        if ctmline_modification:
            self.bo_assert_value_group('ctmline_modification', ctmline_modification)
        if currency:
            self.bo_assert_select_group('Currency', currency)
        if ccrcd_modification:
            self.bo_assert_select_group('ccrcd_modification', ccrcd_modification)
        if mm_limit:
            self.bo_assert_value_group('MM limit ', mm_limit)
        if mm_limit_modify:
            self.bo_assert_value_group('MM limit modify', mm_limit_modify)
        if currency_mm:
            self.bo_assert_select_group('Currency MM', currency_mm)
        if currency_mm_modify:
            self.bo_assert_select_group('Currency MM modify', currency_mm_modify)
        if fx_limit:
            self.bo_assert_value_group('FX limit', fx_limit)
        if fx_limit_modify:
            self.bo_assert_value_group('FX limit modify ', fx_limit_modify)
        if currency_fx:
            self.bo_assert_select_group('Currency FX ', currency_fx)
        if currency_fx_modify:
            self.bo_assert_select_group('Currency FX modify ', currency_fx_modify)

    def customer_approve_profile_modification_approve(self, customer_code):
        self.customer_approve_profile_modification_view(customer_code=customer_code)
        self.click_button('View Modification')
        self.wait_loading()
        self.click_button('Approve')
        self.wait_loading()
        self.check_notification('Approve successfully')
        # back to tab 'General information'
        self.bo_click_tab('General information')
        customer_code = self.bo_get_value('Customer code')
        print('Customer code: ' + customer_code)
        self.customer_approve_profile_modification_simple_search(str(customer_code).replace('-', ''))
        self.assert_search_not_found()
        return customer_code

    def customer_approve_profile_modification_reject(self, customer_code):
        self.customer_approve_profile_modification_view(customer_code=customer_code)
        self.click_button('View Modification')
        self.wait_loading()
        self.click_button('Reject')
        self.wait_loading()
        self.check_notification('Reject successfully')
        # back to tab 'General information'
        self.bo_click_tab('General information')
        customer_code = self.bo_get_value('Customer code')
        print('Customer code: ' + customer_code)
        self.customer_approve_profile_modification_simple_search(str(customer_code).replace('-', ''))
        self.assert_search_not_found()
        return customer_code

    # CTM-Customer Linkage
    def customer_linkage_simple_search(self, text):
        self.close_all_form()
        self.click_menu('Customer', 'Customer Linkage')
        self.wait_for_button_available('Search')
        self.assert_form_title('CTM-Customer Linkage-Search')
        self.simple_search(text=text, placeholder='Search Text')
        self.wait_loading()

    def customer_linkage_advanced_search(self, master_customer_code=None, master_customer_name=None, credit_line_from=None, credit_line_to=None, group_limit_code=None, linkage_description=None, linkage_status=None):
        self.close_all_form()
        self.click_menu('Customer', 'Customer Linkage')
        self.wait_for_button_available('Search')
        self.assert_form_title('CTM-Customer Linkage-Search')
        if master_customer_code:
            self.adv_search('Master customer code', master_customer_code)
        if master_customer_name:
            self.adv_search_text('Master customer name', master_customer_name)
        if credit_line_from:
            self.adv_search_group('Credit line from', credit_line_from)
        if credit_line_to:
            self.adv_search_group('Credit line to', credit_line_to)
        if group_limit_code:
            self.adv_search_text('Group limit code', group_limit_code)
        self.key_escape()
        if linkage_description:
            self.adv_search_select('Linkage description', linkage_description)
        self.key_escape()
        if linkage_status:
            self.adv_search_select('Linkage status', linkage_status)
        self.click_button_search_advanced()
        self.wait_loading()

    def customer_linkage_view(self, master_customer_code=None, linkage_description=None, linkage_status=None, group_limit_code=None, credit_line=None, curency=None, mm_limit=None, currency_mm=None, fx_limit=None, currency_fx=None):
        # search
        self.customer_linkage_simple_search(str(master_customer_code).replace('-', ''))
        self.assert_table_data('Master Customer Code', 1, self.customer_code_mask(master_customer_code))
        # view
        self.click_table_menu('View', 1)
        self.wait_for_button_available('Modify')
        self.assert_form_title('CTM-Customer Linkage-View')
        # verify value
        self.bo_click_tab('General Information')
        if master_customer_code:
            self.bo_assert_value_group('Master Customer Code', self.customer_code_mask(master_customer_code))
        if linkage_description:
            self.bo_assert_select('Linkage description', linkage_description)
        if linkage_status:
            self.bo_assert_select('Linkage status', linkage_status)
        self.bo_click_tab('Credit Line Information')
        if group_limit_code:
            self.bo_assert_value_group('Group limit code', group_limit_code)
        if credit_line:
            self.bo_assert_value_group('Credit Line', credit_line)
        if curency:
            self.bo_assert_select_group('Curency', curency)
        if mm_limit:
            self.bo_assert_value_group('MM Limit ', mm_limit)
        if currency_mm:
            self.bo_assert_select_group('Currency MM', currency_mm)
        if fx_limit:
            self.bo_assert_value_group('FX Limit', fx_limit)
        if currency_fx:
            self.bo_assert_select_group('Currency FX', currency_fx)

    def customer_linkage_update(self, master_customer_code=None, linkage_description=None, linkage_status=None, group_limit_code=None, credit_line=None, curency=None, mm_limit=None, currency_mm=None, fx_limit=None, currency_fx=None, detail_customer_code=None, linkage_type=None, list_error_message=None):
        # view
        self.customer_linkage_view(master_customer_code=master_customer_code)
        self.click_button('Modify')
        self.wait_loading()
        # update value
        self.bo_click_tab('General Information')
        self.key_escape()
        if linkage_description:
            self.bo_select('Linkage description', linkage_description)
        self.key_escape()
        if linkage_status:
            self.bo_select('Linkage status', linkage_status)
        if detail_customer_code:
            self.click_button('Add')
            self.bo_write_data('Detail customer code', detail_customer_code)
            self.key_escape()
            if linkage_type:
                self.bo_select_data('Linkage type', linkage_type)
            self.click_button('Apply')
            self.wait_loading()
        self.bo_click_tab('Credit Line Information')
        if group_limit_code:
            self.bo_write_group('Group limit code', group_limit_code)
        if credit_line:
            self.bo_write_number_group('Credit Line', credit_line)
        self.key_escape()
        if curency:
            self.bo_select_group('Curency', curency)
        if mm_limit:
            self.bo_write_number_group('MM Limit ', mm_limit)
        self.key_escape()
        if currency_mm:
            self.bo_select_group('Currency MM', currency_mm)
        if fx_limit:
            self.bo_write_number_group('FX Limit', fx_limit)
        self.key_escape()
        if currency_fx:
            self.bo_select_group('Currency FX', currency_fx)
        # assert value
        self.bo_click_tab('General Information')
        if master_customer_code:
            self.bo_assert_value_group('Master Customer Code', self.customer_code_mask(master_customer_code))
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
            self.bo_click_tab('General Information')
            master_customer_code_out=self.bo_get_value_group('Master Customer Code')
            print(f'Master Customer Code: {master_customer_code_out}')
            return master_customer_code_out

    def customer_linkage_delete(self, master_customer_code=None, list_error_message=None):
        # search
        self.customer_linkage_simple_search(str(master_customer_code).replace('-', ''))
        self.assert_table_data('Master Customer Code', 1, self.customer_code_mask(master_customer_code))
        # delete
        self.click_table_menu('Delete', 1)
        self.wait_loading()
        self.click_button_in_popup('Yes')
        if list_error_message:
        # verify error
            self.assert_error_message()
            self.assert_list_error_message(list_error_message)
            print(f"Action delete '{master_customer_code}' failed!")
        else:
        # verify success
            self.check_notification('Deleted successfully')
            self.wait_loading()
            self.customer_linkage_simple_search(str(master_customer_code).replace('-', ''))
            self.assert_search_not_found()
            print(f'Deleted: {master_customer_code}')
            return master_customer_code

    # CTM-Approve Customer Linkage Modify
    def customer_approve_linkage_modify_simple_search(self, text):
        self.close_all_form()
        self.click_menu('Customer', 'Approve Modify Customer Linkage')
        self.wait_for_button_available('Search')
        self.assert_form_title('CTM-Approve Customer Linkage Modify-Search')
        self.simple_search(text=text, placeholder='Search Text')
        self.wait_loading()

    def customer_approve_linkage_modify_advanced_search(self, master_customer_code=None, master_customer_name=None, credit_line_from=None, credit_line_to=None, group_limit_code=None, linkage_description=None, linkage_status=None):
        self.close_all_form()
        self.click_menu('Customer', 'Approve Modify Customer Linkage')
        self.wait_for_button_available('Search')
        self.assert_form_title('CTM-Approve Customer Linkage Modify-Search')
        if master_customer_code:
            self.adv_search('Master customer code', master_customer_code)
        if master_customer_name:
            self.adv_search_text('Master customer name', master_customer_name)
        if credit_line_from:
            self.adv_search_group('Credit line from', credit_line_from)
        if credit_line_to:
            self.adv_search_group('Credit line to', credit_line_to)
        if group_limit_code:
            self.adv_search_text('Group limit code', group_limit_code)
        self.key_escape()
        if linkage_description:
            self.adv_search_select('Linkage description', linkage_description)
        self.key_escape()
        if linkage_status:
            self.adv_search_select('Linkage status', linkage_status)
        self.click_button_search_advanced()
        self.wait_loading()

    def customer_approve_linkage_modify_view(self, master_customer_code=None, linkage_description=None, linkage_description_modification=None, linkage_status=None, linkage_status_modification=None, group_limit_code=None, credit_line=None, credit_line_modify=None, curency=None, curency_copy=None, mm_limit=None, mm_limit_modify=None, currency_mm=None, currency_mm_modify=None, fx_limit=None, fx_limit_modify=None, currency_fx=None, currency_fx_modify=None):
        # search
        self.customer_approve_linkage_modify_simple_search(str(master_customer_code).replace('-', ''))
        self.assert_table_data('Master Customer Code', 1, self.customer_code_mask(master_customer_code))
        # view
        self.click_table_menu(row=1)
        self.wait_for_button_available('View Modification')
        self.assert_form_title('CTM-Approve Customer Linkage Modify-View')
        # verify value
        self.bo_click_tab('General Information')
        if master_customer_code:
            self.bo_assert_value_group('Master Customer Code', self.customer_code_mask(master_customer_code))
        if linkage_description:
            self.bo_assert_select_group('Linkage description', linkage_description)
        if linkage_description_modification:
            self.bo_assert_select_group('linkage_description_modification', linkage_description_modification)
        if linkage_status:
            self.bo_assert_select_group('Linkage status', linkage_status)
        if linkage_status_modification:
            self.bo_assert_select_group('linkage_status_modification', linkage_status_modification)
        self.bo_click_tab('Credit Line Information')
        if group_limit_code:
            self.bo_assert_value_group('Group limit code', group_limit_code)
        if credit_line:
            self.bo_assert_value_group('Credit Line', credit_line)
        if credit_line_modify:
            self.bo_assert_value_group('credit_line_modify', credit_line_modify)
        if curency:
            self.bo_assert_select_group('Curency', curency)
        if curency_copy:
            self.bo_assert_select_group('Curency Copy', curency_copy)
        if mm_limit:
            self.bo_assert_value_group('MM Limit ', mm_limit)
        if mm_limit_modify:
            self.bo_assert_value_group('MM Limit Modify', mm_limit_modify)
        if currency_mm:
            self.bo_assert_select_group('Currency MM', currency_mm)
        if currency_mm_modify:
            self.bo_assert_select_group('Currency MM Modify', currency_mm_modify)
        if fx_limit:
            self.bo_assert_value_group('FX Limit', fx_limit)
        if fx_limit_modify:
            self.bo_assert_value_group('FX Limit Modify ', fx_limit_modify)
        if currency_fx:
            self.bo_assert_select_group('Currency FX', currency_fx)
        if currency_fx_modify:
            self.bo_assert_select_group('Currency FX Modify ', currency_fx_modify)

    def customer_approve_linkage_modify_approve(self, master_customer_code):
        self.customer_approve_linkage_modify_view(master_customer_code=master_customer_code)
        self.click_button('View Modification')
        self.wait_loading()
        self.click_button('Approve')
        self.wait_loading()
        self.check_notification('Approve successfully')
        # back to tab 'General Information'
        self.bo_click_tab('General Information')
        master_customer_code = self.bo_get_value_group('Master Customer Code')
        print('Master Customer Code: ' + master_customer_code)
        self.customer_approve_linkage_modify_simple_search(str(master_customer_code).replace('-', ''))
        self.assert_search_not_found()
        return master_customer_code

    def customer_approve_linkage_modify_reject(self, master_customer_code):
        self.customer_approve_linkage_modify_view(master_customer_code=master_customer_code)
        self.click_button('View Modification')
        self.wait_loading()
        self.click_button('Reject')
        self.wait_loading()
        self.check_notification('Reject successfully')
        # back to tab 'General Information'
        self.bo_click_tab('General Information')
        master_customer_code = self.bo_get_value_group('Master Customer Code')
        print('Master Customer Code: ' + master_customer_code)
        self.customer_approve_linkage_modify_simple_search(str(master_customer_code).replace('-', ''))
        self.assert_search_not_found()
        return master_customer_code

    # CTM-Customer relation management (Customer Group)
    def customer_relation_management_simple_search(self, text):
        self.close_all_form()
        self.click_menu('Customer', 'Customer Group')
        self.wait_for_button_available('Search')
        self.assert_form_title('CTM-Customer relation management-Search')
        self.simple_search(text=text, placeholder='Search Text')
        self.wait_loading()

    def customer_relation_management_advanced_search(self, master_customer_code=None, full_name=None, group_status=None):
        self.close_all_form()
        self.click_menu('Customer', 'Customer Group')
        self.wait_for_button_available('Search')
        self.assert_form_title('CTM-Customer relation management-Search')
        if master_customer_code:
            self.adv_search_text('Master customer code', master_customer_code)
        if full_name:
            self.adv_search_text('Full name', full_name)
        self.key_escape()
        if group_status:
            self.adv_search_select('Group status', group_status)
        self.click_button_search_advanced()
        self.wait_loading()

    def customer_relation_management_view(self, master_customer=None, full_name=None, group_status=None, group_limit_code=None, group_line=None, curency_code=None, mm_limit=None, currency_mm=None, fx_limit=None, currency_fx=None):
        # search
        self.customer_relation_management_simple_search(str(master_customer).replace('-', ''))
        self.assert_table_data('Mater customer code', 1, self.customer_code_mask(master_customer))
        # view
        self.click_table_menu('View', 1)
        self.wait_for_button_available('Modify')
        self.assert_form_title('CTM-Customer relation management-View')
        # verify value
        self.bo_click_tab('General Information')
        if master_customer:
            self.bo_assert_value('Master customer', self.customer_code_mask(master_customer))
        if full_name:
            self.bo_assert_text('Full name', full_name)
        if group_status:
            self.bo_assert_select('Group status', group_status)
        self.bo_click_tab('Credit Line Information')
        if group_limit_code:
            self.bo_assert_value_group('Group limit code', group_limit_code)
        if group_line:
            self.bo_assert_value_group('Group Line', group_line)
        if curency_code:
            self.bo_assert_select_group('Curency Code', curency_code)
        if mm_limit:
            self.bo_assert_value_group('MM Limit ', mm_limit)
        if currency_mm:
            self.bo_assert_select_group('Currency MM', currency_mm)
        if fx_limit:
            self.bo_assert_value_group('FX Limit', fx_limit)
        if currency_fx:
            self.bo_assert_select_group('Currency FX', currency_fx)

    def customer_relation_management_update(self, master_customer=None, full_name=None, group_status=None, group_limit_code=None, group_line=None, curency_code=None, mm_limit=None, currency_mm=None, fx_limit=None, currency_fx=None, customer_code=None, position=None, list_error_message=None):
        # view
        self.customer_relation_management_view(master_customer=master_customer)
        self.click_button('Modify')
        # update value
        self.bo_click_tab('General Information')
        self.key_escape()
        if group_status:
            self.bo_select('Group status', group_status)
        self.bo_click_tab('Credit Line Information')
        if group_limit_code:
            self.bo_write_group('Group limit code', group_limit_code)
        if group_line:
            self.bo_write_number_group('Group Line', group_line)
        self.key_escape()
        if curency_code:
            self.bo_select_group('Curency Code', curency_code)
        if mm_limit:
            self.bo_write_number_group('MM Limit ', mm_limit)
        self.key_escape()
        if currency_mm:
            self.bo_select_group('Currency MM', currency_mm)
        if fx_limit:
            self.bo_write_number_group('FX Limit', fx_limit)
        self.key_escape()
        if currency_fx:
            self.bo_select_group('Currency FX', currency_fx)
        # assert value
        self.bo_click_tab('General Information')
        if master_customer:
            self.bo_assert_value('Master customer', self.customer_code_mask(master_customer))
        if full_name:
            self.bo_assert_text('Full name', full_name)
        if customer_code:
            self.click_button('Add')
            self.bo_write_data('Customer code', customer_code)
            if position:
                self.bo_write_text_data('Position', position)
            self.click_button('Apply')
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
            self.bo_click_tab('General Information')
            master_customer_out=self.bo_get_value('Master customer')
            print(f'Master customer: {master_customer_out}')
            return master_customer_out

    def customer_relation_management_delete(self, master_customer=None, list_error_message=None):
        # search
        self.customer_relation_management_simple_search(str(master_customer).replace('-', ''))
        self.assert_table_data('Mater customer code', 1, self.customer_code_mask(master_customer))
        # delete
        self.click_table_menu('Delete', 1)
        self.wait_loading()
        self.click_button_in_popup('Yes')
        if list_error_message:
        # verify error
            self.assert_error_message()
            self.assert_list_error_message(list_error_message)
            print(f"Action delete '{master_customer}' failed!")
        else:
        # verify success
            self.check_notification('Deleted successfully')
            self.wait_loading()
            self.customer_relation_management_simple_search(str(master_customer).replace('-', ''))
            self.assert_search_not_found()
            print(f'Deleted: {master_customer}')
            return master_customer

    # CTM-Approve Customer relation management Modify
    def customer_approve_relation_management_modify_simple_search(self, text):
        self.close_all_form()
        self.click_menu('Customer', 'Approve Modify Customer Group')
        self.wait_for_button_available('Search')
        self.assert_form_title('CTM-Approve Customer relation management Modify-Search')
        self.simple_search(text=text, placeholder='Search Text')
        self.wait_loading()

    def customer_approve_relation_management_modify_advanced_search(self, master_customer_code=None, full_name=None, group_status=None):
        self.close_all_form()
        self.click_menu('Customer', 'Approve Modify Customer Group')
        self.wait_for_button_available('Search')
        self.assert_form_title('CTM-Approve Customer relation management Modify-Search')
        if master_customer_code:
            self.adv_search_text('Master customer code', master_customer_code)
        if full_name:
            self.adv_search_text('Full name', full_name)
        self.key_escape()
        if group_status:
            self.adv_search_select('Group status', group_status)
        self.click_button_search_advanced()
        self.wait_loading()

    def customer_approve_relation_management_modify_view(self, master_customer=None, full_name=None, group_status=None, group_status_modification=None, group_limit_code=None, credit_line=None, credit_line_modify=None, curency=None, curency_copy=None, mm_limit=None, mm_limit_modify=None, currency_mm=None, currency_mm_modify=None, fx_limit=None, fx_limit_modify=None, currency_fx=None, currency_fx_modify=None):
        # search
        self.customer_approve_relation_management_modify_simple_search(str(master_customer).replace('-', ''))
        self.assert_table_data('Mater customer code', 1, self.customer_code_mask(master_customer))
        # view
        self.click_table_menu(row=1)
        self.wait_for_button_available('View Modification')
        self.assert_form_title('CTM-Approve Customer relation management Modify-View')
        # verify value
        self.bo_click_tab('General Information')
        if master_customer:
            self.bo_assert_value('Master customer', self.customer_code_mask(master_customer))
        if full_name:
            self.bo_assert_text('Full name', full_name)
        if group_status:
            self.bo_assert_select('Group status', group_status)
        if group_status_modification:
            self.bo_assert_select('group_status_modification', group_status_modification)
        self.bo_click_tab('Credit Line Information')
        if group_limit_code:
            self.bo_assert_value_group('Group limit code', group_limit_code)
        if credit_line:
            self.bo_assert_value_group('Credit Line', credit_line)
        if credit_line_modify:
            self.bo_assert_value_group('credit_line_modify', credit_line_modify)
        if curency:
            self.bo_assert_select_group('Curency', curency)
        if curency_copy:
            self.bo_assert_select_group('Curency Copy', curency_copy)
        if mm_limit:
            self.bo_assert_value_group('MM Limit ', mm_limit)
        if mm_limit_modify:
            self.bo_assert_value_group('MM Limit Modify', mm_limit_modify)
        if currency_mm:
            self.bo_assert_select_group('Currency MM', currency_mm)
        if currency_mm_modify:
            self.bo_assert_select_group('Currency MM ', currency_mm_modify)
        if fx_limit:
            self.bo_assert_value_group('FX Limit', fx_limit)
        if fx_limit_modify:
            self.bo_assert_value_group('FX Limit Modify', fx_limit_modify)
        if currency_fx:
            self.bo_assert_select_group('Currency FX', currency_fx)
        if currency_fx_modify:
            self.bo_assert_select_group('Currency FX', currency_fx_modify)

    def customer_approve_relation_management_modify_approve(self, master_customer):
        self.customer_approve_relation_management_modify_view(master_customer=master_customer)
        self.click_button('View Modification')
        self.wait_loading()
        self.click_button('Approve')
        self.wait_loading()
        self.check_notification('Approve successfully')
        # back to tab 'General Information'
        self.bo_click_tab('General Information')
        master_customer = self.bo_get_value('Master customer')
        print('Master customer: ' + master_customer)
        self.customer_approve_relation_management_modify_simple_search(str(master_customer).replace('-', ''))
        self.assert_search_not_found()
        return master_customer

    def customer_approve_relation_management_modify_reject(self, master_customer):
        self.customer_approve_relation_management_modify_view(master_customer=master_customer)
        self.click_button('View Modification')
        self.wait_loading()
        self.click_button('Reject')
        self.wait_loading()
        self.check_notification('Reject successfully')
        # back to tab 'General Information'
        self.bo_click_tab('General Information')
        master_customer = self.bo_get_value('Master customer')
        print('Master customer: ' + master_customer)
        self.customer_approve_relation_management_modify_simple_search(str(master_customer).replace('-', ''))
        self.assert_search_not_found()
        return master_customer

    # CTM-Customer Media Files
    def customer_media_files_simple_search(self, text):
        self.close_all_form()
        self.click_menu('Customer', 'Customer Media Files')
        self.wait_for_button_available('Search')
        self.assert_form_title('CTM-Customer media files-Search')
        self.simple_search(text=text, placeholder='Search text')
        self.wait_loading()

    def customer_media_files_advanced_search(self, customer_code=None, account_number=None, business_line=None, customer_name=None, media_name=None, status=None, open_date_from=None, open_date_to=None, last_date_from=None, last_date_to=None, expire_date_from=None, expire_date_to=None):
        self.close_all_form()
        self.click_menu('Customer', 'Customer Media Files')
        self.wait_for_button_available('Search')
        self.assert_form_title('CTM-Customer media files-Search')
        if customer_code:
            self.adv_search('Customer code', str(customer_code).replace('-', ''))
        if account_number:
            self.adv_search('Account number', str(account_number).replace('-', ''))
        self.key_escape()
        if business_line:
            self.adv_search_select('Business line', business_line)
        if customer_name:
            self.adv_search_text('Customer name', customer_name)
        if media_name:
            self.adv_search_text('Media name', media_name)
        self.key_escape()
        if status:
            self.adv_search_select('Status', status)
        if open_date_from:
            self.adv_search_group('Open date from', open_date_from)
        if open_date_to:
            self.adv_search_group('Open date to', open_date_to)
        if last_date_from:
            self.adv_search_group('Last date from', last_date_from)
        if last_date_to:
            self.adv_search_group('Last date to', last_date_to)
        if expire_date_from:
            self.adv_search_group('Expire date from', expire_date_from)
        if expire_date_to:
            self.adv_search_group('Expire date to', expire_date_to)
        self.click_button_search_advanced()
        self.wait_loading()

    def customer_media_files_add(self, file_path=None, customer_code=None, business_line=None, customer_name=None, expire_date=None, account_number=None, list_error_message=None):
        # open form
        self.close_all_form()
        self.click_menu('Customer', 'Customer Media Files')
        self.wait_for_button_available('Add')
        self.click_button('Add')
        self.wait_for_button_available('Save')
        self.assert_form_title('CTM-Customer media files-Add')
        # choose file
        if file_path:
            self.bo_choose_file(file_path)
        # enter value
        if customer_code:
            self.bo_write_single('Customer code', self.no_mask(customer_code))
            self.wait_loading()
        if expire_date:
            self.bo_write_date_single('Expire Date', expire_date)
        if account_number:
            self.bo_write_single('Account number', self.no_mask(account_number))
            self.wait_loading()
        # assert value
        if business_line:
            self.bo_assert_select_single('Business line', business_line)
        if customer_name:
            self.bo_assert_text_single('Customer name', customer_name)
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
            self.check_notification('Save successfully')
            customer_code_out=self.bo_get_value_single('Customer code')
            print(f'Customer code: {customer_code_out}')
            return customer_code_out

    def customer_media_files_add_lookup(self, file_path=None, customer_code=None, business_line=None, customer_name=None, expire_date=None, account_number=None, list_error_message=None):
        # open form
        self.close_all_form()
        self.click_menu('Customer', 'Customer Media Files')
        self.wait_for_button_available('Add')
        self.click_button('Add')
        self.wait_for_button_available('Save')
        self.assert_form_title('CTM-Customer media files-Add')
        # choose file
        if file_path:
            self.bo_choose_file(file_path)
        # enter value
        if customer_code:
            customer_code_value = self.no_mask(customer_code)
            self.lookup_data_text(
                title='Customer code',
                value_search_code=customer_code_value,
                value_code=customer_code_value,
            )
            self.wait_loading()
        if expire_date:
            self.bo_write_date_single('Expire Date', expire_date)
        if account_number:
            self.bo_write_single('Account number', self.no_mask(account_number))
            self.wait_loading()
        # assert value
        if business_line:
            self.bo_assert_select_single('Business line', business_line)
        if customer_name:
            self.bo_assert_text_single('Customer name', customer_name)
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
            self.check_notification('Save successfully')
            customer_code_out=self.bo_get_value_single('Customer code')
            print(f'Customer code: {customer_code_out}')
            return customer_code_out

    def customer_media_files_view(self, customer_code=None, business_line=None, customer_name=None, expire_date=None, account_number=None):
        # search
        self.customer_media_files_simple_search(self.no_mask(customer_code))
        self.assert_table_data('Customer code', 1, self.customer_code_mask(customer_code))
        # view
        self.click_table_menu('View', 1)
        self.wait_for_button_available('Modify')
        self.assert_form_title('CTM-Customer media files-View')
        # verify value
        if customer_code:
            self.bo_assert_value_single('Customer code', self.customer_code_mask(customer_code))
        if business_line:
            self.bo_assert_select_single('Business line', business_line)
        if customer_name:
            self.bo_assert_text_single('Customer name', customer_name)
        if expire_date:
            self.bo_assert_date_single('Expire Date', expire_date)
        if account_number:
            self.bo_assert_value_single('Account nunber', self.deposit_account_number_mask(account_number))

    def customer_media_files_update(self, customer_code=None, business_line=None, customer_name=None, expire_date=None, account_number=None, list_error_message=None):
        # view
        self.customer_media_files_view(customer_code=customer_code)
        self.click_button('Modify')
        self.wait_loading()
        # update value
        if expire_date:
            self.bo_write_date_single('Expire Date', expire_date)
        if account_number:
            self.bo_write_single('Account nunber', self.no_mask(account_number))
        # assert value
        if customer_code:
            self.bo_assert_value_single('Customer code', self.customer_code_mask(customer_code))
        if business_line:
            self.bo_assert_select_single('Business line', business_line)
        if customer_name:
            self.bo_assert_text_single('Customer name', customer_name)
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
            self.check_notification('Save successfully')
            customer_code_out=self.bo_get_value_single('Customer code')
            print(f'Customer code: {customer_code_out}')
            return customer_code_out

    def customer_media_files_approve(self, customer_code, list_error_message=None):
        # view
        self.customer_media_files_view(customer_code=customer_code)
        # click 'Approve'
        self.click_button('Approve')
        if list_error_message:
        # verify error
            self.assert_error_message()
            self.assert_list_error_message(list_error_message)
            print('Action approve failed!')
        else:
        # verify success
            self.assert_button_disable('Approve')
            self.check_notification('Approve successfully')
            customer_code_out=self.bo_get_value_single('Customer code')
            print(f'Customer code: {customer_code_out}')
            media_name_out=self.bo_get_file_name()
            print(f'Media name: {media_name_out}')
            self.customer_media_files_advanced_search(
                customer_code=str(customer_code_out).replace('-', ''),
                media_name=media_name_out,
            )
            self.assert_table_data('Customer code', 1, self.customer_code_mask(customer_code_out))
            self.assert_table_data('Media name', 1, media_name_out)
            self.assert_table_data('Status', 1, 'Approved')
            return customer_code_out

    def customer_media_files_get_information(self, customer_code=None, customer_name=None, dob=None, identification=None):
        # view
        self.customer_media_files_view(customer_code=customer_code)
        # click 'Get information'
        self.click_button('Get information')
        # verify
        self.assert_form_title_header_popup('Signature View')
        self.bo_assert_info_signature('Customer code', self.no_mask(customer_code))
        if dob:
            self.bo_assert_info_signature('DOB', dob)
        if identification:
            self.bo_assert_info_signature('Identification', identification)
        if customer_name:
            self.bo_assert_info_signature('Customer name', customer_name)
        self.close_popup()

    def customer_media_files_delete(self, customer_code=None, media_name=None, list_error_message=None):
        # search
        self.customer_media_files_advanced_search(
            customer_code=self.no_mask(customer_code),
            media_name=media_name,
        )
        self.assert_table_data('Customer code', 1, self.customer_code_mask(customer_code))
        if media_name:
            self.assert_table_data('Media name', 1, media_name)
        # delete
        self.click_table_menu('Delete', 1)
        self.wait_loading()
        self.click_button_in_popup('Yes')
        if list_error_message:
        # verify error
            self.assert_error_message()
            self.assert_list_error_message(list_error_message)
            print(f"Action delete '{customer_code}' and '{media_name}' failed!")
        else:
        # verify success
            self.check_notification('Deleted successfully')
            self.wait_loading()
            self.customer_media_files_advanced_search(
                customer_code=self.no_mask(customer_code),
                media_name=media_name,
            )
            self.assert_search_not_found()
            print(f"Deleted: '{customer_code}' and '{media_name}'")
            return customer_code

