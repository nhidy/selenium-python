import random
import webui_test
import os
from datetime import datetime
from webui_test.logging import log

from webui_test.form_action import FormAction
# thay doi path dan vao thu muc chua file excel
main_path = '../../data_excel/'
# KHONG thay doi cac tham so sau
data_environments = 'data_environments.xlsx'
url_file_data_environments = os.path.join(os.path.dirname(__file__), f'{main_path}{data_environments}')
sheet_url = 'LIST_URL'
sheet_user = 'LIST_USER'
# thay doi gia tri environment va data test
# ========== 117 ==========
# row_url = 1
# row_user = 12
# row_user_approve = 13
# row_user_reverse = 13
# customer_code_personal = '1-1-056810' # or get data sau khi run regression_customer.py
# ========== 104, 198, 128 ==========
row_url = 2 # 104
customer_code_personal = '1-1-001797' # 104
# row_url = 3 # 198
# customer_code_personal = '' # 198
# row_url = 4 # 128
# customer_code_personal = '' # 128
# row_url = 5 # 194
# customer_code_personal = '1-1-056756' # 194
row_user = 14
row_user_approve = 15
row_user_reverse = 15

# data test secure mortgage
catalogue_code_mortgage = '00000003'
collateral_asset_value = '4,500,000.00'

class RegressionMortgageTest(FormAction):
    def get_url(self):
        # get environment
        file_url = self.open_file_excel(sheet=sheet_url, url_file_name=url_file_data_environments)
        url = self.get_value_excel_cell(file_url, column='URL', row=row_url)
        return url

    def data_begin(self):
        log.debug("Go to data_begin method")
        # get data file user test
        file_user = self.open_file_excel(sheet=sheet_user, url_file_name=url_file_data_environments)
        # get username_reverse and password_reverse
        global username_approve, password_approve, username_reverse, password_reverse, username, password
        username_approve = self.get_value_excel_cell(file_user, column='Username', row=int(row_user_approve))
        password_approve = self.get_value_excel_cell(file_user, column='Password', row=int(row_user_approve))
        username_reverse = self.get_value_excel_cell(file_user, column='Username', row=int(row_user_reverse))
        password_reverse = self.get_value_excel_cell(file_user, column='Password', row=int(row_user_reverse))
        # get username and password
        username = self.get_value_excel_cell(file_user, column='Username', row=int(row_user))
        password = self.get_value_excel_cell(file_user, column='Password', row=int(row_user))
        self.login(username, password, one_app='Y')
        global working_date, branch_code
        working_date = self.get_working_date()
        branch_code = self.get_logged_branch_code()
        global gl_account_number
        gl_account_number = f'{branch_code}-1100601000000-01'

    def start_class(self):
        self.data_begin()

    def end_class(self):
        self.logout()

    def reset_browser(self):
        self.restart_browser(self)
        self.data_begin()

# # Check the data used for testing
#     def test_000_check_test_data_must_exist(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         self.add_gl_level_9_use_for_testing(
#             branch_code=branch_code,
#             currency_code='MMK',
#             account_number=gl_account_number
#         )
#         if self.check_customer_profile_not_exist(customer_code_personal):
#             self.stop()
#             self.fail()

    def test_001_open_mortgage_account_success(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        # open mortgage account
        global mortgage_account_cross_branch_mask
        mtg_opn_result = self.mtg_opn(
            customer_code=customer_code_personal,
            catalogue_code=catalogue_code_mortgage,
            collateral_asset_value=collateral_asset_value,
            reference_number='Ref AUTO TEST',
            evaluate_by='By AUTO TEST',
            approve_later='Y'
            # approve_on_form='Y',
            # username=username_approve,
            # password=password_approve,
        )
        transaction_references = mtg_opn_result[0]
        mortgage_account_cross_branch_mask = mtg_opn_result[1]
        self.mtg_opn_view(
            transaction_references=transaction_references,
            customer_code=customer_code_personal,
            catalogue_code=catalogue_code_mortgage,
            collateral_asset_value=collateral_asset_value,
            reference_number='Ref AUTO TEST',
            evaluate_by='By AUTO TEST',
            account_number=mortgage_account_cross_branch_mask,
        )

    def test_002_reset_browser(self):
        self.reset_browser()

    def test_003_approve_mortgage_account_success(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        # approve mortgage account
        mtg_apr_result = self.mtg_apr(
            account_number=mortgage_account_cross_branch_mask
        )
        transaction_references = mtg_apr_result[0]
        self.mtg_apr_view(
            transaction_references=transaction_references,
            account_number=mortgage_account_cross_branch_mask
        )

if __name__ == '__main__': 
    webui_test.main()