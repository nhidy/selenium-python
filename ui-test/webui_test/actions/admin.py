from webui_test.case import *

class AdminActions(TestCase):

# -------------------------- handle BO - ADMINISTRATION --------------------------
    # ADM-User Profile
    def user_profile_simple_search(self, text):
        self.close_all_form()
        self.click_menu('Administration', 'Bank Administration', 'User Profile')
        self.wait_for_button_available('Search')
        self.assert_form_title('ADM-User Profile-Search')
        self.simple_search(text=text, placeholder='Search Text')
        self.wait_loading()

    def user_profile_advanced_search(self, user_code=None, user_name=None, login_name=None, branch_name=None, department_name=None, status=None, is_online=None, email=None):
        self.close_all_form()
        self.click_menu('Administration', 'Bank Administration', 'User Profile')
        self.wait_for_button_available('Search')
        self.assert_form_title('ADM-User Profile-Search')
        if user_code:
            self.adv_search_text('User code', user_code)
        if user_name:
            self.adv_search_text('User name', user_name)
        if login_name:
            self.adv_search_text('Login name', login_name)
        if branch_name:
            self.adv_search_text('Branch name', branch_name)
        if department_name:
            self.adv_search_text('Department name', department_name)
        self.key_escape()
        if status:
            self.adv_search_select('Status', status)
        self.key_escape()
        if is_online:
            self.adv_search_select('Is online', is_online)
        if email:
            self.adv_search_text('Email', email)
        self.click_button_search_advanced()
        self.wait_loading()

    def user_profile_add(self, user_code=None, old_user_id=None, user_name=None, login_name=None, branch_code=None, department_name=None, cashier=None, officer=None, chief_cashier=None, operation_staff=None, dealer=None, inter_branch_user=None, branch_manager_authorized=None, hr=None, email=None, remark=None, status_of_this_record=None, password=None, main_language=None, user_phone=None, home=None, office=None, cell=None, facsimile=None, telex=None, time_zone_of_user=None, thousand_separate_character_in_amount_field=None, decimal_separate_character_in_amount_field=None, date_format_for_short=None, long_date_format=None, time_format=None, expire_date_of_this_user=None, id_of_policy_apply_for_this_user=None, list_error_message=None):
        # open form
        self.close_all_form()
        self.click_menu('Administration', 'Bank Administration', 'User Profile')
        self.wait_for_button_available('Add')
        self.click_button('Add')
        self.wait_for_button_available('Save')
        self.assert_form_title('ADM-User Profile-Add')
        # enter value
        self.bo_click_tab('General Information')
        if old_user_id:
            self.bo_write_text('Old User ID', old_user_id)
        if user_name:
            self.bo_write_text('User Name', user_name)
        if login_name:
            self.bo_write_text('Login Name', login_name)
        self.key_escape()
        if branch_code:
            self.bo_select('Branch Code', branch_code)
        self.key_escape()
        if department_name:
            self.bo_select('Department Name', department_name)
        self.bo_click_collap('Position')
        if cashier is True:
            self.bo_click_checkbox_multi('Position', 'Cashier')
        if officer is True:
            self.bo_click_checkbox_multi('Position', 'Officer')
        if chief_cashier is True:
            self.bo_click_checkbox_multi('Position', 'Chief Cashier')
        if operation_staff is True:
            self.bo_click_checkbox_multi('Position', 'Operation Staff')
        if dealer is True:
            self.bo_click_checkbox_multi('Position', 'Dealer')
        if inter_branch_user is True:
            self.bo_click_checkbox_multi('Position', 'Inter-branch user')
        if branch_manager_authorized is True:
            self.bo_click_checkbox_multi('Position', 'Branch Manager/Authorized')
        if hr is True:
            self.bo_click_checkbox_multi('Position', 'HR')
        if cashier is False:
            self.bo_click_uncheckbox_multi('Position', 'Cashier')
        if officer is False:
            self.bo_click_uncheckbox_multi('Position', 'Officer')
        if chief_cashier is False:
            self.bo_click_uncheckbox_multi('Position', 'Chief Cashier')
        if operation_staff is False:
            self.bo_click_uncheckbox_multi('Position', 'Operation Staff')
        if dealer is False:
            self.bo_click_uncheckbox_multi('Position', 'Dealer')
        if inter_branch_user is False:
            self.bo_click_uncheckbox_multi('Position', 'Inter-branch user')
        if branch_manager_authorized is False:
            self.bo_click_uncheckbox_multi('Position', 'Branch Manager/Authorized')
        if hr is False:
            self.bo_click_uncheckbox_multi('Position', 'HR')
        if email:
            self.bo_write('Email', email)
        if remark:
            self.bo_write_text('Remark', remark)
        self.key_escape()
        if status_of_this_record:
            self.bo_select('Status Of This Record', status_of_this_record)
        self.bo_click_tab('Other Information')
        self.key_escape()
        if main_language:
            self.bo_select('Main Language', main_language)
        if user_phone:
            self.bo_write_text('User Phone', user_phone)
        if home:
            self.bo_click_collap('Phone Number')
            self.bo_write_text_multi('Phone Number', 'Home', home)
        if office:
            self.bo_click_collap('Phone Number')
            self.bo_write_text_multi('Phone Number', 'Office', office)
        if cell:
            self.bo_click_collap('Phone Number')
            self.bo_write_text_multi('Phone Number', 'Cell', cell)
        if facsimile:
            self.bo_click_collap('Phone Number')
            self.bo_write_text_multi('Phone Number', 'Facsimile', facsimile)
        if telex:
            self.bo_click_collap('Phone Number')
            self.bo_write_text_multi('Phone Number', 'Telex', telex)
        self.key_escape()
        if time_zone_of_user:
            self.bo_select('Time Zone Of User', time_zone_of_user)
        self.key_escape()
        if thousand_separate_character_in_amount_field:
            self.bo_select('Thousand Separate Character In Amount Field', thousand_separate_character_in_amount_field)
        self.key_escape()
        if decimal_separate_character_in_amount_field:
            self.bo_select('Decimal Separate Character In Amount Field', decimal_separate_character_in_amount_field)
        self.key_escape()
        if date_format_for_short:
            self.bo_select('Date Format For Short', date_format_for_short)
        self.key_escape()
        if long_date_format:
            self.bo_select('Long Date Format', long_date_format)
        self.key_escape()
        if time_format:
            self.bo_select('Time Format', time_format)
        if expire_date_of_this_user:
            self.bo_write_date('Expire Date Of This User', expire_date_of_this_user)
        self.key_escape()
        if id_of_policy_apply_for_this_user:
            self.bo_select('ID Of Policy Apply For This User', id_of_policy_apply_for_this_user)
        # assert value
        self.bo_click_tab('General Information')
        if user_code:
            self.bo_assert_text('User Code', user_code)
        if password:
            self.bo_assert_text('Password', password)
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
            self.bo_click_tab('General Information')
            user_code_out=self.bo_get_text('User Code')
            print(f'User Code: {user_code_out}')
            password_out=self.bo_get_text('Password')
            print(f'Password: {password_out}')
            return user_code_out, password_out

    def user_profile_view(self, user_code=None, old_user_id=None, user_name=None, login_name=None, branch_code=None, department_name=None, cashier=None, officer=None, chief_cashier=None, operation_staff=None, dealer=None, inter_branch_user=None, branch_manager_authorized=None, hr=None, email=None, remark=None, status_of_this_record=None, password=None, main_language=None, user_phone=None, home=None, office=None, cell=None, facsimile=None, telex=None, time_zone_of_user=None, thousand_separate_character_in_amount_field=None, decimal_separate_character_in_amount_field=None, date_format_for_short=None, long_date_format=None, time_format=None, expire_date_of_this_user=None, id_of_policy_apply_for_this_user=None):
        # search
        self.user_profile_simple_search(user_code)
        self.assert_table_data('User Code', 1, user_code)
        # view
        self.click_table_menu('View', 1)
        self.wait_for_button_available('Modify')
        self.assert_form_title('ADM-User Profile-View')
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
        if home:
            self.bo_click_collap('Phone Number')
            self.bo_assert_text_multi('Phone Number', 'Home', home)
        if office:
            self.bo_click_collap('Phone Number')
            self.bo_assert_text_multi('Phone Number', 'Office', office)
        if cell:
            self.bo_click_collap('Phone Number')
            self.bo_assert_text_multi('Phone Number', 'Cell', cell)
        if facsimile:
            self.bo_click_collap('Phone Number')
            self.bo_assert_text_multi('Phone Number', 'Facsimile', facsimile)
        if telex:
            self.bo_click_collap('Phone Number')
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

    def user_profile_update(self, user_code=None, old_user_id=None, user_name=None, login_name=None, branch_code=None, department_name=None, cashier=None, officer=None, chief_cashier=None, operation_staff=None, dealer=None, inter_branch_user=None, branch_manager_authorized=None, hr=None, email=None, remark=None, status_of_this_record=None, password=None, main_language=None, user_phone=None, home=None, office=None, cell=None, facsimile=None, telex=None, time_zone_of_user=None, thousand_separate_character_in_amount_field=None, decimal_separate_character_in_amount_field=None, date_format_for_short=None, long_date_format=None, time_format=None, expire_date_of_this_user=None, id_of_policy_apply_for_this_user=None, list_error_message=None):
        # view
        self.user_profile_view(user_code=user_code)
        self.click_button('Modify')
        self.wait_loading()
        # update value
        self.bo_click_tab('General Information')
        if old_user_id:
            self.bo_write_text('Old User ID', old_user_id)
        if user_name:
            self.bo_write_text('User Name', user_name)
        self.key_escape()
        if branch_code:
            self.bo_select('Branch Code', branch_code)
        self.key_escape()
        if department_name:
            self.bo_select('Department Name', department_name)
        self.bo_click_collap('Position')
        if cashier is True:
            self.bo_click_checkbox_multi('Position', 'Cashier')
        if officer is True:
            self.bo_click_checkbox_multi('Position', 'Officer')
        if chief_cashier is True:
            self.bo_click_checkbox_multi('Position', 'Chief Cashier')
        if operation_staff is True:
            self.bo_click_checkbox_multi('Position', 'Operation Staff')
        if dealer is True:
            self.bo_click_checkbox_multi('Position', 'Dealer')
        if inter_branch_user is True:
            self.bo_click_checkbox_multi('Position', 'Inter-branch user')
        if branch_manager_authorized is True:
            self.bo_click_checkbox_multi('Position', 'Branch Manager/Authorized')
        if hr is True:
            self.bo_click_checkbox_multi('Position', 'HR')
        if cashier is False:
            self.bo_click_uncheckbox_multi('Position', 'Cashier')
        if officer is False:
            self.bo_click_uncheckbox_multi('Position', 'Officer')
        if chief_cashier is False:
            self.bo_click_uncheckbox_multi('Position', 'Chief Cashier')
        if operation_staff is False:
            self.bo_click_uncheckbox_multi('Position', 'Operation Staff')
        if dealer is False:
            self.bo_click_uncheckbox_multi('Position', 'Dealer')
        if inter_branch_user is False:
            self.bo_click_uncheckbox_multi('Position', 'Inter-branch user')
        if branch_manager_authorized is False:
            self.bo_click_uncheckbox_multi('Position', 'Branch Manager/Authorized')
        if hr is False:
            self.bo_click_uncheckbox_multi('Position', 'HR')
        if email:
            self.bo_write('Email', email)
        if remark:
            self.bo_write_text('Remark', remark)
        self.key_escape()
        if status_of_this_record:
            self.bo_select('Status Of This Record', status_of_this_record)
        self.bo_click_tab('Other Information')
        self.key_escape()
        if main_language:
            self.bo_select('Main Language', main_language)
        if user_phone:
            self.bo_write_text('User Phone', user_phone)
        if home:
            self.bo_click_collap('Phone Number')
            self.bo_write_text_multi('Phone Number', 'Home', home)
        if office:
            self.bo_click_collap('Phone Number')
            self.bo_write_text_multi('Phone Number', 'Office', office)
        if cell:
            self.bo_click_collap('Phone Number')
            self.bo_write_text_multi('Phone Number', 'Cell', cell)
        if facsimile:
            self.bo_click_collap('Phone Number')
            self.bo_write_text_multi('Phone Number', 'Facsimile', facsimile)
        if telex:
            self.bo_click_collap('Phone Number')
            self.bo_write_text_multi('Phone Number', 'Telex', telex)
        self.key_escape()
        if time_zone_of_user:
            self.bo_select('Time Zone Of User', time_zone_of_user)
        self.key_escape()
        if thousand_separate_character_in_amount_field:
            self.bo_select('Thousand Separate Character In Amount Field', thousand_separate_character_in_amount_field)
        self.key_escape()
        if decimal_separate_character_in_amount_field:
            self.bo_select('Decimal Separate Character In Amount Field', decimal_separate_character_in_amount_field)
        self.key_escape()
        if date_format_for_short:
            self.bo_select('Date Format For Short', date_format_for_short)
        self.key_escape()
        if long_date_format:
            self.bo_select('Long Date Format', long_date_format)
        self.key_escape()
        if time_format:
            self.bo_select('Time Format', time_format)
        if expire_date_of_this_user:
            self.bo_write_date('Expire Date Of This User', expire_date_of_this_user)
        self.key_escape()
        if id_of_policy_apply_for_this_user:
            self.bo_select('ID Of Policy Apply For This User', id_of_policy_apply_for_this_user)
        # assert value
        self.bo_click_tab('General Information')
        if user_code:
            self.bo_assert_text('User Code', user_code)
        if login_name:
            self.bo_assert_text('Login Name', login_name)
        if password:
            self.bo_assert_text('Password', password)
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
            user_code_out=self.bo_get_text('User Code')
            print(f'User Code: {user_code_out}')
            return user_code_out

    def user_profile_delete(self, user_code, list_error_message=None, expected_message=None):
        # search
        self.user_profile_simple_search(user_code)
        self.assert_table_data('User Code', 1, user_code)
        # delete
        self.click_table_menu('Delete', 1)
        self.wait_loading()
        self.click_button_in_popup('Yes')
        if list_error_message:
        # verify error
            self.assert_error_message()
            self.assert_list_error_message(list_error_message)
            print(f"Action delete '{user_code}' failed!")
        else:
        # verify success
            if expected_message:
                self.assert_notification(expected_message)
            print(f"Deleted: '{user_code}'")
            return user_code

    def user_profile_logout(self, user_code, list_error_message=None):
        # search
        self.user_profile_simple_search(user_code)
        self.assert_table_data('User Code', 1, user_code)
        # logout
        self.click_table_menu('Log out', 1)
        self.wait_loading()
        self.click_button_in_popup('Yes')
        if list_error_message:
        # verify error
            self.assert_error_message()
            self.assert_list_error_message(list_error_message)
            print(f"Action logout '{user_code}' failed!")
        else:
        # verify success
            self.check_notification('#Logout all successfully')
            self.wait_loading()
            self.user_profile_simple_search(user_code)
            self.assert_search_not_found()
            print(f'Logout: {user_code}')
            return user_code

    def user_profile_reset_password(self, user_code=None):
        # view
        self.user_profile_view(user_code=user_code)
        # reset password
        self.click_button('Reset password')
        self.wait_loading()
        self.check_notification('#Reset password successfully')
        # get value
        self.bo_click_tab('General Information')
        user_code_out=self.bo_get_text('User Code')
        print(f'User Code: {user_code_out}')
        password_out=self.bo_get_text('Password')
        print(f'Password: {password_out}')
        return user_code_out, password_out

    def user_profile_change_password(self, username, reset_password, new_password, one_app='N'):
        self.logout()
        self.wait_page_login()
        self.login(username, reset_password, one_app=one_app)
        self.wait_loading()
        try:
            password_input = self.wait_for_element_visibility_by_css("input[placeholder='Password']")
            confirm_password_input = self.wait_for_element_visibility_by_css("input[placeholder='Confirm Password']")
            password_input.send_keys(new_password)
            password_input.send_keys(Keys.TAB)
            confirm_password_input.send_keys(new_password)
            confirm_password_input.send_keys(Keys.ENTER)
            self.wait_page_login()
            self.login(username, new_password, one_app=one_app)
        except (NoSuchElementException, ElementNotInteractableException) as e:
            log.error(f"Change password screen failed. Exception: {e}")

    def check_user_profile_not_exist(self, login_name):
        # search login_name
        self.user_profile_advanced_search(login_name=login_name)
        if (self.get_text_notification(timeout=3) == 'Data not found'):
            print(f"Login name '{login_name}' does NOT exist.")
            return True
        else:
            print(f"Login name '{login_name}' already exists.")
            return False

    def login_admin(self, username, password):
        self.logout()
        self.wait_page_login()
        self.login(username=username, password=password, one_app='N', app_name="Neptune Admin")
        self.wait_loading()

    def set_role_for_user(self, username, app_name, tab_name, role_name):
        self.close_all_form()
        self.click_menu('Role Profiles')
        self.wait_loading()
        self.assert_form_title('ADM-Roles Profile')
        self.bo_click_tab(app_name)
        self.wait_loading()
        self.bo_click_tab_child(tab_name)
        self.wait_loading()
        self.select_in_tab_child(role_name)
        self.wait_loading()

    def check_bank_closed(self):
        self.close_all_form()
        self.click_menu('Administration', 'Bank Administration', 'Bank Open/close')
        if self.button_exists('Close Bank'):
            print(f"The bank is open.")
            return False
        else:
            print(f"The bank is closed.")
            return True

    def check_branch_closed(self, branch_code):
        self.close_all_form()
        self.click_menu('Administration', 'Bank Administration', 'Bank Open/close')
        self.wait_for_button_available('Refresh')
        self.click_button('Refresh')
        self.choose_page()
        self.wait_loading()
        if self.is_online(branch_code):
            print(f"The branch {branch_code} is open.")
            return False
        else:
            print(f"The branch {branch_code} is closed.")
            return True

    # ADM-Branch Profile
    def branch_profile_simple_search(self, text):
        self.close_all_form()
        self.click_menu('Administration', 'Bank Administration', 'Branch Profile')
        self.wait_for_button_available('Search')
        self.assert_form_title('ADM-Branch Profile-Search')
        self.simple_search(text=text, placeholder='Search text')
        self.wait_loading()

    def branch_profile_advanced_search(self, branch_code=None, branch_name=None, address=None, base_currency_code=None, online_status=None):
        self.close_all_form()
        self.click_menu('Administration', 'Bank Administration', 'Branch Profile')
        self.wait_for_button_available('Search')
        self.assert_form_title('ADM-Branch Profile-Search')
        if branch_code:
            self.adv_search_text('Branch code', branch_code)
        if branch_name:
            self.adv_search_text('Branch name', branch_name)
        if address:
            self.adv_search_text('Address', address)
        if base_currency_code:
            self.adv_search_text('Base currency code', base_currency_code)
        self.key_escape()
        if online_status:
            self.adv_search_select('Online status', online_status)
        self.click_button_search_advanced()
        self.wait_loading()

    def branch_profile_add(self, branch_code=None, old_branch_id=None, branch_name=None, branch_address=None, branch_type=None, branch_phone=None, home=None, office=None, cell=None, facsimile=None, telex=None, tax_code=None, base_currency_code=None, local_currency_code=None, region=None, bic=None, domestic_bank_code=None, internal_code=None, country=None, main_language=None, time_zone_of_branch=None, thousand_separate_character=None, decimal_separate_character=None, date_format_for_short=None, long_date_format=None, time_format=None, online=None, list_error_message=None):
        # open form
        self.close_all_form()
        self.click_menu('Administration', 'Bank Administration', 'Branch Profile')
        self.wait_for_button_available('Add')
        self.click_button('Add')
        self.wait_for_button_available('Save')
        self.assert_form_title('ADM-Branch Profile-Add')
        # enter value
        self.bo_click_tab('General information')
        if branch_code:
            self.bo_write('Branch code', branch_code)
        if old_branch_id:
            self.bo_write_text('Old branch ID', old_branch_id)
        if branch_name:
            self.bo_write_text('Branch name', branch_name)
        if branch_address:
            self.bo_write_text('Branch address', branch_address)
        self.key_escape()
        if branch_type:
            self.bo_select('Branch type', branch_type)
        if branch_phone:
            self.bo_write_text('Branch phone', branch_phone)
        self.bo_click_collap('Phone number')
        if home:
            self.bo_write_text_multi('Phone number', 'Home', home)
        if office:
            self.bo_write_text_multi('Phone number', 'Office', office)
        if cell:
            self.bo_write_text_multi('Phone number', 'Cell', cell)
        if facsimile:
            self.bo_write_text_multi('Phone number', 'Facsimile', facsimile)
        if telex:
            self.bo_write_text_multi('Phone number', 'Telex', telex)
        if tax_code:
            self.bo_write_text('Tax code', tax_code)
        self.key_escape()
        if base_currency_code:
            self.bo_select('Base currency code', base_currency_code)
        self.key_escape()
        if local_currency_code:
            self.bo_select('Local currency code', local_currency_code)
        self.key_escape()
        if region:
            self.bo_select('Region', region)
        self.bo_click_collap('Reference code')
        if bic:
            self.bo_write_text_multi('Reference code', 'Bic', bic)
        if domestic_bank_code:
            self.bo_write_text_multi('Reference code', 'Domestic bank code', domestic_bank_code)
        if internal_code:
            self.bo_write_text_multi('Reference code', 'Internal code', internal_code)
        self.key_escape()
        if country:
            self.bo_select('Country', country)
        self.key_escape()
        if main_language:
            self.bo_select('Main language', main_language)
        self.key_escape()
        if time_zone_of_branch:
            self.bo_select('Time zone of branch', time_zone_of_branch)
        self.key_escape()
        if thousand_separate_character:
            self.bo_select('Thousand separate character', thousand_separate_character)
        self.key_escape()
        if decimal_separate_character:
            self.bo_select('Decimal separate character', decimal_separate_character)
        self.key_escape()
        if date_format_for_short:
            self.bo_select('Date format for short', date_format_for_short)
        self.key_escape()
        if long_date_format:
            self.bo_select('Long date format', long_date_format)
        self.key_escape()
        if time_format:
            self.bo_select('Time format', time_format)
        self.key_escape()
        if online:
            self.bo_select('Online', online)
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
            self.assert_notification('Saved successfully!')
            self.bo_click_tab('General information')
            branch_code_out=self.bo_get_value('Branch code')
            print(f'Branch code: {branch_code_out}')
            return branch_code_out

    def branch_profile_view(self, branch_code=None, old_branch_id=None, branch_name=None, branch_address=None, branch_phone=None, branch_type=None, home=None, office=None, cell=None, facsimile=None, telex=None, tax_code=None, base_currency_code=None, local_currency_code=None, region=None, bic=None, domestic_bank_code=None, internal_code=None, country=None, main_language=None, time_zone_of_branch=None, thousand_separate_character=None, decimal_separate_character=None, date_format_for_short=None, long_date_format=None, time_format=None, online=None):
        # search
        self.branch_profile_simple_search(branch_code)
        self.assert_table_data('Branch code', 1, branch_code)
        # view
        self.click_table_menu('View', 1)
        self.wait_for_button_available('Modify')
        self.assert_form_title('ADM-Branch Profile-View')
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

    def branch_profile_update(self, branch_code=None, old_branch_id=None, branch_name=None, branch_address=None, branch_phone=None, branch_type=None, home=None, office=None, cell=None, facsimile=None, telex=None, tax_code=None, base_currency_code=None, local_currency_code=None, region=None, bic=None, domestic_bank_code=None, internal_code=None, country=None, main_language=None, time_zone_of_branch=None, thousand_separate_character=None, decimal_separate_character=None, date_format_for_short=None, long_date_format=None, time_format=None, online=None, list_error_message=None):
        # view
        self.branch_profile_view(branch_code=branch_code)
        self.click_button('Modify')
        self.wait_loading()
        # update value
        self.bo_click_tab('General information')
        if old_branch_id:
            self.bo_write_text('Old branch ID', old_branch_id)
        if branch_name:
            self.bo_write_text('Branch name', branch_name)
        if branch_address:
            self.bo_write_text('Branch address', branch_address)
        if branch_phone:
            self.bo_write_text('Branch phone', branch_phone)
        self.key_escape()
        if branch_type:
            self.bo_select('Branch type', branch_type)
        self.bo_click_collap('Phone number')
        if home:
            self.bo_write_text_multi('Phone number', 'Home', home)
        if office:
            self.bo_write_text_multi('Phone number', 'Office', office)
        if cell:
            self.bo_write_text_multi('Phone number', 'Cell', cell)
        if facsimile:
            self.bo_write_text_multi('Phone number', 'Facsimile', facsimile)
        if telex:
            self.bo_write_text_multi('Phone number', 'Telex', telex)
        if tax_code:
            self.bo_write_text('Tax code', tax_code)
        self.key_escape()
        if base_currency_code:
            self.bo_select('Base currency code', base_currency_code)
        self.key_escape()
        if local_currency_code:
            self.bo_select('Local currency code', local_currency_code)
        self.key_escape()
        if region:
            self.bo_select('Region', region)
        self.bo_click_collap('Reference code')
        if bic:
            self.bo_write_text_multi('Reference code', 'Bic', bic)
        if domestic_bank_code:
            self.bo_write_text_multi('Reference code', 'Domestic bank code', domestic_bank_code)
        if internal_code:
            self.bo_write_text_multi('Reference code', 'Internal code', internal_code)
        self.key_escape()
        if country:
            self.bo_select('Country', country)
        self.key_escape()
        if main_language:
            self.bo_select('Main language', main_language)
        self.key_escape()
        if time_zone_of_branch:
            self.bo_select('Time zone of branch', time_zone_of_branch)
        self.key_escape()
        if thousand_separate_character:
            self.bo_select('Thousand separate character', thousand_separate_character)
        self.key_escape()
        if decimal_separate_character:
            self.bo_select('Decimal separate character', decimal_separate_character)
        self.key_escape()
        if date_format_for_short:
            self.bo_select('Date format for short', date_format_for_short)
        self.key_escape()
        if long_date_format:
            self.bo_select('Long date format', long_date_format)
        self.key_escape()
        if time_format:
            self.bo_select('Time format', time_format)
        self.key_escape()
        if online:
            self.bo_select('Online', online)
        # assert value
        self.bo_click_tab('General information')
        if branch_code:
            self.bo_assert_text('Branch code', branch_code)
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
            self.assert_notification('Saved successfully!')
            self.bo_click_tab('General information')
            branch_code_out=self.bo_get_text('Branch code')
            print(f'Branch code: {branch_code_out}')
            return branch_code_out

    def branch_profile_delete(self, branch_code, list_error_message=None, expected_message=None):
        # search
        self.branch_profile_simple_search(branch_code)
        self.assert_table_data('Branch code', 1, branch_code)
        # delete
        self.click_table_menu('Delete', 1)
        self.wait_loading()
        self.click_button_in_popup('Yes')
        if list_error_message:
        # verify error
            self.assert_error_message()
            self.assert_list_error_message(list_error_message)
            print(f"Action delete '{branch_code}' failed!")
        else:
        # verify success
            if expected_message:
                self.assert_notification(expected_message)
            print(f"Deleted: '{branch_code}'")
            return branch_code

    # ADM-Department Profile
    def department_profile_simple_search(self, text):
        self.close_all_form()
        self.click_menu('Administration', 'Bank Administration', 'Department Profile')
        self.wait_for_button_available('Search')
        self.assert_form_title('ADM-Department Profile-Search')
        self.simple_search(text=text, placeholder='Search Text')
        self.wait_loading()

    def department_profile_advanced_search(self, department_code=None, department_name=None, branch_name=None):
        self.close_all_form()
        self.click_menu('Administration', 'Bank Administration', 'Department Profile')
        self.wait_for_button_available('Search')
        self.assert_form_title('ADM-Department Profile-Search')
        if department_code:
            self.adv_search_text('Department code', department_code)
        if department_name:
            self.adv_search_text('Department name', department_name)
        if branch_name:
            self.adv_search_text('Branch name', branch_name)
        self.click_button_search_advanced()
        self.wait_loading()

    def department_profile_add(self, department_code=None, department_name=None, branch_code=None, list_error_message=None):
        # open form
        self.close_all_form()
        self.click_menu('Administration', 'Bank Administration', 'Department Profile')
        self.wait_for_button_available('Add')
        self.click_button('Add')
        self.wait_for_button_available('Save')
        self.assert_form_title('ADM-Department Profile-Add')
        # enter value
        if department_code:
            self.bo_write_single('Department Code', department_code)
        if department_name:
            self.bo_write_text_single('Department Name', department_name)
        self.key_escape()
        if branch_code:
            self.bo_select_single('Branch Code', branch_code)
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
            self.assert_notification('Saved successfully!')
            department_code_out=self.bo_get_value_single('Department Code')
            print(f'Department Code: {department_code_out}')
            return department_code_out

    def department_profile_view(self, department_code=None, department_name=None, branch_code=None):
        # search
        self.department_profile_simple_search(department_code)
        self.assert_table_data('Department Code', 1, department_code)
        # view
        self.click_table_menu('View', 1)
        self.wait_for_button_available('Modify')
        self.assert_form_title('ADM-Department Profile-View')
        # verify value
        self.bo_click_tab('General')
        if department_code:
            self.bo_assert_text('Department Code', department_code)
        if department_name:
            self.bo_assert_text('Department Name', department_name)
        if branch_code:
            self.bo_assert_select('Branch Code', branch_code)

    def department_profile_update(self, department_code=None, department_name=None, branch_code=None, list_error_message=None):
        # view
        self.department_profile_view(department_code=department_code)
        self.click_button('Modify')
        self.wait_loading()
        # update value
        self.bo_click_tab('General')
        if department_name:
            self.bo_write_text('Department Name', department_name)
        self.key_escape()
        if branch_code:
            self.bo_select('Branch Code', branch_code)
        # assert value
        self.bo_click_tab('General')
        if department_code:
            self.bo_assert_text('Department Code', department_code)
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
            self.assert_notification('Saved successfully!')
            self.bo_click_tab('General')
            department_code_out=self.bo_get_text('Department Code')
            print(f'Department Code: {department_code_out}')
            return department_code_out

    def department_profile_delete(self, department_code, list_error_message=None, expected_message=None):
        # search
        self.department_profile_simple_search(department_code)
        self.assert_table_data('Department Code', 1, department_code)
        # delete
        self.click_table_menu('Delete', 1)
        self.wait_loading()
        self.click_button_in_popup('Yes')
        if list_error_message:
        # verify error
            self.assert_error_message()
            self.assert_list_error_message(list_error_message)
            print(f"Action delete '{department_code}' failed!")
        else:
        # verify success
            if expected_message:
                self.assert_notification(expected_message)
            print(f"Deleted: '{department_code}'")
            return department_code

    # ADM-Branch Linkage
    def branch_linkage_simple_search(self, text):
        self.close_all_form()
        self.click_menu('Administration', 'Bank Administration', 'Branch Linkage')
        self.wait_for_button_available('Search')
        self.assert_form_title('ADM-Branch Linkage-Search')
        self.simple_search(text=text, placeholder='Search text')
        self.wait_loading()

    def branch_linkage_advanced_search(self, master_branch_code=None, linkage_branch_code=None, linkage_type=None, description=None):
        self.close_all_form()
        self.click_menu('Administration', 'Bank Administration', 'Branch Linkage')
        self.wait_for_button_available('Search')
        self.assert_form_title('ADM-Branch Linkage-Search')
        if master_branch_code:
            self.adv_search_text('Master branch code', master_branch_code)
        if linkage_branch_code:
            self.adv_search_text('Linkage branch code', linkage_branch_code)
        self.key_escape()
        if linkage_type:
            self.adv_search_select('Linkage type', linkage_type)
        if description:
            self.adv_search_text('Description', description)
        self.click_button_search_advanced()
        self.wait_loading()

    def branch_linkage_add(self, master_branch=None, linkage_branch=None, linkage_type=None, description=None, list_error_message=None):
        # open form
        self.close_all_form()
        self.click_menu('Administration', 'Bank Administration', 'Branch Linkage')
        self.wait_for_button_available('Add')
        self.click_button('Add')
        self.wait_for_button_available('Save')
        self.assert_form_title('ADM-Branch Linkage-Add')
        # enter value
        self.key_escape()
        if master_branch:
            self.bo_select_single('Master branch', master_branch)
        self.key_escape()
        if linkage_branch:
            self.bo_select_single('Linkage branch', linkage_branch)
        self.key_escape()
        if linkage_type:
            self.select('Linkage type', linkage_type)
        if description:
            self.write_textarea('Description', description)
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
            self.assert_notification('Saved successfully!')
            master_branch_out=self.bo_get_select_single('Master branch')
            print(f"Master branch: '{master_branch_out}'")
            linkage_branch_out=self.bo_get_select_single('Linkage branch')
            print(f"Linkage branch: '{linkage_branch_out}'")
            return master_branch_out, linkage_branch_out

    def branch_linkage_view(self, master_branch=None, linkage_branch=None, linkage_type=None, description=None):
        # search
        self.branch_linkage_simple_search(description)
        self.assert_table_data('Linkage description', 1, description)
        # view
        self.click_table_menu('View', 1)
        self.wait_for_button_available('Modify')
        self.assert_form_title('ADM-Branch Linkage-View')
        # verify value
        if master_branch:
            self.bo_assert_select_single('Master branch', master_branch)
        if linkage_branch:
            self.bo_assert_select_single('Linkage branch', linkage_branch)
        if linkage_type:
            self.bo_assert_value_data('Linkage type', linkage_type)
        if description:
            self.bo_assert_text_single('Description', description)

    def branch_linkage_update(self, master_branch=None, linkage_branch=None, linkage_type=None, description_search=None, description_update=None, list_error_message=None):
        # view
        self.branch_linkage_view(description=description_search)
        self.click_button('Modify')
        self.wait_loading()
        # update value
        if description_update:
            self.write_textarea('Description', description_update)
        # assert value
        if master_branch:
            self.bo_assert_select_single('Master branch', master_branch)
        if linkage_branch:
            self.bo_assert_select_single('Linkage branch', linkage_branch)
        if linkage_type:
            self.bo_assert_select_single('Linkage type', linkage_type)
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
            self.assert_notification('Saved successfully!')
            master_branch_out=self.bo_get_select_single('Master branch')
            print(f"Master branch: '{master_branch_out}'")
            linkage_branch_out=self.bo_get_select_single('Linkage branch')
            print(f"Linkage branch: '{linkage_branch_out}'")
            return master_branch_out, linkage_branch_out

    def branch_linkage_delete(self, description, list_error_message=None, expected_message=None):
        # search
        self.branch_linkage_simple_search(description)
        self.assert_table_data('Linkage description', 1, description)
        # delete
        self.click_table_menu('Delete', 1)
        self.wait_loading()
        self.click_button_in_popup('Yes')
        if list_error_message:
        # verify error
            self.assert_error_message()
            self.assert_list_error_message(list_error_message)
            print(f"Action delete '{description}' failed!")
        else:
        # verify success
            if expected_message:
                self.assert_notification(expected_message)
            print(f"Deleted: '{description}'")
            return description

    # ADM-System Policy
    def system_policy_simple_search(self, text):
        self.close_all_form()
        self.click_menu('Administration', 'Bank Administration', 'System Policy')
        self.wait_for_button_available('Search')
        self.assert_form_title('ADM-System Policy-Search')
        self.simple_search(text=text, placeholder='Search Text')
        self.wait_loading()

    def system_policy_advanced_search(self, policy_id=None, desciption_of_policy=None, effective_from=None, effective_to=None):
        self.close_all_form()
        self.click_menu('Administration', 'Bank Administration', 'System Policy')
        self.wait_for_button_available('Search')
        self.assert_form_title('ADM-System Policy-Search')
        if policy_id:
            self.adv_search('Policy id', policy_id)
        if desciption_of_policy:
            self.adv_search_text('Desciption of policy', desciption_of_policy)
        if effective_from:
            self.adv_search_group('Effective from', effective_from)
        if effective_to:
            self.adv_search_group('Effective to', effective_to)
        self.click_button_search_advanced()
        self.wait_loading()

    def system_policy_add(self, policy_id=None, description_of_policy=None, effective_from=None, effective_to=None, enforce_password_history=None, maximum_password_age=None, minimum_password_length=None, password_must_meet_complexity_requirements=None, at_least_one_lower_case_letter=None, at_least_one_upper_case_letter=None, at_least_symbol_character=None, at_least_one_number=None, can_login_from=None, can_login_to=None, the_number_of_failed_logon_attempts=None, session_mode=None, list_error_message=None):
        # open form
        self.close_all_form()
        self.click_menu('Administration', 'Bank Administration', 'System Policy')
        self.wait_for_button_available('Add')
        self.click_button('Add')
        self.wait_for_button_available('Save')
        self.assert_form_title('ADM-System Policy-Add')
        # enter value
        if description_of_policy:
            self.bo_write_text_single('Description Of Policy', description_of_policy)
        if effective_from:
            self.bo_write_date_single('Effective From', effective_from)
        if effective_to:
            self.bo_write_date_single('Effective To', effective_to)
        if enforce_password_history:
            self.bo_write_number_single('Enforce Password History', enforce_password_history)
        if maximum_password_age:
            self.bo_write_number_single('Maximum Password age (0=unlimit)', maximum_password_age)
        if minimum_password_length:
            self.bo_write_number_single('Minimum Password Length', minimum_password_length)
        self.key_escape()
        if password_must_meet_complexity_requirements:
            self.bo_select_single('Password Must Meet Complexity Requirements', password_must_meet_complexity_requirements)
        self.key_escape()
        if at_least_one_lower_case_letter:
            self.bo_select_single('At Least One Lower Case Letter', at_least_one_lower_case_letter)
        self.key_escape()
        if at_least_one_upper_case_letter:
            self.bo_select_single('At Least One Upper Case Letter', at_least_one_upper_case_letter)
        self.key_escape()
        if at_least_symbol_character:
            self.bo_select_single("At Least Symbol Character (`~!@#$%^&*()-_=+[]{}|;:'\",<.>/?)", at_least_symbol_character)
        self.key_escape()
        if at_least_one_number:
            self.bo_select_single('At Least One Number', at_least_one_number)
        if can_login_from:
            self.bo_write_single('Can Login From', can_login_from)
        if can_login_to:
            self.bo_write_single('Can Login To', can_login_to)
        if the_number_of_failed_logon_attempts:
            self.bo_write_number_single('The Number Of Failed Logon Attempts (0=unlimit)', the_number_of_failed_logon_attempts)
        self.key_escape()
        if session_mode:
            self.bo_select_single('Session Mode', session_mode)
        # assert value
        if policy_id:
            self.bo_assert_value('Policy ID', policy_id)
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
            self.assert_notification('Saved successfully!')
            policy_id_out=self.bo_get_value('Policy ID')
            print(f'Policy ID: {policy_id_out}')
            return policy_id_out

    def system_policy_view(self, policy_id=None, description_of_policy=None, effective_from=None, effective_to=None, enforce_password_history=None, maximum_password_age=None, minimum_password_length=None, password_must_meet_complexity_requirements=None, at_least_symbol_character=None, at_least_one_upper_case_letter=None, at_least_one_lower_case_letter=None, at_least_one_number=None, can_login_from=None, can_login_to=None, the_number_of_failed_logon_attempts=None, session_mode=None):
        # search
        self.system_policy_advanced_search(policy_id=policy_id)
        self.assert_table_data('Policy ID', 1, policy_id)
        # view
        self.click_table_menu('View', 1)
        self.wait_for_button_available('Modify')
        self.assert_form_title('ADM-System Policy-View')
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

    def system_policy_update(self, policy_id=None, description_of_policy=None, effective_from=None, effective_to=None, enforce_password_history=None, maximum_password_age=None, minimum_password_length=None, password_must_meet_complexity_requirements=None, at_least_symbol_character=None, at_least_one_upper_case_letter=None, at_least_one_lower_case_letter=None, at_least_one_number=None, can_login_from=None, can_login_to=None, the_number_of_failed_logon_attempts=None, session_mode=None, list_error_message=None):
        # view
        self.system_policy_view(policy_id=policy_id)
        self.click_button('Modify')
        self.wait_loading()
        # update value
        self.bo_click_tab('Group Name')
        if description_of_policy:
            self.bo_write_text('Description Of Policy', description_of_policy)
        if effective_from:
            self.bo_write_date('Effective From', effective_from)
        if effective_to:
            self.bo_write_date('Effective To', effective_to)
        if enforce_password_history:
            self.bo_write_number('Enforce Password History', enforce_password_history)
        if maximum_password_age:
            self.bo_write_number('Maximum Password age (0=unlimit)', maximum_password_age)
        if minimum_password_length:
            self.bo_write_number('Minimum Password Length', minimum_password_length)
        self.key_escape()
        if password_must_meet_complexity_requirements:
            self.bo_select('Password Must Meet Complexity Requirements', password_must_meet_complexity_requirements)
        self.key_escape()
        if at_least_symbol_character:
            self.bo_select("At Least Symbol Character (`~!@#$%^&*()-_=+[]{}|;:'\",<.>/?)", at_least_symbol_character)
        self.key_escape()
        if at_least_one_upper_case_letter:
            self.bo_select('At Least One Upper Case Letter', at_least_one_upper_case_letter)
        self.key_escape()
        if at_least_one_lower_case_letter:
            self.bo_select('At Least One Lower Case Letter', at_least_one_lower_case_letter)
        self.key_escape()
        if at_least_one_number:
            self.bo_select('At Least One Number', at_least_one_number)
        if can_login_from:
            self.bo_write('Can Login From', can_login_from)
        if can_login_to:
            self.bo_write('Can Login To', can_login_to)
        if the_number_of_failed_logon_attempts:
            self.bo_write_number('The Number Of Failed Logon Attempts (0=unlimit)', the_number_of_failed_logon_attempts)
        self.key_escape()
        if session_mode:
            self.bo_select('Session Mode', session_mode)
        # assert value
        self.bo_click_tab('Group Name')
        if policy_id:
            self.bo_assert_value('Policy ID', policy_id)
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
            self.assert_notification('Saved successfully!')
            self.bo_click_tab('Group Name')
            policy_id_out=self.bo_get_value('Policy ID')
            print(f'Policy ID: {policy_id_out}')
            return policy_id_out

    def system_policy_delete(self, policy_id, list_error_message=None, expected_message=None):
        # search
        self.system_policy_advanced_search(policy_id=policy_id)
        self.assert_table_data('Policy ID', 1, policy_id)
        # delete
        self.click_table_menu('Delete', 1)
        self.wait_loading()
        self.click_button_in_popup('Yes')
        if list_error_message:
        # verify error
            self.assert_error_message()
            self.assert_list_error_message(list_error_message)
            print(f"Action delete '{policy_id}' failed!")
        else:
        # verify success
            if expected_message:
                self.assert_notification(expected_message)
            print(f"Deleted: '{policy_id}'")
            return policy_id

    # ADM-Currency
    def currency_simple_search(self, text):
        self.close_all_form()
        self.click_menu('Administration', 'List', 'Currency')
        self.wait_for_button_available('Search')
        self.assert_form_title('ADM-Currency-Search')
        self.simple_search(text=text, placeholder='Search text')
        self.wait_loading()

    def currency_advanced_search(self, currency_code=None, short_currency_code=None, currency_number=None, currency_number_from=None, currency_number_to=None, status=None, order=None, order_from=None, order_to=None):
        self.close_all_form()
        self.click_menu('Administration', 'List', 'Currency')
        self.wait_for_button_available('Search')
        self.assert_form_title('ADM-Currency-Search')
        if currency_code:
            self.adv_search_text('Currency code', currency_code)
        if short_currency_code:
            self.adv_search_text('Short currency code', short_currency_code)
        if currency_number:
            self.adv_search('Currency number', currency_number)
        if currency_number_from:
            self.adv_search_group('Currency number from', currency_number_from)
        if currency_number_to:
            self.adv_search_group('Currency number to', currency_number_to)
        self.key_escape()
        if status:
            self.adv_search_select('Status', status)
        if order:
            self.adv_search('Order', order)
        if order_from:
            self.adv_search_group('Order from', order_from)
        if order_to:
            self.adv_search_group('Order to', order_to)
        self.click_button_search_advanced()
        self.wait_loading()

    def currency_add(self, currency_code=None, short_currency_code=None, currency_number=None, currency_name_1=None, currency_name_2=None, currency_name_3=None, master_name_1=None, master_name_2=None, master_name_3=None, decimal_name_1=None, decimal_name_2=None, decimal_name_3=None, decimal_digits=None, rounding_digits=None, status_of_currency=None, order=None, list_error_message=None):
        # open form
        self.close_all_form()
        self.click_menu('Administration', 'List', 'Currency')
        self.wait_for_button_available('Add')
        self.click_button('Add')
        self.wait_for_button_available('Save')
        self.assert_form_title('ADM-Currency-Add')
        # enter value
        if currency_code:
            self.bo_write_single('Currency code', currency_code)
        if short_currency_code:
            self.bo_write_single('Short currency code', short_currency_code)
        if currency_number:
            self.bo_write_number_single('Currency number', currency_number)
        if currency_name_1:
            self.bo_click_collap('Currency name')
            self.bo_write_text_multi_single('Currency name', 'Currency name 1', currency_name_1)
        if currency_name_2:
            self.bo_click_collap('Currency name')
            self.bo_write_text_multi_single('Currency name', 'Currency name 2', currency_name_2)
        if currency_name_3:
            self.bo_click_collap('Currency name')
            self.bo_write_text_multi_single('Currency name', 'Currency name 3', currency_name_3)
        if master_name_1:
            self.bo_click_collap('Master name')
            self.bo_write_text_multi_single('Master name', 'Master name 1', master_name_1)
        if master_name_2:
            self.bo_click_collap('Master name')
            self.bo_write_text_multi_single('Master name', 'Master name 2', master_name_2)
        if master_name_3:
            self.bo_click_collap('Master name')
            self.bo_write_text_multi_single('Master name', 'Master name 3', master_name_3)
        if decimal_name_1:
            self.bo_click_collap('Decimal name')
            self.bo_write_text_multi_single('Decimal name', 'Decimal name 1', decimal_name_1)
        if decimal_name_2:
            self.bo_click_collap('Decimal name')
            self.bo_write_text_multi_single('Decimal name', 'Decimal name 2', decimal_name_2)
        if decimal_name_3:
            self.bo_click_collap('Decimal name')
            self.bo_write_text_multi_single('Decimal name', 'Decimal name 3', decimal_name_3)
        if decimal_digits:
            self.bo_write_number_single('Decimal digits', decimal_digits)
        if rounding_digits:
            self.bo_write_number_single('Rounding digits', rounding_digits)
        self.key_escape()
        if status_of_currency:
            self.bo_select_single('Status of currency', status_of_currency)
        if order:
            self.bo_write_number_single('Order', order)
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
            self.assert_notification('Saved successfully!')
            currency_code_out=self.bo_get_value_single('Currency code')
            print(f'Currency code: {currency_code_out}')
            return currency_code_out

    def currency_view(self, currency_code=None, short_currency_code=None, currency_number=None, currency_name_1=None, currency_name_2=None, currency_name_3=None, master_name_1=None, master_name_2=None, master_name_3=None, decimal_name_1=None, decimal_name_2=None, decimal_name_3=None, decimal_digits=None, rounding_digits=None, status_of_currency=None, order=None):
        # search
        self.currency_advanced_search(currency_code=currency_code)
        self.assert_table_data('Currency code', 1, currency_code)
        # view
        self.click_table_menu('View', 1)
        self.wait_for_button_available('Modify')
        self.assert_form_title('ADM-Currency-View')
        # verify value
        self.bo_click_tab('General')
        if currency_code:
            self.bo_assert_value('Currency code', currency_code)
        if short_currency_code:
            self.bo_assert_value('Short currency code', short_currency_code)
        if currency_number:
            self.bo_assert_value('Currency number', currency_number)
        if currency_name_1:
            self.bo_click_collap('Currency name')
            self.bo_assert_text_multi('Currency name', 'Currency name 1', currency_name_1)
        if currency_name_2:
            self.bo_click_collap('Currency name')
            self.bo_assert_text_multi('Currency name', 'Currency name 2', currency_name_2)
        if currency_name_3:
            self.bo_click_collap('Currency name')
            self.bo_assert_text_multi('Currency name', 'Currency name 3', currency_name_3)
        if master_name_1:
            self.bo_click_collap('Master name')
            self.bo_assert_text_multi('Master name', 'Master name 1', master_name_1)
        if master_name_2:
            self.bo_click_collap('Master name')
            self.bo_assert_text_multi('Master name', 'Master name 2', master_name_2)
        if master_name_3:
            self.bo_click_collap('Master name')
            self.bo_assert_text_multi('Master name', 'Master name 3', master_name_3)
        if decimal_name_1:
            self.bo_click_collap('Decimal name')
            self.bo_assert_text_multi('Decimal name', 'Decimal name 1', decimal_name_1)
        if decimal_name_2:
            self.bo_click_collap('Decimal name')
            self.bo_assert_text_multi('Decimal name', 'Decimal name 2', decimal_name_2)
        if decimal_name_3:
            self.bo_click_collap('Decimal name')
            self.bo_assert_text_multi('Decimal name', 'Decimal name 3', decimal_name_3)
        if decimal_digits:
            self.bo_assert_value('Decimal digits', decimal_digits)
        if rounding_digits:
            self.bo_assert_value('Rounding digits', rounding_digits)
        if status_of_currency:
            self.bo_assert_select('Status of currency', status_of_currency)
        if order:
            self.bo_assert_value('Order', order)

    def currency_update(self, currency_code=None, short_currency_code=None, currency_number=None, currency_name_1=None, currency_name_2=None, currency_name_3=None, master_name_1=None, master_name_2=None, master_name_3=None, decimal_name_1=None, decimal_name_2=None, decimal_name_3=None, decimal_digits=None, rounding_digits=None, status_of_currency=None, order=None, list_error_message=None):
        # view
        self.currency_view(currency_code=currency_code)
        self.click_button('Modify')
        self.wait_loading()
        # update value
        self.bo_click_tab('General')
        if short_currency_code:
            self.bo_write('Short currency code', short_currency_code)
        if currency_number:
            self.bo_write_number('Currency number', currency_number)
        if currency_name_1:
            self.bo_click_collap('Currency name')
            self.bo_write_text_multi('Currency name', 'Currency name 1', currency_name_1)
        if currency_name_2:
            self.bo_click_collap('Currency name')
            self.bo_write_text_multi('Currency name', 'Currency name 2', currency_name_2)
        if currency_name_3:
            self.bo_click_collap('Currency name')
            self.bo_write_text_multi('Currency name', 'Currency name 3', currency_name_3)
        if master_name_1:
            self.bo_click_collap('Master name')
            self.bo_write_text_multi('Master name', 'Master name 1', master_name_1)
        if master_name_2:
            self.bo_click_collap('Master name')
            self.bo_write_text_multi('Master name', 'Master name 2', master_name_2)
        if master_name_3:
            self.bo_click_collap('Master name')
            self.bo_write_text_multi('Master name', 'Master name 3', master_name_3)
        if decimal_name_1:
            self.bo_click_collap('Decimal name')
            self.bo_write_text_multi('Decimal name', 'Decimal name 1', decimal_name_1)
        if decimal_name_2:
            self.bo_click_collap('Decimal name')
            self.bo_write_text_multi('Decimal name', 'Decimal name 2', decimal_name_2)
        if decimal_name_3:
            self.bo_click_collap('Decimal name')
            self.bo_write_text_multi('Decimal name', 'Decimal name 3', decimal_name_3)
        if decimal_digits:
            self.bo_write_number('Decimal digits', decimal_digits)
        if rounding_digits:
            self.bo_write_number('Rounding digits', rounding_digits)
        self.key_escape()
        if status_of_currency:
            self.bo_select('Status of currency', status_of_currency)
        if order:
            self.bo_write_number('Order', order)
        # assert value
        self.bo_click_tab('General')
        if currency_code:
            self.bo_assert_value('Currency code', currency_code)
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
            self.assert_notification('Saved successfully!')
            self.bo_click_tab('General')
            currency_code_out=self.bo_get_value('Currency code')
            print(f'Currency code: {currency_code_out}')
            return currency_code_out

    def currency_delete(self, currency_code, list_error_message=None, expected_message=None):
        # search
        self.currency_advanced_search(currency_code=currency_code)
        self.assert_table_data('Currency code', 1, currency_code)
        # delete
        self.click_table_menu('Delete', 1)
        self.wait_loading()
        self.click_button_in_popup('Yes')
        if list_error_message:
        # verify error
            self.assert_error_message()
            self.assert_list_error_message(list_error_message)
            print(f"Action delete '{currency_code}' failed!")
        else:
        # verify success
            if expected_message:
                self.assert_notification(expected_message)
            print(f"Deleted: '{currency_code}'")
            return currency_code

    # ADM-Country
    def country_simple_search(self, text):
        self.close_all_form()
        self.click_menu('Administration', 'List', 'Country')
        self.wait_for_button_available('Search')
        self.assert_form_title('ADM-Country-Search')
        self.simple_search(text=text, placeholder='Search text')
        self.wait_loading()

    def country_advanced_search(self, iso_3_alpha=None, iso_2_alpha=None, country_name=None):
        self.close_all_form()
        self.click_menu('Administration', 'List', 'Country')
        self.wait_for_button_available('Search')
        self.assert_form_title('ADM-Country-Search')
        if iso_3_alpha:
            self.adv_search_text('ISO 3 alpha', iso_3_alpha)
        if iso_2_alpha:
            self.adv_search_text('ISO 2 alpha', iso_2_alpha)
        if country_name:
            self.adv_search_text('Country name', country_name)
        self.click_button_search_advanced()
        self.wait_loading()

    def country_add(self, iso_2_alpha=None, iso_3_alpha=None, country_name=None, country_name_1=None, country_name_2=None, country_name_3=None, country_short_name=None, short_name_1=None, short_name_2=None, short_name_3=None, currency_code=None, main_language=None, region_of_country=None, status_of_country=None, order=None, list_error_message=None):
        # open form
        self.close_all_form()
        self.click_menu('Administration', 'List', 'Country')
        self.wait_for_button_available('Add')
        self.click_button('Add')
        self.wait_for_button_available('Save')
        self.assert_form_title('ADM-Country-Add')
        # enter value
        if iso_2_alpha:
            self.bo_write_single('ISO 2 alpha', iso_2_alpha)
        if iso_3_alpha:
            self.bo_write_single('ISO 3 alpha', iso_3_alpha)
        if country_name:
            self.write_textarea('Country name', country_name)
        if country_name_1:
            self.bo_click_collap('Multi lingual country name')
            self.bo_write_text_multi_single('Multi lingual country name', 'Country name 1', country_name_1)
        if country_name_2:
            self.bo_click_collap('Multi lingual country name')
            self.bo_write_text_multi_single('Multi lingual country name', 'Country name 2', country_name_2)
        if country_name_3:
            self.bo_click_collap('Multi lingual country name')
            self.bo_write_text_multi_single('Multi lingual country name', 'Country name 3', country_name_3)
        if country_short_name:
            self.bo_write_text_single('Country short name', country_short_name)
        if short_name_1:
            self.bo_click_collap('Multi lingual country short name')
            self.bo_write_text_multi_single('Multi lingual country short name', 'Short name 1', short_name_1)
        if short_name_2:
            self.bo_click_collap('Multi lingual country short name')
            self.bo_write_text_multi_single('Multi lingual country short name', 'Short name 2', short_name_2)
        if short_name_3:
            self.bo_click_collap('Multi lingual country short name')
            self.bo_write_text_multi_single('Multi lingual country short name', 'Short name 3', short_name_3)
        self.key_escape()
        if currency_code:
            self.bo_select_single('Currency code', currency_code)
        self.key_escape()
        if main_language:
            self.bo_select_single('Main language', main_language)
        self.key_escape()
        if region_of_country:
            self.bo_select_single('Region of country', region_of_country)
        self.key_escape()
        if status_of_country:
            self.bo_select_single('Status of country', status_of_country)
        if order:
            self.bo_write_number_single('Order', order)
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
            self.assert_notification('Saved successfully!')
            iso_3_alpha_out=self.bo_get_value_single('ISO 3 alpha')
            print(f'ISO 3 alpha: {iso_3_alpha_out}')
            return iso_3_alpha_out

    def country_view(self, iso_2_alpha=None, iso_3_alpha=None, country_name=None, country_name_1=None, country_name_2=None, country_name_3=None, country_short_name=None, short_name_1=None, short_name_2=None, short_name_3=None, currency_code=None, main_language=None, region_of_country=None, status_of_country=None, order=None):
        # search
        self.country_advanced_search(iso_3_alpha=iso_3_alpha)
        self.assert_table_data('ISO 3 alpha', 1, iso_3_alpha)
        # view
        self.click_table_menu('View', 1)
        self.wait_for_button_available('Modify')
        self.assert_form_title('ADM-Country-View')
        # verify value
        self.bo_click_tab('General')
        if iso_2_alpha:
            self.bo_assert_value('ISO 2 alpha', iso_2_alpha)
        if iso_3_alpha:
            self.bo_assert_value('ISO 3 alpha', iso_3_alpha)
        if country_name:
            self.bo_assert_text('Country name', country_name)
        if country_name_1:
            self.bo_click_collap('Multi lingual country name')
            self.bo_assert_text_multi('Multi lingual country name', 'Country name 1', country_name_1)
        if country_name_2:
            self.bo_click_collap('Multi lingual country name')
            self.bo_assert_text_multi('Multi lingual country name', 'Country name 2', country_name_2)
        if country_name_3:
            self.bo_click_collap('Multi lingual country name')
            self.bo_assert_text_multi('Multi lingual country name', 'Country name 3', country_name_3)
        if country_short_name:
            self.bo_assert_text('Country short name', country_short_name)
        if short_name_1:
            self.bo_click_collap('Multi lingual country short name')
            self.bo_assert_text_multi('Multi lingual country short name', 'Short name 1', short_name_1)
        if short_name_2:
            self.bo_click_collap('Multi lingual country short name')
            self.bo_assert_text_multi('Multi lingual country short name', 'Short name 2', short_name_2)
        if short_name_3:
            self.bo_click_collap('Multi lingual country short name')
            self.bo_assert_text_multi('Multi lingual country short name', 'Short name 3', short_name_3)
        if currency_code:
            self.bo_assert_select('Currency code', currency_code)
        if main_language:
            self.bo_assert_select('Main language', main_language)
        if region_of_country:
            self.bo_assert_select('Region of country', region_of_country)
        if status_of_country:
            self.bo_assert_select('Status of country', status_of_country)
        if order:
            self.bo_assert_value('Order', order)

    def country_update(self, iso_2_alpha=None, iso_3_alpha=None, country_name=None, country_name_1=None, country_name_2=None, country_name_3=None, country_short_name=None, short_name_1=None, short_name_2=None, short_name_3=None, currency_code=None, main_language=None, region_of_country=None, status_of_country=None, order=None, list_error_message=None):
        # view
        self.country_view(iso_3_alpha=iso_3_alpha)
        self.click_button('Modify')
        self.wait_loading()
        # update value
        self.bo_click_tab('General')
        if iso_2_alpha:
            self.bo_write('ISO 2 alpha', iso_2_alpha)
        if country_name:
            self.bo_write_text('Country name', country_name)
        if country_name_1:
            self.bo_click_collap('Multi lingual country name')
            self.bo_write_text_multi('Multi lingual country name', 'Country name 1', country_name_1)
        if country_name_2:
            self.bo_click_collap('Multi lingual country name')
            self.bo_write_text_multi('Multi lingual country name', 'Country name 2', country_name_2)
        if country_name_3:
            self.bo_click_collap('Multi lingual country name')
            self.bo_write_text_multi('Multi lingual country name', 'Country name 3', country_name_3)
        if country_short_name:
            self.bo_write_text('Country short name', country_short_name)
        if short_name_1:
            self.bo_click_collap('Multi lingual country short name')
            self.bo_write_text_multi('Multi lingual country short name', 'Short name 1', short_name_1)
        if short_name_2:
            self.bo_click_collap('Multi lingual country short name')
            self.bo_write_text_multi('Multi lingual country short name', 'Short name 2', short_name_2)
        if short_name_3:
            self.bo_click_collap('Multi lingual country short name')
            self.bo_write_text_multi('Multi lingual country short name', 'Short name 3', short_name_3)
        self.key_escape()
        if currency_code:
            self.bo_select('Currency code', currency_code)
        self.key_escape()
        if main_language:
            self.bo_select('Main language', main_language)
        self.key_escape()
        if region_of_country:
            self.bo_select('Region of country', region_of_country)
        self.key_escape()
        if status_of_country:
            self.bo_select('Status of country', status_of_country)
        if order:
            self.bo_write_number('Order', order)
        # assert value
        self.bo_click_tab('General')
        if iso_3_alpha:
            self.bo_assert_value('ISO 3 alpha', iso_3_alpha)
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
            self.assert_notification('Saved successfully!')
            self.bo_click_tab('General')
            iso_3_alpha_out=self.bo_get_value('ISO 3 alpha')
            print(f'ISO 3 alpha: {iso_3_alpha_out}')
            return iso_3_alpha_out

    def country_delete(self, iso_3_alpha, list_error_message=None, expected_message=None):
        # search
        self.country_advanced_search(iso_3_alpha=iso_3_alpha)
        self.assert_table_data('ISO 3 alpha', 1, iso_3_alpha)
        # delete
        self.click_table_menu('Delete', 1)
        self.wait_loading()
        self.click_button_in_popup('Yes')
        if list_error_message:
        # verify error
            self.assert_error_message()
            self.assert_list_error_message(list_error_message)
            print(f"Action delete '{iso_3_alpha}' failed!")
        else:
        # verify success
            if expected_message:
                self.assert_notification(expected_message)
            print(f"Deleted: '{iso_3_alpha}'")
            return iso_3_alpha

# -------------------------- handle BO approval - ADMINISTRATION --------------------------
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

