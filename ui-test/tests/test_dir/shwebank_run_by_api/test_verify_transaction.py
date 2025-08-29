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

# data test for 'Cheque'
stock_type_cq = 'Cheque'
stock_prefix_cq = 'CQ'
number_of_leaves_cq = '25'
number_of_book_cq = '1'
# data for current
catalogue_code_current = 'CAMMK0000'
deposit_amount_current = '1,000,000.54'
amount_current_valid = '0.01'
amount_current_invalid = '1,500,000.55'
# data for current USD
catalogue_code_current_usd = 'CAUSD0000'
deposit_amount_current_usd = '20,000.00'
amount_current_usd_valid = '0.01'
amount_current_usd_invalid = '25,000.01'
# data test for 'Passbook for Savings'
stock_type_sb = 'Passbook for Savings'
stock_prefix_sb = 'SB'
number_of_leaves_sb = '1'
number_of_book_sb = '1'
# data for savings
catalogue_code_savings = 'SAMMK0000'
deposit_amount_savings = '1,000,000.54'
amount_savings_valid = '0.01'
amount_savings_invalid = '1,500,000.55'
# data for bonus savings
catalogue_code_bonus_savings = 'BSMMK0000'
deposit_amount_bonus_savings = '1,000,000.54'
amount_bonus_savings_valid = '0.01'
amount_bonus_savings_invalid = '1,500,000.55'
# data test for 'Passbook for Fixed Deposit'
stock_type_fb = 'Passbook for Fixed Deposit'
stock_prefix_fb = 'FB'
number_of_leaves_fb = '1'
number_of_book_fb = '1'
# data for fixed
catalogue_code_fixed_01m = 'FD01PIMMK'
deposit_amount_fixed_01m = '1,000,000.65'
amount_fixed_01m_valid = '0.01'
amount_fixed_01m_invalid = '1,500,000.66'
# data test for 'Receipt'
stock_type_fr = 'Receipt'
stock_prefix_fr = 'FR'
number_of_leaves_fr = '1'
number_of_book_fr = '1'
# data for prepaid
catalogue_code_prepaid = 'PR007MMK0'
deposit_amount_prepaid = '1,000,000.65'
amount_prepaid_valid = '0.01'
amount_prepaid_invalid = '1,500,000.66'
# data test deposit status
status_pending = 'Pending to approve'
status_new = 'New'
status_normal = 'Normal'
status_dormant = 'Dormant'
status_block = 'Block'
status_closed = 'Closed'
status_reject = 'Reject'
# data test for fee
ifc_codes = ['308']
value_valid = '0.01000'
values_valid = [value_valid]
value_invalid = '1,500,000.66'
values_invalid = [value_invalid]
# data test deposit account use on 104
deposit_current_pending = '11-004-527250-1'
deposit_current_new = '11-004-606485-1'
deposit_current_normal = '11-004-973720-8'
deposit_current_dormant = '11-004-717987-9'
deposit_current_block = '11-004-348451-7'
deposit_current_close = '11-004-373067-4'
deposit_current_reject = '11-004-554210-1'

deposit_current_usd_pending = '12-004-431092-3'
deposit_current_usd_new = '12-004-131777-6'
deposit_current_usd_normal = '12-004-597864-9'
deposit_current_usd_dormant = '12-004-826768-9'
deposit_current_usd_block = '12-004-318107-8'
deposit_current_usd_close = '12-004-987788-9'
deposit_current_usd_reject = '12-004-739716-9'

deposit_savings_pending = '21-004-768949-9'
deposit_savings_new = '21-004-429271-5'
deposit_savings_normal = '21-004-517473-7'
deposit_savings_dormant = '21-004-787290-7'
deposit_savings_block = '21-004-682434-7'
deposit_savings_close = '21-004-991225-0'
deposit_savings_reject = '21-004-971432-6'

deposit_fixed_01m_pending = '41-004-181967-0'
deposit_fixed_01m_new = '41-004-052202-9'
deposit_fixed_01m_normal = '41-004-764968-8'
deposit_fixed_01m_block = '41-004-119540-6'
deposit_fixed_01m_close = '41-004-888846-0'
deposit_fixed_01m_reject = '41-004-029136-7'

deposit_prepaid_pending = '46-004-138545-4'
deposit_prepaid_new = '46-004-324063-6'
deposit_prepaid_normal = '46-004-953899-5'
deposit_prepaid_block = '46-004-427725-7'
deposit_prepaid_close = '46-004-472814-2'
deposit_prepaid_reject = '46-004-036047-6'

other_current_deposit_account = '11-004-455491-2'
other_savings_deposit_account = '31-001-214137-9'
from_serial_cq = 'CQ-777634'
to_serial_cq = 'CQ-777658'

deposit_prepaid_normal_valid = '46-004-050993-2'
from_serial_fr = 'FR-792620'
to_serial_fr = 'FR-792620'

deposit_fixed_01m_normal_valid = '41-004-635525-2'
from_serial_sb = 'SB-793428'
to_serial_sb = 'SB-793428'

class VerifyTransactionTest(FormAction):
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
        self.logout()
        self.restart_browser()
        self.data_begin()

# # Check the data used for testing
#     def test_000_01_check_test_data_must_exist(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         self.add_gl_level_9_use_for_testing(
#             branch_code=branch_code,
#             currency_code='MMK',
#             account_number=gl_account_number
#         )
#         if self.check_customer_profile_not_exist(customer_code_personal):
#             self.stop()
#             self.fail()

# # Create current deposit account use for testing
#     def test_000_02_create_current_deposit_account_use_for_testing(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         global deposit_current_pending
#         dpt_opn_result = self.dpt_opn(
#             customer_code=customer_code_personal,
#             customer_type='Single customer',
#             catalogue_code=catalogue_code_current,
#             reason_of_account_opening='Enter value reason of account opening'
#         )
#         deposit_current_pending=dpt_opn_result[1]
#         global deposit_current_new
#         dpt_opn_result = self.dpt_opn(
#             customer_code=customer_code_personal,
#             customer_type='Single customer',
#             catalogue_code=catalogue_code_current,
#             reason_of_account_opening='Enter value reason of account opening'
#         )
#         deposit_current_new=dpt_opn_result[1]
#         self.dpt_apr(
#             account_number=deposit_current_new,
#             approve_on_form='Y',
#             username=username_approve,
#             password=password_approve
#         )
#         generated_number = self.gen_serial_number(stock_prefix_cq, stock_type_cq, 24)
#         print(f'generated_number new: {generated_number}')
#         from_serial = generated_number[0]
#         to_serial = generated_number[1]
#         dpt_srg_result = self.dpt_srg(
#             stock_type=stock_type_cq,
#             from_serial=from_serial,
#             to_serial=to_serial,
#             stock_prefix=stock_prefix_cq,
#             number_of_leaves=number_of_leaves_cq,
#             number_of_book=number_of_book_cq,
#             approve_on_form='Y',
#             username=username_approve,
#             password=password_approve
#         )
#         from_serial_cq = dpt_srg_result[1]
#         to_serial_cq = dpt_srg_result[2]
#         self.dpt_sat(
#             stock_type=stock_type_cq,
#             from_serial=from_serial_cq,
#             to_serial=to_serial_cq,
#             assigned_staff_code=username_login
#         )
#         self.dpt_ccr(
#             stock_type=stock_type_cq,
#             from_serial=from_serial_cq,
#             to_serial=to_serial_cq,
#             approve_on_form='Y',
#             username=username_approve,
#             password=password_approve
#         )
#         self.dpt_cis(
#             account_number=deposit_current_new,
#             from_serial=from_serial_cq,
#             to_serial=to_serial_cq,
#             approve_on_form='Y',
#             username=username_approve,
#             password=password_approve,
#         )
#         global deposit_current_normal
#         dpt_opn_result = self.dpt_opn(
#             customer_code=customer_code_personal,
#             customer_type='Single customer',
#             catalogue_code=catalogue_code_current,
#             reason_of_account_opening='Enter value reason of account opening'
#         )
#         deposit_current_normal=dpt_opn_result[1]
#         self.dpt_apr(
#             account_number=deposit_current_normal,
#             approve_on_form='Y',
#             username=username_approve,
#             password=password_approve
#         )
#         self.dpt_cdp(
#             account_number=deposit_current_normal,
#             amount_deposit=deposit_amount_current,
#             approve_on_form='Y',
#             username=username_approve,
#             password=password_approve
#         )
#         generated_number = self.gen_serial_number(stock_prefix_cq, stock_type_cq, 24)
#         print(f'generated_number normal: {generated_number}')
#         from_serial = generated_number[0]
#         to_serial = generated_number[1]
#         dpt_srg_result = self.dpt_srg(
#             stock_type=stock_type_cq,
#             from_serial=from_serial,
#             to_serial=to_serial,
#             stock_prefix=stock_prefix_cq,
#             number_of_leaves=number_of_leaves_cq,
#             number_of_book=number_of_book_cq,
#             approve_on_form='Y',
#             username=username_approve,
#             password=password_approve
#         )
#         from_serial_cq = dpt_srg_result[1]
#         to_serial_cq = dpt_srg_result[2]
#         self.dpt_sat(
#             stock_type=stock_type_cq,
#             from_serial=from_serial_cq,
#             to_serial=to_serial_cq,
#             assigned_staff_code=username_login
#         )
#         self.dpt_ccr(
#             stock_type=stock_type_cq,
#             from_serial=from_serial_cq,
#             to_serial=to_serial_cq,
#             approve_on_form='Y',
#             username=username_approve,
#             password=password_approve
#         )
#         self.dpt_cis(
#             account_number=deposit_current_normal,
#             from_serial=from_serial_cq,
#             to_serial=to_serial_cq,
#             approve_on_form='Y',
#             username=username_approve,
#             password=password_approve,
#         )
#         global deposit_current_dormant
#         dpt_opn_result = self.dpt_opn(
#             customer_code=customer_code_personal,
#             customer_type='Single customer',
#             catalogue_code=catalogue_code_current,
#             reason_of_account_opening='Enter value reason of account opening'
#         )
#         deposit_current_dormant=dpt_opn_result[1]
#         self.dpt_apr(
#             account_number=deposit_current_dormant,
#             approve_on_form='Y',
#             username=username_approve,
#             password=password_approve
#         )
#         self.dpt_cdp(
#             account_number=deposit_current_dormant,
#             amount_deposit=deposit_amount_current,
#             approve_on_form='Y',
#             username=username_approve,
#             password=password_approve
#         )
#         self.dpt_cas(
#             account_number=deposit_current_dormant,
#             new_status=status_dormant,
#             current_status=status_normal,
#             approve_on_form='Y',
#             username=username_approve,
#             password=password_approve
#         )
#         generated_number = self.gen_serial_number(stock_prefix_cq, stock_type_cq, 24)
#         print(f'generated_number dormant: {generated_number}')
#         from_serial = generated_number[0]
#         to_serial = generated_number[1]
#         dpt_srg_result = self.dpt_srg(
#             stock_type=stock_type_cq,
#             from_serial=from_serial,
#             to_serial=to_serial,
#             stock_prefix=stock_prefix_cq,
#             number_of_leaves=number_of_leaves_cq,
#             number_of_book=number_of_book_cq,
#             approve_on_form='Y',
#             username=username_approve,
#             password=password_approve
#         )
#         from_serial_cq = dpt_srg_result[1]
#         to_serial_cq = dpt_srg_result[2]
#         self.dpt_sat(
#             stock_type=stock_type_cq,
#             from_serial=from_serial_cq,
#             to_serial=to_serial_cq,
#             assigned_staff_code=username_login
#         )
#         self.dpt_ccr(
#             stock_type=stock_type_cq,
#             from_serial=from_serial_cq,
#             to_serial=to_serial_cq,
#             approve_on_form='Y',
#             username=username_approve,
#             password=password_approve
#         )
#         self.dpt_cis(
#             account_number=deposit_current_dormant,
#             from_serial=from_serial_cq,
#             to_serial=to_serial_cq,
#             approve_on_form='Y',
#             username=username_approve,
#             password=password_approve,
#         )
#         global deposit_current_block
#         dpt_opn_result = self.dpt_opn(
#             customer_code=customer_code_personal,
#             customer_type='Single customer',
#             catalogue_code=catalogue_code_current,
#             reason_of_account_opening='Enter value reason of account opening'
#         )
#         deposit_current_block=dpt_opn_result[1]
#         self.dpt_apr(
#             account_number=deposit_current_block,
#             approve_on_form='Y',
#             username=username_approve,
#             password=password_approve
#         )
#         self.dpt_cdp(
#             account_number=deposit_current_block,
#             amount_deposit=deposit_amount_current,
#             approve_on_form='Y',
#             username=username_approve,
#             password=password_approve
#         )
#         generated_number = self.gen_serial_number(stock_prefix_cq, stock_type_cq, 24)
#         print(f'generated_number block: {generated_number}')
#         from_serial = generated_number[0]
#         to_serial = generated_number[1]
#         dpt_srg_result = self.dpt_srg(
#             stock_type=stock_type_cq,
#             from_serial=from_serial,
#             to_serial=to_serial,
#             stock_prefix=stock_prefix_cq,
#             number_of_leaves=number_of_leaves_cq,
#             number_of_book=number_of_book_cq,
#             approve_on_form='Y',
#             username=username_approve,
#             password=password_approve
#         )
#         from_serial_cq = dpt_srg_result[1]
#         to_serial_cq = dpt_srg_result[2]
#         self.dpt_sat(
#             stock_type=stock_type_cq,
#             from_serial=from_serial_cq,
#             to_serial=to_serial_cq,
#             assigned_staff_code=username_login
#         )
#         self.dpt_ccr(
#             stock_type=stock_type_cq,
#             from_serial=from_serial_cq,
#             to_serial=to_serial_cq,
#             approve_on_form='Y',
#             username=username_approve,
#             password=password_approve
#         )
#         self.dpt_cis(
#             account_number=deposit_current_block,
#             from_serial=from_serial_cq,
#             to_serial=to_serial_cq,
#             approve_on_form='Y',
#             username=username_approve,
#             password=password_approve,
#         )
#         self.dpt_blk(
#             account_number=deposit_current_block,
#             approve_on_form='Y',
#             username=username_approve,
#             password=password_approve
#         )
#         global deposit_current_close
#         dpt_opn_result = self.dpt_opn(
#             customer_code=customer_code_personal,
#             customer_type='Single customer',
#             catalogue_code=catalogue_code_current,
#             reason_of_account_opening='Enter value reason of account opening'
#         )
#         deposit_current_close=dpt_opn_result[1]
#         self.dpt_apr(
#             account_number=deposit_current_close,
#             approve_on_form='Y',
#             username=username_approve,
#             password=password_approve
#         )
#         generated_number = self.gen_serial_number(stock_prefix_cq, stock_type_cq, 24)
#         print(f'generated_number close: {generated_number}')
#         from_serial = generated_number[0]
#         to_serial = generated_number[1]
#         dpt_srg_result = self.dpt_srg(
#             stock_type=stock_type_cq,
#             from_serial=from_serial,
#             to_serial=to_serial,
#             stock_prefix=stock_prefix_cq,
#             number_of_leaves=number_of_leaves_cq,
#             number_of_book=number_of_book_cq,
#             approve_on_form='Y',
#             username=username_approve,
#             password=password_approve
#         )
#         from_serial_cq = dpt_srg_result[1]
#         to_serial_cq = dpt_srg_result[2]
#         self.dpt_sat(
#             stock_type=stock_type_cq,
#             from_serial=from_serial_cq,
#             to_serial=to_serial_cq,
#             assigned_staff_code=username_login
#         )
#         self.dpt_ccr(
#             stock_type=stock_type_cq,
#             from_serial=from_serial_cq,
#             to_serial=to_serial_cq,
#             approve_on_form='Y',
#             username=username_approve,
#             password=password_approve
#         )
#         self.dpt_cis(
#             account_number=deposit_current_close,
#             from_serial=from_serial_cq,
#             to_serial=to_serial_cq,
#             approve_on_form='Y',
#             username=username_approve,
#             password=password_approve,
#         )
#         self.dpt_cls(
#             account_number=deposit_current_close,
#         )
#         global deposit_current_reject
#         dpt_opn_result = self.dpt_opn(
#             customer_code=customer_code_personal,
#             customer_type='Single customer',
#             catalogue_code=catalogue_code_current,
#             reason_of_account_opening='Enter value reason of account opening'
#         )
#         deposit_current_reject=dpt_opn_result[1]
#         self.dpt_rej(
#             account_number=deposit_current_reject,
#         )

# # Create current usd deposit account use for testing
#     def test_000_03_create_current_usd_deposit_account_use_for_testing(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         global deposit_current_usd_pending
#         dpt_opn_result = self.dpt_opn(
#             customer_code=customer_code_personal,
#             customer_type='Single customer',
#             catalogue_code=catalogue_code_current_usd,
#             reason_of_account_opening='Enter value reason of account opening'
#         )
#         deposit_current_usd_pending=dpt_opn_result[1]
#         global deposit_current_usd_new
#         dpt_opn_result = self.dpt_opn(
#             customer_code=customer_code_personal,
#             customer_type='Single customer',
#             catalogue_code=catalogue_code_current_usd,
#             reason_of_account_opening='Enter value reason of account opening'
#         )
#         deposit_current_usd_new=dpt_opn_result[1]
#         self.dpt_apr(
#             account_number=deposit_current_usd_new,
#             approve_on_form='Y',
#             username=username_approve,
#             password=password_approve
#         )
#         generated_number = self.gen_serial_number(stock_prefix_cq, stock_type_cq, 24)
#         print(f'generated_number new: {generated_number}')
#         from_serial = generated_number[0]
#         to_serial = generated_number[1]
#         dpt_srg_result = self.dpt_srg(
#             stock_type=stock_type_cq,
#             from_serial=from_serial,
#             to_serial=to_serial,
#             stock_prefix=stock_prefix_cq,
#             number_of_leaves=number_of_leaves_cq,
#             number_of_book=number_of_book_cq,
#             approve_on_form='Y',
#             username=username_approve,
#             password=password_approve
#         )
#         from_serial_cq = dpt_srg_result[1]
#         to_serial_cq = dpt_srg_result[2]
#         self.dpt_sat(
#             stock_type=stock_type_cq,
#             from_serial=from_serial_cq,
#             to_serial=to_serial_cq,
#             assigned_staff_code=username_login
#         )
#         self.dpt_ccr(
#             stock_type=stock_type_cq,
#             from_serial=from_serial_cq,
#             to_serial=to_serial_cq,
#             approve_on_form='Y',
#             username=username_approve,
#             password=password_approve
#         )
#         self.dpt_cis(
#             account_number=deposit_current_usd_new,
#             from_serial=from_serial_cq,
#             to_serial=to_serial_cq,
#             approve_on_form='Y',
#             username=username_approve,
#             password=password_approve,
#         )
#         global deposit_current_usd_normal
#         dpt_opn_result = self.dpt_opn(
#             customer_code=customer_code_personal,
#             customer_type='Single customer',
#             catalogue_code=catalogue_code_current_usd,
#             reason_of_account_opening='Enter value reason of account opening'
#         )
#         deposit_current_usd_normal=dpt_opn_result[1]
#         self.dpt_apr(
#             account_number=deposit_current_usd_normal,
#             approve_on_form='Y',
#             username=username_approve,
#             password=password_approve
#         )
#         self.dpt_cdp(
#             account_number=deposit_current_usd_normal,
#             amount_deposit=deposit_amount_current_usd,
#             approve_on_form='Y',
#             username=username_approve,
#             password=password_approve
#         )
#         generated_number = self.gen_serial_number(stock_prefix_cq, stock_type_cq, 24)
#         print(f'generated_number normal: {generated_number}')
#         from_serial = generated_number[0]
#         to_serial = generated_number[1]
#         dpt_srg_result = self.dpt_srg(
#             stock_type=stock_type_cq,
#             from_serial=from_serial,
#             to_serial=to_serial,
#             stock_prefix=stock_prefix_cq,
#             number_of_leaves=number_of_leaves_cq,
#             number_of_book=number_of_book_cq,
#             approve_on_form='Y',
#             username=username_approve,
#             password=password_approve
#         )
#         from_serial_cq = dpt_srg_result[1]
#         to_serial_cq = dpt_srg_result[2]
#         self.dpt_sat(
#             stock_type=stock_type_cq,
#             from_serial=from_serial_cq,
#             to_serial=to_serial_cq,
#             assigned_staff_code=username_login
#         )
#         self.dpt_ccr(
#             stock_type=stock_type_cq,
#             from_serial=from_serial_cq,
#             to_serial=to_serial_cq,
#             approve_on_form='Y',
#             username=username_approve,
#             password=password_approve
#         )
#         self.dpt_cis(
#             account_number=deposit_current_usd_normal,
#             from_serial=from_serial_cq,
#             to_serial=to_serial_cq,
#             approve_on_form='Y',
#             username=username_approve,
#             password=password_approve,
#         )
#         global deposit_current_usd_dormant
#         dpt_opn_result = self.dpt_opn(
#             customer_code=customer_code_personal,
#             customer_type='Single customer',
#             catalogue_code=catalogue_code_current_usd,
#             reason_of_account_opening='Enter value reason of account opening'
#         )
#         deposit_current_usd_dormant=dpt_opn_result[1]
#         self.dpt_apr(
#             account_number=deposit_current_usd_dormant,
#             approve_on_form='Y',
#             username=username_approve,
#             password=password_approve
#         )
#         self.dpt_cdp(
#             account_number=deposit_current_usd_dormant,
#             amount_deposit=deposit_amount_current_usd,
#             approve_on_form='Y',
#             username=username_approve,
#             password=password_approve
#         )
#         self.dpt_cas(
#             account_number=deposit_current_usd_dormant,
#             new_status=status_dormant,
#             current_status=status_normal,
#             approve_on_form='Y',
#             username=username_approve,
#             password=password_approve
#         )
#         generated_number = self.gen_serial_number(stock_prefix_cq, stock_type_cq, 24)
#         print(f'generated_number dormant: {generated_number}')
#         from_serial = generated_number[0]
#         to_serial = generated_number[1]
#         dpt_srg_result = self.dpt_srg(
#             stock_type=stock_type_cq,
#             from_serial=from_serial,
#             to_serial=to_serial,
#             stock_prefix=stock_prefix_cq,
#             number_of_leaves=number_of_leaves_cq,
#             number_of_book=number_of_book_cq,
#             approve_on_form='Y',
#             username=username_approve,
#             password=password_approve
#         )
#         from_serial_cq = dpt_srg_result[1]
#         to_serial_cq = dpt_srg_result[2]
#         self.dpt_sat(
#             stock_type=stock_type_cq,
#             from_serial=from_serial_cq,
#             to_serial=to_serial_cq,
#             assigned_staff_code=username_login
#         )
#         self.dpt_ccr(
#             stock_type=stock_type_cq,
#             from_serial=from_serial_cq,
#             to_serial=to_serial_cq,
#             approve_on_form='Y',
#             username=username_approve,
#             password=password_approve
#         )
#         self.dpt_cis(
#             account_number=deposit_current_usd_dormant,
#             from_serial=from_serial_cq,
#             to_serial=to_serial_cq,
#             approve_on_form='Y',
#             username=username_approve,
#             password=password_approve,
#         )
#         global deposit_current_usd_block
#         dpt_opn_result = self.dpt_opn(
#             customer_code=customer_code_personal,
#             customer_type='Single customer',
#             catalogue_code=catalogue_code_current_usd,
#             reason_of_account_opening='Enter value reason of account opening'
#         )
#         deposit_current_usd_block=dpt_opn_result[1]
#         self.dpt_apr(
#             account_number=deposit_current_usd_block,
#             approve_on_form='Y',
#             username=username_approve,
#             password=password_approve
#         )
#         self.dpt_cdp(
#             account_number=deposit_current_usd_block,
#             amount_deposit=deposit_amount_current_usd,
#             approve_on_form='Y',
#             username=username_approve,
#             password=password_approve
#         )
#         generated_number = self.gen_serial_number(stock_prefix_cq, stock_type_cq, 24)
#         print(f'generated_number block: {generated_number}')
#         from_serial = generated_number[0]
#         to_serial = generated_number[1]
#         dpt_srg_result = self.dpt_srg(
#             stock_type=stock_type_cq,
#             from_serial=from_serial,
#             to_serial=to_serial,
#             stock_prefix=stock_prefix_cq,
#             number_of_leaves=number_of_leaves_cq,
#             number_of_book=number_of_book_cq,
#             approve_on_form='Y',
#             username=username_approve,
#             password=password_approve
#         )
#         from_serial_cq = dpt_srg_result[1]
#         to_serial_cq = dpt_srg_result[2]
#         self.dpt_sat(
#             stock_type=stock_type_cq,
#             from_serial=from_serial_cq,
#             to_serial=to_serial_cq,
#             assigned_staff_code=username_login
#         )
#         self.dpt_ccr(
#             stock_type=stock_type_cq,
#             from_serial=from_serial_cq,
#             to_serial=to_serial_cq,
#             approve_on_form='Y',
#             username=username_approve,
#             password=password_approve
#         )
#         self.dpt_cis(
#             account_number=deposit_current_usd_block,
#             from_serial=from_serial_cq,
#             to_serial=to_serial_cq,
#             approve_on_form='Y',
#             username=username_approve,
#             password=password_approve,
#         )
#         self.dpt_blk(
#             account_number=deposit_current_usd_block,
#             approve_on_form='Y',
#             username=username_approve,
#             password=password_approve
#         )
#         global deposit_current_usd_close
#         dpt_opn_result = self.dpt_opn(
#             customer_code=customer_code_personal,
#             customer_type='Single customer',
#             catalogue_code=catalogue_code_current_usd,
#             reason_of_account_opening='Enter value reason of account opening'
#         )
#         deposit_current_usd_close=dpt_opn_result[1]
#         self.dpt_apr(
#             account_number=deposit_current_usd_close,
#             approve_on_form='Y',
#             username=username_approve,
#             password=password_approve
#         )
#         generated_number = self.gen_serial_number(stock_prefix_cq, stock_type_cq, 24)
#         print(f'generated_number close: {generated_number}')
#         from_serial = generated_number[0]
#         to_serial = generated_number[1]
#         dpt_srg_result = self.dpt_srg(
#             stock_type=stock_type_cq,
#             from_serial=from_serial,
#             to_serial=to_serial,
#             stock_prefix=stock_prefix_cq,
#             number_of_leaves=number_of_leaves_cq,
#             number_of_book=number_of_book_cq,
#             approve_on_form='Y',
#             username=username_approve,
#             password=password_approve
#         )
#         from_serial_cq = dpt_srg_result[1]
#         to_serial_cq = dpt_srg_result[2]
#         self.dpt_sat(
#             stock_type=stock_type_cq,
#             from_serial=from_serial_cq,
#             to_serial=to_serial_cq,
#             assigned_staff_code=username_login
#         )
#         self.dpt_ccr(
#             stock_type=stock_type_cq,
#             from_serial=from_serial_cq,
#             to_serial=to_serial_cq,
#             approve_on_form='Y',
#             username=username_approve,
#             password=password_approve
#         )
#         self.dpt_cis(
#             account_number=deposit_current_usd_close,
#             from_serial=from_serial_cq,
#             to_serial=to_serial_cq,
#             approve_on_form='Y',
#             username=username_approve,
#             password=password_approve,
#         )
#         self.dpt_cls(
#             account_number=deposit_current_usd_close,
#         )
#         global deposit_current_usd_reject
#         dpt_opn_result = self.dpt_opn(
#             customer_code=customer_code_personal,
#             customer_type='Single customer',
#             catalogue_code=catalogue_code_current_usd,
#             reason_of_account_opening='Enter value reason of account opening'
#         )
#         deposit_current_usd_reject=dpt_opn_result[1]
#         self.dpt_rej(
#             account_number=deposit_current_usd_reject,
#         )

# # Create savings deposit account use for testing
#     def test_000_04_create_savings_deposit_account_use_for_testing(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         global deposit_savings_pending
#         dpt_opn_result = self.dpt_opn(
#             customer_code=customer_code_personal,
#             customer_type='Single customer',
#             catalogue_code=catalogue_code_savings,
#             reason_of_account_opening='Enter value reason of account opening'
#         )
#         deposit_savings_pending=dpt_opn_result[1]
#         global deposit_savings_new
#         dpt_opn_result = self.dpt_opn(
#             customer_code=customer_code_personal,
#             customer_type='Single customer',
#             catalogue_code=catalogue_code_savings,
#             reason_of_account_opening='Enter value reason of account opening'
#         )
#         deposit_savings_new=dpt_opn_result[1]
#         self.dpt_apr(
#             account_number=deposit_savings_new,
#             approve_on_form='Y',
#             username=username_approve,
#             password=password_approve
#         )
#         generated_number = self.gen_serial_number(stock_prefix_sb, stock_type_sb, 0)
#         print(f'generated_number new: {generated_number}')
#         from_serial = generated_number[0]
#         to_serial = generated_number[1]
#         dpt_srg_result = self.dpt_srg(
#             stock_type=stock_type_sb,
#             from_serial=from_serial,
#             to_serial=to_serial,
#             stock_prefix=stock_prefix_sb,
#             number_of_leaves=number_of_leaves_sb,
#             number_of_book=number_of_book_sb,
#             approve_on_form='Y',
#             username=username_approve,
#             password=password_approve
#         )
#         from_serial_sb = dpt_srg_result[1]
#         to_serial_sb = dpt_srg_result[2]
#         self.dpt_sat(
#             stock_type=stock_type_sb,
#             from_serial=from_serial_sb,
#             to_serial=to_serial_sb,
#             assigned_staff_code=username_login
#         )
#         self.dpt_ccr(
#             stock_type=stock_type_sb,
#             from_serial=from_serial_sb,
#             to_serial=to_serial_sb,
#             approve_on_form='Y',
#             username=username_approve,
#             password=password_approve
#         )
#         self.dpt_sbi(
#             account_number=deposit_savings_new,
#             serial_no=from_serial_sb,
#             approve_on_form='Y',
#             username=username_approve,
#             password=password_approve
#         )
#         global deposit_savings_normal
#         dpt_opn_result = self.dpt_opn(
#             customer_code=customer_code_personal,
#             customer_type='Single customer',
#             catalogue_code=catalogue_code_savings,
#             reason_of_account_opening='Enter value reason of account opening'
#         )
#         deposit_savings_normal=dpt_opn_result[1]
#         self.dpt_apr(
#             account_number=deposit_savings_normal,
#             approve_on_form='Y',
#             username=username_approve,
#             password=password_approve
#         )
#         self.dpt_cdp(
#             account_number=deposit_savings_normal,
#             amount_deposit=deposit_amount_savings,
#             approve_on_form='Y',
#             username=username_approve,
#             password=password_approve
#         )
#         generated_number = self.gen_serial_number(stock_prefix_sb, stock_type_sb, 0)
#         print(f'generated_number normal: {generated_number}')
#         from_serial = generated_number[0]
#         to_serial = generated_number[1]
#         dpt_srg_result = self.dpt_srg(
#             stock_type=stock_type_sb,
#             from_serial=from_serial,
#             to_serial=to_serial,
#             stock_prefix=stock_prefix_sb,
#             number_of_leaves=number_of_leaves_sb,
#             number_of_book=number_of_book_sb,
#             approve_on_form='Y',
#             username=username_approve,
#             password=password_approve
#         )
#         from_serial_sb = dpt_srg_result[1]
#         to_serial_sb = dpt_srg_result[2]
#         self.dpt_sat(
#             stock_type=stock_type_sb,
#             from_serial=from_serial_sb,
#             to_serial=to_serial_sb,
#             assigned_staff_code=username_login
#         )
#         self.dpt_ccr(
#             stock_type=stock_type_sb,
#             from_serial=from_serial_sb,
#             to_serial=to_serial_sb,
#             approve_on_form='Y',
#             username=username_approve,
#             password=password_approve
#         )
#         self.dpt_sbi(
#             account_number=deposit_savings_normal,
#             serial_no=from_serial_sb,
#             approve_on_form='Y',
#             username=username_approve,
#             password=password_approve
#         )
#         global deposit_savings_dormant
#         dpt_opn_result = self.dpt_opn(
#             customer_code=customer_code_personal,
#             customer_type='Single customer',
#             catalogue_code=catalogue_code_savings,
#             reason_of_account_opening='Enter value reason of account opening'
#         )
#         deposit_savings_dormant=dpt_opn_result[1]
#         self.dpt_apr(
#             account_number=deposit_savings_dormant,
#             approve_on_form='Y',
#             username=username_approve,
#             password=password_approve
#         )
#         self.dpt_cdp(
#             account_number=deposit_savings_dormant,
#             amount_deposit=deposit_amount_savings,
#             approve_on_form='Y',
#             username=username_approve,
#             password=password_approve
#         )
#         self.dpt_cas(
#             account_number=deposit_savings_dormant,
#             new_status=status_dormant,
#             current_status=status_normal,
#             approve_on_form='Y',
#             username=username_approve,
#             password=password_approve
#         )
#         generated_number = self.gen_serial_number(stock_prefix_sb, stock_type_sb, 0)
#         print(f'generated_number dormant: {generated_number}')
#         from_serial = generated_number[0]
#         to_serial = generated_number[1]
#         dpt_srg_result = self.dpt_srg(
#             stock_type=stock_type_sb,
#             from_serial=from_serial,
#             to_serial=to_serial,
#             stock_prefix=stock_prefix_sb,
#             number_of_leaves=number_of_leaves_sb,
#             number_of_book=number_of_book_sb,
#             approve_on_form='Y',
#             username=username_approve,
#             password=password_approve
#         )
#         from_serial_sb = dpt_srg_result[1]
#         to_serial_sb = dpt_srg_result[2]
#         self.dpt_sat(
#             stock_type=stock_type_sb,
#             from_serial=from_serial_sb,
#             to_serial=to_serial_sb,
#             assigned_staff_code=username_login
#         )
#         self.dpt_ccr(
#             stock_type=stock_type_sb,
#             from_serial=from_serial_sb,
#             to_serial=to_serial_sb,
#             approve_on_form='Y',
#             username=username_approve,
#             password=password_approve
#         )
#         self.dpt_sbi(
#             account_number=deposit_savings_dormant,
#             serial_no=from_serial_sb,
#             approve_on_form='Y',
#             username=username_approve,
#             password=password_approve
#         )
#         global deposit_savings_block
#         dpt_opn_result = self.dpt_opn(
#             customer_code=customer_code_personal,
#             customer_type='Single customer',
#             catalogue_code=catalogue_code_savings,
#             reason_of_account_opening='Enter value reason of account opening'
#         )
#         deposit_savings_block=dpt_opn_result[1]
#         self.dpt_apr(
#             account_number=deposit_savings_block,
#             approve_on_form='Y',
#             username=username_approve,
#             password=password_approve
#         )
#         self.dpt_cdp(
#             account_number=deposit_savings_block,
#             amount_deposit=deposit_amount_savings,
#             approve_on_form='Y',
#             username=username_approve,
#             password=password_approve
#         )
#         generated_number = self.gen_serial_number(stock_prefix_sb, stock_type_sb, 0)
#         print(f'generated_number block: {generated_number}')
#         from_serial = generated_number[0]
#         to_serial = generated_number[1]
#         dpt_srg_result = self.dpt_srg(
#             stock_type=stock_type_sb,
#             from_serial=from_serial,
#             to_serial=to_serial,
#             stock_prefix=stock_prefix_sb,
#             number_of_leaves=number_of_leaves_sb,
#             number_of_book=number_of_book_sb,
#             approve_on_form='Y',
#             username=username_approve,
#             password=password_approve
#         )
#         from_serial_sb = dpt_srg_result[1]
#         to_serial_sb = dpt_srg_result[2]
#         self.dpt_sat(
#             stock_type=stock_type_sb,
#             from_serial=from_serial_sb,
#             to_serial=to_serial_sb,
#             assigned_staff_code=username_login
#         )
#         self.dpt_ccr(
#             stock_type=stock_type_sb,
#             from_serial=from_serial_sb,
#             to_serial=to_serial_sb,
#             approve_on_form='Y',
#             username=username_approve,
#             password=password_approve
#         )
#         self.dpt_sbi(
#             account_number=deposit_savings_block,
#             serial_no=from_serial_sb,
#             approve_on_form='Y',
#             username=username_approve,
#             password=password_approve
#         )
#         self.dpt_blk(
#             account_number=deposit_savings_block,
#             approve_on_form='Y',
#             username=username_approve,
#             password=password_approve
#         )
#         global deposit_savings_close
#         dpt_opn_result = self.dpt_opn(
#             customer_code=customer_code_personal,
#             customer_type='Single customer',
#             catalogue_code=catalogue_code_savings,
#             reason_of_account_opening='Enter value reason of account opening'
#         )
#         deposit_savings_close=dpt_opn_result[1]
#         self.dpt_apr(
#             account_number=deposit_savings_close,
#             approve_on_form='Y',
#             username=username_approve,
#             password=password_approve
#         )
#         generated_number = self.gen_serial_number(stock_prefix_sb, stock_type_sb, 0)
#         print(f'generated_number close: {generated_number}')
#         from_serial = generated_number[0]
#         to_serial = generated_number[1]
#         dpt_srg_result = self.dpt_srg(
#             stock_type=stock_type_sb,
#             from_serial=from_serial,
#             to_serial=to_serial,
#             stock_prefix=stock_prefix_sb,
#             number_of_leaves=number_of_leaves_sb,
#             number_of_book=number_of_book_sb,
#             approve_on_form='Y',
#             username=username_approve,
#             password=password_approve
#         )
#         from_serial_sb = dpt_srg_result[1]
#         to_serial_sb = dpt_srg_result[2]
#         self.dpt_sat(
#             stock_type=stock_type_sb,
#             from_serial=from_serial_sb,
#             to_serial=to_serial_sb,
#             assigned_staff_code=username_login
#         )
#         self.dpt_ccr(
#             stock_type=stock_type_sb,
#             from_serial=from_serial_sb,
#             to_serial=to_serial_sb,
#             approve_on_form='Y',
#             username=username_approve,
#             password=password_approve
#         )
#         self.dpt_sbi(
#             account_number=deposit_savings_close,
#             serial_no=from_serial_sb,
#             approve_on_form='Y',
#             username=username_approve,
#             password=password_approve
#         )
#         self.dpt_cls(
#             account_number=deposit_savings_close,
#         )
#         global deposit_savings_reject
#         dpt_opn_result = self.dpt_opn(
#             customer_code=customer_code_personal,
#             customer_type='Single customer',
#             catalogue_code=catalogue_code_savings,
#             reason_of_account_opening='Enter value reason of account opening'
#         )
#         deposit_savings_reject=dpt_opn_result[1]
#         self.dpt_rej(
#             account_number=deposit_savings_reject,
#         )

# # Create fixed deposit account - 01 month use for testing
#     def test_000_05_create_fixed_01m_deposit_account_use_for_testing(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         global deposit_fixed_01m_pending
#         dpt_opn_result = self.dpt_opn(
#             customer_code=customer_code_personal,
#             customer_type='Single customer',
#             catalogue_code=catalogue_code_fixed_01m,
#             reason_of_account_opening='Enter value reason of account opening'
#         )
#         deposit_fixed_01m_pending=dpt_opn_result[1]
#         global deposit_fixed_01m_new
#         dpt_opn_result = self.dpt_opn(
#             customer_code=customer_code_personal,
#             customer_type='Single customer',
#             catalogue_code=catalogue_code_fixed_01m,
#             reason_of_account_opening='Enter value reason of account opening'
#         )
#         deposit_fixed_01m_new=dpt_opn_result[1]
#         self.dpt_apr(
#             account_number=deposit_fixed_01m_new,
#             approve_on_form='Y',
#             username=username_approve,
#             password=password_approve
#         )
#         generated_number = self.gen_serial_number(stock_prefix_fb, stock_type_fb, 0)
#         print(f'generated_number new: {generated_number}')
#         from_serial = generated_number[0]
#         to_serial = generated_number[1]
#         dpt_srg_result = self.dpt_srg(
#             stock_type=stock_type_fb,
#             from_serial=from_serial,
#             to_serial=to_serial,
#             stock_prefix=stock_prefix_fb,
#             number_of_leaves=number_of_leaves_fb,
#             number_of_book=number_of_book_fb,
#             approve_on_form='Y',
#             username=username_approve,
#             password=password_approve
#         )
#         from_serial_fb = dpt_srg_result[1]
#         to_serial_fb = dpt_srg_result[2]
#         self.dpt_sat(
#             stock_type=stock_type_fb,
#             from_serial=from_serial_fb,
#             to_serial=to_serial_fb,
#             assigned_staff_code=username_login
#         )
#         self.dpt_ccr(
#             stock_type=stock_type_fb,
#             from_serial=from_serial_fb,
#             to_serial=to_serial_fb,
#             approve_on_form='Y',
#             username=username_approve,
#             password=password_approve
#         )
#         self.dpt_fbi(
#             account_number=deposit_fixed_01m_new,
#             serial_no=from_serial_fb,
#             approve_on_form='Y',
#             username=username_approve,
#             password=password_approve
#         )
#         global deposit_fixed_01m_normal
#         dpt_opn_result = self.dpt_opn(
#             customer_code=customer_code_personal,
#             customer_type='Single customer',
#             catalogue_code=catalogue_code_fixed_01m,
#             reason_of_account_opening='Enter value reason of account opening'
#         )
#         deposit_fixed_01m_normal=dpt_opn_result[1]
#         self.dpt_apr(
#             account_number=deposit_fixed_01m_normal,
#             approve_on_form='Y',
#             username=username_approve,
#             password=password_approve
#         )
#         self.dpt_cdp(
#             account_number=deposit_fixed_01m_normal,
#             amount_deposit=deposit_amount_fixed_01m,
#             approve_on_form='Y',
#             username=username_approve,
#             password=password_approve
#         )
#         generated_number = self.gen_serial_number(stock_prefix_fb, stock_type_fb, 0)
#         print(f'generated_number normal: {generated_number}')
#         from_serial = generated_number[0]
#         to_serial = generated_number[1]
#         dpt_srg_result = self.dpt_srg(
#             stock_type=stock_type_fb,
#             from_serial=from_serial,
#             to_serial=to_serial,
#             stock_prefix=stock_prefix_fb,
#             number_of_leaves=number_of_leaves_fb,
#             number_of_book=number_of_book_fb,
#             approve_on_form='Y',
#             username=username_approve,
#             password=password_approve
#         )
#         from_serial_fb = dpt_srg_result[1]
#         to_serial_fb = dpt_srg_result[2]
#         self.dpt_sat(
#             stock_type=stock_type_fb,
#             from_serial=from_serial_fb,
#             to_serial=to_serial_fb,
#             assigned_staff_code=username_login
#         )
#         self.dpt_ccr(
#             stock_type=stock_type_fb,
#             from_serial=from_serial_fb,
#             to_serial=to_serial_fb,
#             approve_on_form='Y',
#             username=username_approve,
#             password=password_approve
#         )
#         self.dpt_fbi(
#             account_number=deposit_fixed_01m_normal,
#             serial_no=from_serial_fb,
#             approve_on_form='Y',
#             username=username_approve,
#             password=password_approve
#         )
#         global deposit_fixed_01m_block
#         dpt_opn_result = self.dpt_opn(
#             customer_code=customer_code_personal,
#             customer_type='Single customer',
#             catalogue_code=catalogue_code_fixed_01m,
#             reason_of_account_opening='Enter value reason of account opening'
#         )
#         deposit_fixed_01m_block=dpt_opn_result[1]
#         self.dpt_apr(
#             account_number=deposit_fixed_01m_block,
#             approve_on_form='Y',
#             username=username_approve,
#             password=password_approve
#         )
#         self.dpt_cdp(
#             account_number=deposit_fixed_01m_block,
#             amount_deposit=deposit_amount_fixed_01m,
#             approve_on_form='Y',
#             username=username_approve,
#             password=password_approve
#         )
#         generated_number = self.gen_serial_number(stock_prefix_fb, stock_type_fb, 0)
#         print(f'generated_number block: {generated_number}')
#         from_serial = generated_number[0]
#         to_serial = generated_number[1]
#         dpt_srg_result = self.dpt_srg(
#             stock_type=stock_type_fb,
#             from_serial=from_serial,
#             to_serial=to_serial,
#             stock_prefix=stock_prefix_fb,
#             number_of_leaves=number_of_leaves_fb,
#             number_of_book=number_of_book_fb,
#             approve_on_form='Y',
#             username=username_approve,
#             password=password_approve
#         )
#         from_serial_fb = dpt_srg_result[1]
#         to_serial_fb = dpt_srg_result[2]
#         self.dpt_sat(
#             stock_type=stock_type_fb,
#             from_serial=from_serial_fb,
#             to_serial=to_serial_fb,
#             assigned_staff_code=username_login
#         )
#         self.dpt_ccr(
#             stock_type=stock_type_fb,
#             from_serial=from_serial_fb,
#             to_serial=to_serial_fb,
#             approve_on_form='Y',
#             username=username_approve,
#             password=password_approve
#         )
#         self.dpt_fbi(
#             account_number=deposit_fixed_01m_block,
#             serial_no=from_serial_fb,
#             approve_on_form='Y',
#             username=username_approve,
#             password=password_approve
#         )
#         self.dpt_blk(
#             account_number=deposit_fixed_01m_block,
#             approve_on_form='Y',
#             username=username_approve,
#             password=password_approve
#         )
#         global deposit_fixed_01m_close
#         dpt_opn_result = self.dpt_opn(
#             customer_code=customer_code_personal,
#             customer_type='Single customer',
#             catalogue_code=catalogue_code_fixed_01m,
#             reason_of_account_opening='Enter value reason of account opening'
#         )
#         deposit_fixed_01m_close=dpt_opn_result[1]
#         self.dpt_apr(
#             account_number=deposit_fixed_01m_close,
#             approve_on_form='Y',
#             username=username_approve,
#             password=password_approve
#         )
#         generated_number = self.gen_serial_number(stock_prefix_fb, stock_type_fb, 0)
#         print(f'generated_number close: {generated_number}')
#         from_serial = generated_number[0]
#         to_serial = generated_number[1]
#         dpt_srg_result = self.dpt_srg(
#             stock_type=stock_type_fb,
#             from_serial=from_serial,
#             to_serial=to_serial,
#             stock_prefix=stock_prefix_fb,
#             number_of_leaves=number_of_leaves_fb,
#             number_of_book=number_of_book_fb,
#             approve_on_form='Y',
#             username=username_approve,
#             password=password_approve
#         )
#         from_serial_fb = dpt_srg_result[1]
#         to_serial_fb = dpt_srg_result[2]
#         self.dpt_sat(
#             stock_type=stock_type_fb,
#             from_serial=from_serial_fb,
#             to_serial=to_serial_fb,
#             assigned_staff_code=username_login
#         )
#         self.dpt_ccr(
#             stock_type=stock_type_fb,
#             from_serial=from_serial_fb,
#             to_serial=to_serial_fb,
#             approve_on_form='Y',
#             username=username_approve,
#             password=password_approve
#         )
#         self.dpt_fbi(
#             account_number=deposit_fixed_01m_close,
#             serial_no=from_serial_fb,
#             approve_on_form='Y',
#             username=username_approve,
#             password=password_approve
#         )
#         self.dpt_cls(
#             account_number=deposit_fixed_01m_close,
#         )
#         global deposit_fixed_01m_reject
#         dpt_opn_result = self.dpt_opn(
#             customer_code=customer_code_personal,
#             customer_type='Single customer',
#             catalogue_code=catalogue_code_fixed_01m,
#             reason_of_account_opening='Enter value reason of account opening'
#         )
#         deposit_fixed_01m_reject=dpt_opn_result[1]
#         self.dpt_rej(
#             account_number=deposit_fixed_01m_reject,
#         )

# # Create other current deposit account use for testing
#     def test_000_06_create_other_current_deposit_account_use_for_testing(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         global other_current_deposit_account
#         dpt_opn_result = self.dpt_opn(
#             customer_code=customer_code_personal,
#             customer_type='Single customer',
#             catalogue_code=catalogue_code_current,
#             reason_of_account_opening='Enter value reason of account opening'
#         )
#         other_current_deposit_account=dpt_opn_result[1]
#         self.dpt_apr(
#             account_number=other_current_deposit_account,
#             approve_on_form='Y',
#             username=username_approve,
#             password=password_approve
#         )
#         self.dpt_cdp(
#             account_number=other_current_deposit_account,
#             amount_deposit=deposit_amount_current,
#             approve_on_form='Y',
#             username=username_approve,
#             password=password_approve
#         )

# # Create prepaid deposit account use for testing
#     def test_000_07_create_prepaid_deposit_account_use_for_testing(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         global deposit_prepaid_pending
#         dpt_opn_result = self.dpt_opn(
#             customer_code=customer_code_personal,
#             customer_type='Single customer',
#             catalogue_code=catalogue_code_prepaid,
#             reason_of_account_opening='Enter value reason of account opening',
#             to_account_number=other_current_deposit_account,
#         )
#         deposit_prepaid_pending=dpt_opn_result[1]
#         global deposit_prepaid_new
#         dpt_opn_result = self.dpt_opn(
#             customer_code=customer_code_personal,
#             customer_type='Single customer',
#             catalogue_code=catalogue_code_prepaid,
#             reason_of_account_opening='Enter value reason of account opening',
#             to_account_number=other_current_deposit_account,
#         )
#         deposit_prepaid_new=dpt_opn_result[1]
#         self.dpt_apr(
#             account_number=deposit_prepaid_new,
#             approve_on_form='Y',
#             username=username_approve,
#             password=password_approve
#         )
#         generated_number = self.gen_serial_number(stock_prefix_fr, stock_type_fr, 0)
#         print(f'generated_number new: {generated_number}')
#         from_serial = generated_number[0]
#         to_serial = generated_number[1]
#         dpt_srg_result = self.dpt_srg(
#             stock_type=stock_type_fr,
#             from_serial=from_serial,
#             to_serial=to_serial,
#             stock_prefix=stock_prefix_fr,
#             number_of_leaves=number_of_leaves_fr,
#             number_of_book=number_of_book_fr,
#             approve_on_form='Y',
#             username=username_approve,
#             password=password_approve
#         )
#         from_serial_fr = dpt_srg_result[1]
#         to_serial_fr = dpt_srg_result[2]
#         self.dpt_sat(
#             stock_type=stock_type_fr,
#             from_serial=from_serial_fr,
#             to_serial=to_serial_fr,
#             assigned_staff_code=username_login
#         )
#         self.dpt_ccr(
#             stock_type=stock_type_fr,
#             from_serial=from_serial_fr,
#             to_serial=to_serial_fr,
#             approve_on_form='Y',
#             username=username_approve,
#             password=password_approve
#         )
#         self.dpt_cer(
#             account_number=deposit_prepaid_new,
#             cerfiticate_serial=from_serial_fr,
#             approve_on_form='Y',
#             username=username_approve,
#             password=password_approve
#         )
#         global deposit_prepaid_normal
#         dpt_opn_result = self.dpt_opn(
#             customer_code=customer_code_personal,
#             customer_type='Single customer',
#             catalogue_code=catalogue_code_prepaid,
#             reason_of_account_opening='Enter value reason of account opening',
#             to_account_number=other_current_deposit_account,
#         )
#         deposit_prepaid_normal=dpt_opn_result[1]
#         self.dpt_apr(
#             account_number=deposit_prepaid_normal,
#             approve_on_form='Y',
#             username=username_approve,
#             password=password_approve
#         )
#         self.dpt_cdp(
#             account_number=deposit_prepaid_normal,
#             amount_deposit=deposit_amount_prepaid,
#             approve_on_form='Y',
#             username=username_approve,
#             password=password_approve
#         )
#         generated_number = self.gen_serial_number(stock_prefix_fr, stock_type_fr, 0)
#         print(f'generated_number normal: {generated_number}')
#         from_serial = generated_number[0]
#         to_serial = generated_number[1]
#         dpt_srg_result = self.dpt_srg(
#             stock_type=stock_type_fr,
#             from_serial=from_serial,
#             to_serial=to_serial,
#             stock_prefix=stock_prefix_fr,
#             number_of_leaves=number_of_leaves_fr,
#             number_of_book=number_of_book_fr,
#             approve_on_form='Y',
#             username=username_approve,
#             password=password_approve
#         )
#         from_serial_fr = dpt_srg_result[1]
#         to_serial_fr = dpt_srg_result[2]
#         self.dpt_sat(
#             stock_type=stock_type_fr,
#             from_serial=from_serial_fr,
#             to_serial=to_serial_fr,
#             assigned_staff_code=username_login
#         )
#         self.dpt_ccr(
#             stock_type=stock_type_fr,
#             from_serial=from_serial_fr,
#             to_serial=to_serial_fr,
#             approve_on_form='Y',
#             username=username_approve,
#             password=password_approve
#         )
#         self.dpt_cer(
#             account_number=deposit_prepaid_normal,
#             cerfiticate_serial=from_serial_fr,
#             approve_on_form='Y',
#             username=username_approve,
#             password=password_approve
#         )
#         global deposit_prepaid_block
#         dpt_opn_result = self.dpt_opn(
#             customer_code=customer_code_personal,
#             customer_type='Single customer',
#             catalogue_code=catalogue_code_prepaid,
#             reason_of_account_opening='Enter value reason of account opening',
#             to_account_number=other_current_deposit_account,
#         )
#         deposit_prepaid_block=dpt_opn_result[1]
#         self.dpt_apr(
#             account_number=deposit_prepaid_block,
#             approve_on_form='Y',
#             username=username_approve,
#             password=password_approve
#         )
#         self.dpt_cdp(
#             account_number=deposit_prepaid_block,
#             amount_deposit=deposit_amount_prepaid,
#             approve_on_form='Y',
#             username=username_approve,
#             password=password_approve
#         )
#         generated_number = self.gen_serial_number(stock_prefix_fr, stock_type_fr, 0)
#         print(f'generated_number block: {generated_number}')
#         from_serial = generated_number[0]
#         to_serial = generated_number[1]
#         dpt_srg_result = self.dpt_srg(
#             stock_type=stock_type_fr,
#             from_serial=from_serial,
#             to_serial=to_serial,
#             stock_prefix=stock_prefix_fr,
#             number_of_leaves=number_of_leaves_fr,
#             number_of_book=number_of_book_fr,
#             approve_on_form='Y',
#             username=username_approve,
#             password=password_approve
#         )
#         from_serial_fr = dpt_srg_result[1]
#         to_serial_fr = dpt_srg_result[2]
#         self.dpt_sat(
#             stock_type=stock_type_fr,
#             from_serial=from_serial_fr,
#             to_serial=to_serial_fr,
#             assigned_staff_code=username_login
#         )
#         self.dpt_ccr(
#             stock_type=stock_type_fr,
#             from_serial=from_serial_fr,
#             to_serial=to_serial_fr,
#             approve_on_form='Y',
#             username=username_approve,
#             password=password_approve
#         )
#         self.dpt_cer(
#             account_number=deposit_prepaid_block,
#             cerfiticate_serial=from_serial_fr,
#             approve_on_form='Y',
#             username=username_approve,
#             password=password_approve
#         )
#         self.dpt_blk(
#             account_number=deposit_prepaid_block,
#             approve_on_form='Y',
#             username=username_approve,
#             password=password_approve
#         )
#         global deposit_prepaid_close
#         dpt_opn_result = self.dpt_opn(
#             customer_code=customer_code_personal,
#             customer_type='Single customer',
#             catalogue_code=catalogue_code_prepaid,
#             reason_of_account_opening='Enter value reason of account opening',
#             to_account_number=other_current_deposit_account,
#         )
#         deposit_prepaid_close=dpt_opn_result[1]
#         self.dpt_apr(
#             account_number=deposit_prepaid_close,
#             approve_on_form='Y',
#             username=username_approve,
#             password=password_approve
#         )
#         generated_number = self.gen_serial_number(stock_prefix_fr, stock_type_fr, 0)
#         print(f'generated_number close: {generated_number}')
#         from_serial = generated_number[0]
#         to_serial = generated_number[1]
#         dpt_srg_result = self.dpt_srg(
#             stock_type=stock_type_fr,
#             from_serial=from_serial,
#             to_serial=to_serial,
#             stock_prefix=stock_prefix_fr,
#             number_of_leaves=number_of_leaves_fr,
#             number_of_book=number_of_book_fr,
#             approve_on_form='Y',
#             username=username_approve,
#             password=password_approve
#         )
#         from_serial_fr = dpt_srg_result[1]
#         to_serial_fr = dpt_srg_result[2]
#         self.dpt_sat(
#             stock_type=stock_type_fr,
#             from_serial=from_serial_fr,
#             to_serial=to_serial_fr,
#             assigned_staff_code=username_login
#         )
#         self.dpt_ccr(
#             stock_type=stock_type_fr,
#             from_serial=from_serial_fr,
#             to_serial=to_serial_fr,
#             approve_on_form='Y',
#             username=username_approve,
#             password=password_approve
#         )
#         self.dpt_cer(
#             account_number=deposit_prepaid_close,
#             cerfiticate_serial=from_serial_fr,
#             approve_on_form='Y',
#             username=username_approve,
#             password=password_approve
#         )
#         self.dpt_account_linkage_delete(
#             master_account_number=deposit_prepaid_close
#         )
#         self.dpt_cls(
#             account_number=deposit_prepaid_close,
#         )
#         global deposit_prepaid_reject
#         dpt_opn_result = self.dpt_opn(
#             customer_code=customer_code_personal,
#             customer_type='Single customer',
#             catalogue_code=catalogue_code_prepaid,
#             reason_of_account_opening='Enter value reason of account opening',
#             to_account_number=other_current_deposit_account,
#         )
#         deposit_prepaid_reject=dpt_opn_result[1]
#         self.dpt_rej(
#             account_number=deposit_prepaid_reject,
#         )

# # Create other savings deposit account use for testing
#     def test_000_08_create_other_savings_deposit_account_use_for_testing(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         global other_savings_deposit_account
#         dpt_opn_result = self.dpt_opn(
#             customer_code=customer_code_personal,
#             customer_type='Single customer',
#             catalogue_code=catalogue_code_bonus_savings,
#             reason_of_account_opening='Enter value reason of account opening'
#         )
#         other_savings_deposit_account=dpt_opn_result[1]
#         self.dpt_apr(
#             account_number=other_savings_deposit_account,
#             approve_on_form='Y',
#             username=username_approve,
#             password=password_approve
#         )
#         self.dpt_cdp(
#             account_number=other_savings_deposit_account,
#             amount_deposit=deposit_amount_bonus_savings,
#             approve_on_form='Y',
#             username=username_approve,
#             password=password_approve
#         )

# # DPT_CSH - INVALID CASE
#     def test_001_dpt_csh_01_check_not_allowed_deposit_type_fixed_deposit(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             f'InvalidDpttype: Invalid deposit type of account [{self.no_mask(deposit_fixed_01m_normal)}]- en'
#         ]
#         self.dpt_csh(
#             account_number_debit=deposit_fixed_01m_normal,
#             enter_side='D',
#             debit_amount=amount_fixed_01m_valid,
#             list_error_message=list_error_message,
#         )

#     def test_001_dpt_csh_02_check_not_allowed_deposit_type_prepaid(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             f'InvalidDpttype: Invalid deposit type of account [{self.no_mask(deposit_prepaid_normal)}]- en'
#         ]
#         self.dpt_csh(
#             account_number_debit=deposit_prepaid_normal,
#             enter_side='D',
#             debit_amount=amount_prepaid_valid,
#             list_error_message=list_error_message,
#         )

#     def test_001_dpt_csh_03_check_not_allowed_deposit_status_block(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             f'InvalidDepositStatus: Invalid deposit status [{status_block}]'
#         ]
#         self.dpt_csh(
#             account_number_debit=deposit_current_block,
#             enter_side='D',
#             debit_amount=amount_current_valid,
#             list_error_message=list_error_message,
#         )
#         self.dpt_csh(
#             account_number_debit=deposit_savings_block,
#             enter_side='D',
#             debit_amount=amount_current_valid,
#             list_error_message=list_error_message,
#         )

#     def test_001_dpt_csh_04_check_not_allowed_deposit_status_closed(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             f'InvalidDepositStatus: Invalid deposit status [{status_closed}]'
#         ]
#         self.dpt_csh(
#             account_number_debit=deposit_current_close,
#             enter_side='D',
#             debit_amount=amount_current_valid,
#             list_error_message=list_error_message,
#         )
#         self.dpt_csh(
#             account_number_debit=deposit_savings_close,
#             enter_side='D',
#             debit_amount=amount_current_valid,
#             list_error_message=list_error_message,
#         )

#     def test_001_dpt_csh_05_check_not_allowed_deposit_status_pending(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             f'InvalidDepositStatus: Invalid deposit status [{status_pending}]'
#         ]
#         self.dpt_csh(
#             account_number_debit=deposit_current_pending,
#             enter_side='D',
#             debit_amount=amount_current_valid,
#             list_error_message=list_error_message,
#         )
#         self.dpt_csh(
#             account_number_debit=deposit_savings_pending,
#             enter_side='D',
#             debit_amount=amount_current_valid,
#             list_error_message=list_error_message,
#         )

#     def test_001_dpt_csh_06_check_not_allowed_deposit_status_reject(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             f'InvalidDepositStatus: Invalid deposit status [{status_reject}]'
#         ]
#         self.dpt_csh(
#             account_number_debit=deposit_current_reject,
#             enter_side='D',
#             debit_amount=amount_current_valid,
#             list_error_message=list_error_message,
#         )
#         self.dpt_csh(
#             account_number_debit=deposit_savings_reject,
#             enter_side='D',
#             debit_amount=amount_current_valid,
#             list_error_message=list_error_message,
#         )

#     def test_001_dpt_csh_07_check_not_allowed_deposit_status_new(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             f'InvalidDepositStatus: Invalid deposit status [{status_new}]'
#         ]
#         self.dpt_csh(
#             account_number_debit=deposit_current_new,
#             enter_side='D',
#             debit_amount=amount_current_valid,
#             list_error_message=list_error_message,
#         )
#         self.dpt_csh(
#             account_number_debit=deposit_savings_new,
#             enter_side='D',
#             debit_amount=amount_current_valid,
#             list_error_message=list_error_message,
#         )

#     def test_001_dpt_csh_08_check_not_allowed_deposit_status_dormant(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             f'InvalidDepositStatus: Invalid deposit status [{status_dormant}]'
#         ]
#         self.dpt_csh(
#             account_number_debit=deposit_current_dormant,
#             enter_side='D',
#             debit_amount=amount_current_valid,
#             list_error_message=list_error_message,
#         )
#         self.dpt_csh(
#             account_number_debit=deposit_savings_dormant,
#             enter_side='D',
#             debit_amount=amount_current_valid,
#             list_error_message=list_error_message,
#         )

#     def test_001_dpt_csh_09_check_available_balance_no_fee_invalid_current(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             f'InvalidAvailableAmt: Invalid available balance of account [{self.no_mask(deposit_current_normal)}]. Available balance must be more than [{self.format_number(amount_current_invalid)}] - en'
#         ]
#         self.dpt_csh(
#             account_number_debit=deposit_current_normal,
#             enter_side='D',
#             debit_amount=amount_current_invalid,
#             list_error_message=list_error_message,
#         )

#     def test_001_dpt_csh_10_check_available_balance_no_fee_invalid_savings(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             f'InvalidAvailableAmt: Invalid available balance of account [{self.no_mask(deposit_savings_normal)}]. Available balance must be more than [{self.format_number(amount_savings_invalid)}] - en'
#         ]
#         self.dpt_csh(
#             account_number_debit=deposit_savings_normal,
#             enter_side='D',
#             debit_amount=amount_savings_invalid,
#             list_error_message=list_error_message,
#         )

# # DPT_DPT (Debit account) - INVALID CASE
#     def test_002_dpt_dpt_01_debit_check_not_allowed_deposit_type_fixed_deposit(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             f'InvalidDpttype: Invalid deposit type of account [{self.no_mask(deposit_fixed_01m_normal)}]- en'
#         ]
#         self.dpt_dpt(
#             account_number_debit=deposit_fixed_01m_normal,
#             account_number_credit=deposit_current_normal,
#             enter_side='D',
#             debit_amount=amount_fixed_01m_valid,
#             list_error_message=list_error_message,
#         )
#         self.dpt_dpt(
#             account_number_debit=deposit_fixed_01m_normal,
#             account_number_credit=deposit_savings_normal,
#             enter_side='D',
#             debit_amount=amount_fixed_01m_valid,
#             list_error_message=list_error_message,
#         )

#     def test_002_dpt_dpt_02_debit_check_not_allowed_deposit_type_prepaid(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             f'InvalidDpttype: Invalid deposit type of account [{self.no_mask(deposit_prepaid_normal)}]- en'
#         ]
#         self.dpt_dpt(
#             account_number_debit=deposit_prepaid_normal,
#             account_number_credit=deposit_current_normal,
#             enter_side='D',
#             debit_amount=amount_prepaid_valid,
#             list_error_message=list_error_message,
#         )
#         self.dpt_dpt(
#             account_number_debit=deposit_prepaid_normal,
#             account_number_credit=deposit_savings_normal,
#             enter_side='D',
#             debit_amount=amount_prepaid_valid,
#             list_error_message=list_error_message,
#         )

#     def test_002_dpt_dpt_03_debit_check_not_allowed_deposit_status_block(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             f'InvalidDepositStatus: Invalid deposit status [{status_block}]'
#         ]
#         self.dpt_dpt(
#             account_number_debit=deposit_current_block,
#             account_number_credit=deposit_savings_normal,
#             enter_side='D',
#             debit_amount=amount_current_valid,
#             list_error_message=list_error_message,
#         )
#         self.dpt_dpt(
#             account_number_debit=deposit_current_block,
#             account_number_credit=deposit_current_normal,
#             enter_side='D',
#             debit_amount=amount_current_valid,
#             list_error_message=list_error_message,
#         )
#         self.dpt_dpt(
#             account_number_debit=deposit_savings_block,
#             account_number_credit=deposit_savings_normal,
#             enter_side='D',
#             debit_amount=amount_current_valid,
#             list_error_message=list_error_message,
#         )
#         self.dpt_dpt(
#             account_number_debit=deposit_savings_block,
#             account_number_credit=deposit_current_normal,
#             enter_side='D',
#             debit_amount=amount_current_valid,
#             list_error_message=list_error_message,
#         )

#     def test_002_dpt_dpt_04_debit_check_not_allowed_deposit_status_closed(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             f'InvalidDepositStatus: Invalid deposit status [{status_closed}]'
#         ]
#         self.dpt_dpt(
#             account_number_debit=deposit_current_close,
#             account_number_credit=deposit_current_normal,
#             enter_side='D',
#             debit_amount=amount_current_valid,
#             list_error_message=list_error_message,
#         )
#         self.dpt_dpt(
#             account_number_debit=deposit_savings_close,
#             account_number_credit=deposit_current_normal,
#             enter_side='D',
#             debit_amount=amount_current_valid,
#             list_error_message=list_error_message,
#         )

#     def test_002_dpt_dpt_05_debit_check_not_allowed_deposit_status_pending(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             f'InvalidDepositStatus: Invalid deposit status [{status_pending}]'
#         ]
#         self.dpt_dpt(
#             account_number_debit=deposit_current_pending,
#             account_number_credit=deposit_savings_normal,
#             enter_side='D',
#             debit_amount=amount_current_valid,
#             list_error_message=list_error_message,
#         )
#         self.dpt_dpt(
#             account_number_debit=deposit_savings_pending,
#             account_number_credit=deposit_savings_normal,
#             enter_side='D',
#             debit_amount=amount_current_valid,
#             list_error_message=list_error_message,
#         )

#     def test_002_dpt_dpt_06_debit_check_not_allowed_deposit_status_reject(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             f'InvalidDepositStatus: Invalid deposit status [{status_reject}]'
#         ]
#         self.dpt_dpt(
#             account_number_debit=deposit_current_reject,
#             account_number_credit=deposit_current_normal,
#             enter_side='D',
#             debit_amount=amount_current_valid,
#             list_error_message=list_error_message,
#         )
#         self.dpt_dpt(
#             account_number_debit=deposit_savings_reject,
#             account_number_credit=deposit_current_normal,
#             enter_side='D',
#             debit_amount=amount_current_valid,
#             list_error_message=list_error_message,
#         )

#     def test_002_dpt_dpt_07_debit_check_not_allowed_deposit_status_new(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             f'InvalidDepositStatus: Invalid deposit status [{status_new}]'
#         ]
#         self.dpt_dpt(
#             account_number_debit=deposit_current_new,
#             account_number_credit=deposit_savings_normal,
#             enter_side='D',
#             debit_amount=amount_current_valid,
#             list_error_message=list_error_message,
#         )
#         self.dpt_dpt(
#             account_number_debit=deposit_savings_new,
#             account_number_credit=deposit_savings_normal,
#             enter_side='D',
#             debit_amount=amount_current_valid,
#             list_error_message=list_error_message,
#         )

#     def test_002_dpt_dpt_08_debit_check_not_allowed_deposit_status_dormant(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             f'InvalidDepositStatus: Invalid deposit status [{status_dormant}]'
#         ]
#         self.dpt_dpt(
#             account_number_debit=deposit_current_dormant,
#             account_number_credit=deposit_current_normal,
#             enter_side='D',
#             debit_amount=amount_current_valid,
#             list_error_message=list_error_message,
#         )
#         self.dpt_dpt(
#             account_number_debit=deposit_savings_dormant,
#             account_number_credit=deposit_current_normal,
#             enter_side='D',
#             debit_amount=amount_current_valid,
#             list_error_message=list_error_message,
#         )

#     def test_002_dpt_dpt_09_debit_check_available_balance_no_fee_invalid_current(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             f'InvalidAvailableAmt: Invalid available balance of account [{self.no_mask(deposit_current_normal)}]. Available balance must be more than [{self.format_number(amount_current_invalid)}] - en'
#         ]
#         self.dpt_dpt(
#             account_number_debit=deposit_current_normal,
#             account_number_credit=deposit_current_normal,
#             enter_side='D',
#             debit_amount=amount_current_invalid,
#             list_error_message=list_error_message,
#         )

#     def test_002_dpt_dpt_10_debit_check_available_balance_no_fee_invalid_savings(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             f'InvalidAvailableAmt: Invalid available balance of account [{self.no_mask(deposit_savings_normal)}]. Available balance must be more than [{self.format_number(amount_savings_invalid)}] - en'
#         ]
#         self.dpt_dpt(
#             account_number_debit=deposit_savings_normal,
#             account_number_credit=deposit_current_normal,
#             enter_side='D',
#             debit_amount=amount_savings_invalid,
#             list_error_message=list_error_message,
#         )

# # DPT_DPT (Credit account) - INVALID CASE
#     def test_002_dpt_dpt_11_credit_check_not_allowed_deposit_type_fixed_deposit(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             f'InvalidDpttype: Invalid deposit type of account [{self.no_mask(deposit_fixed_01m_normal)}]- en'
#         ]
#         self.dpt_dpt(
#             account_number_debit=deposit_current_normal,
#             account_number_credit=deposit_fixed_01m_normal,
#             enter_side='C',
#             credit_amount=amount_fixed_01m_valid,
#             list_error_message=list_error_message,
#         )
#         self.dpt_dpt(
#             account_number_debit=deposit_savings_normal,
#             account_number_credit=deposit_fixed_01m_normal,
#             enter_side='C',
#             credit_amount=amount_fixed_01m_valid,
#             list_error_message=list_error_message,
#         )

#     def test_002_dpt_dpt_12_credit_check_not_allowed_deposit_type_prepaid(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             f'InvalidDpttype: Invalid deposit type of account [{self.no_mask(deposit_prepaid_normal)}]- en'
#         ]
#         self.dpt_dpt(
#             account_number_debit=deposit_current_normal,
#             account_number_credit=deposit_prepaid_normal,
#             enter_side='C',
#             credit_amount=amount_prepaid_valid,
#             list_error_message=list_error_message,
#         )
#         self.dpt_dpt(
#             account_number_debit=deposit_savings_normal,
#             account_number_credit=deposit_prepaid_normal,
#             enter_side='C',
#             credit_amount=amount_prepaid_valid,
#             list_error_message=list_error_message,
#         )

#     def test_002_dpt_dpt_13_credit_check_not_allowed_deposit_status_block(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             f'InvalidDepositStatus: Invalid deposit status [{status_block}]'
#         ]
#         self.dpt_dpt(
#             account_number_debit=deposit_savings_normal,
#             account_number_credit=deposit_current_block,
#             enter_side='C',
#             credit_amount=amount_current_valid,
#             list_error_message=list_error_message,
#         )
#         self.dpt_dpt(
#             account_number_debit=deposit_current_normal,
#             account_number_credit=deposit_current_block,
#             enter_side='C',
#             credit_amount=amount_current_valid,
#             list_error_message=list_error_message,
#         )
#         self.dpt_dpt(
#             account_number_debit=deposit_savings_normal,
#             account_number_credit=deposit_savings_block,
#             enter_side='C',
#             credit_amount=amount_current_valid,
#             list_error_message=list_error_message,
#         )
#         self.dpt_dpt(
#             account_number_debit=deposit_current_normal,
#             account_number_credit=deposit_savings_block,
#             enter_side='C',
#             credit_amount=amount_current_valid,
#             list_error_message=list_error_message,
#         )

#     def test_002_dpt_dpt_14_credit_check_not_allowed_deposit_status_closed(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             f'InvalidDepositStatus: Invalid deposit status [{status_closed}]'
#         ]
#         self.dpt_dpt(
#             account_number_debit=deposit_current_normal,
#             account_number_credit=deposit_current_close,
#             enter_side='C',
#             credit_amount=amount_current_valid,
#             list_error_message=list_error_message,
#         )
#         self.dpt_dpt(
#             account_number_debit=deposit_current_normal,
#             account_number_credit=deposit_savings_close,
#             enter_side='C',
#             credit_amount=amount_current_valid,
#             list_error_message=list_error_message,
#         )

#     def test_002_dpt_dpt_15_credit_check_not_allowed_deposit_status_pending(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             f'InvalidDepositStatus: Invalid deposit status [{status_pending}]'
#         ]
#         self.dpt_dpt(
#             account_number_debit=deposit_savings_normal,
#             account_number_credit=deposit_current_pending,
#             enter_side='C',
#             credit_amount=amount_current_valid,
#             list_error_message=list_error_message,
#         )
#         self.dpt_dpt(
#             account_number_debit=deposit_savings_normal,
#             account_number_credit=deposit_savings_pending,
#             enter_side='C',
#             credit_amount=amount_current_valid,
#             list_error_message=list_error_message,
#         )

#     def test_002_dpt_dpt_16_credit_check_not_allowed_deposit_status_reject(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             f'InvalidDepositStatus: Invalid deposit status [{status_reject}]'
#         ]
#         self.dpt_dpt(
#             account_number_debit=deposit_current_normal,
#             account_number_credit=deposit_current_reject,
#             enter_side='C',
#             credit_amount=amount_current_valid,
#             list_error_message=list_error_message,
#         )
#         self.dpt_dpt(
#             account_number_debit=deposit_current_normal,
#             account_number_credit=deposit_savings_reject,
#             enter_side='C',
#             credit_amount=amount_current_valid,
#             list_error_message=list_error_message,
#         )

#     def test_002_dpt_dpt_17_credit_check_not_allowed_deposit_status_new(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             f'InvalidDepositStatus: Invalid deposit status [{status_new}]'
#         ]
#         self.dpt_dpt(
#             account_number_debit=deposit_savings_normal,
#             account_number_credit=deposit_current_new,
#             enter_side='C',
#             credit_amount=amount_current_valid,
#             list_error_message=list_error_message,
#         )
#         self.dpt_dpt(
#             account_number_debit=deposit_savings_normal,
#             account_number_credit=deposit_savings_new,
#             enter_side='C',
#             credit_amount=amount_current_valid,
#             list_error_message=list_error_message,
#         )

#     def test_002_dpt_dpt_18_credit_check_not_allowed_deposit_status_dormant(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             f'InvalidDepositStatus: Invalid deposit status [{status_dormant}]'
#         ]
#         self.dpt_dpt(
#             account_number_debit=deposit_current_normal,
#             account_number_credit=deposit_current_dormant,
#             enter_side='C',
#             credit_amount=amount_current_valid,
#             list_error_message=list_error_message,
#         )
#         self.dpt_dpt(
#             account_number_debit=deposit_current_normal,
#             account_number_credit=deposit_savings_dormant,
#             enter_side='C',
#             credit_amount=amount_current_valid,
#             list_error_message=list_error_message,
#         )

# # DPT_ACT - INVALID CASE
#     def test_003_dpt_act_01_check_not_allowed_deposit_type_fixed_deposit(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             f'InvalidDpttype: Invalid deposit type of account [{self.no_mask(deposit_fixed_01m_normal)}]- en'
#         ]
#         self.dpt_act(
#             account_number_debit=deposit_fixed_01m_normal,
#             account_number_credit=gl_account_number,
#             enter_side='D',
#             debit_amount=amount_fixed_01m_valid,
#             list_error_message=list_error_message,
#         )
#         self.dpt_act(
#             account_number_debit=deposit_fixed_01m_normal,
#             account_number_credit=gl_account_number,
#             enter_side='D',
#             debit_amount=amount_fixed_01m_valid,
#             list_error_message=list_error_message,
#         )

#     def test_003_dpt_act_02_check_not_allowed_deposit_type_prepaid(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             f'InvalidDpttype: Invalid deposit type of account [{self.no_mask(deposit_prepaid_normal)}]- en'
#         ]
#         self.dpt_act(
#             account_number_debit=deposit_prepaid_normal,
#             account_number_credit=gl_account_number,
#             enter_side='D',
#             debit_amount=amount_prepaid_valid,
#             list_error_message=list_error_message,
#         )
#         self.dpt_act(
#             account_number_debit=deposit_prepaid_normal,
#             account_number_credit=gl_account_number,
#             enter_side='D',
#             debit_amount=amount_prepaid_valid,
#             list_error_message=list_error_message,
#         )

#     def test_003_dpt_act_03_check_not_allowed_deposit_status_block(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             f'InvalidDepositStatus: Invalid deposit status [{status_block}]'
#         ]
#         self.dpt_act(
#             account_number_debit=deposit_current_block,
#             account_number_credit=gl_account_number,
#             enter_side='D',
#             debit_amount=amount_current_valid,
#             list_error_message=list_error_message,
#         )
#         self.dpt_act(
#             account_number_debit=deposit_current_block,
#             account_number_credit=gl_account_number,
#             enter_side='D',
#             debit_amount=amount_current_valid,
#             list_error_message=list_error_message,
#         )
#         self.dpt_act(
#             account_number_debit=deposit_savings_block,
#             account_number_credit=gl_account_number,
#             enter_side='D',
#             debit_amount=amount_current_valid,
#             list_error_message=list_error_message,
#         )
#         self.dpt_act(
#             account_number_debit=deposit_savings_block,
#             account_number_credit=gl_account_number,
#             enter_side='D',
#             debit_amount=amount_current_valid,
#             list_error_message=list_error_message,
#         )

#     def test_003_dpt_act_04_check_not_allowed_deposit_status_closed(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             f'InvalidDepositStatus: Invalid deposit status [{status_closed}]'
#         ]
#         self.dpt_act(
#             account_number_debit=deposit_current_close,
#             account_number_credit=gl_account_number,
#             enter_side='D',
#             debit_amount=amount_current_valid,
#             list_error_message=list_error_message,
#         )
#         self.dpt_act(
#             account_number_debit=deposit_savings_close,
#             account_number_credit=gl_account_number,
#             enter_side='D',
#             debit_amount=amount_current_valid,
#             list_error_message=list_error_message,
#         )

#     def test_003_dpt_act_05_check_not_allowed_deposit_status_pending(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             f'InvalidDepositStatus: Invalid deposit status [{status_pending}]'
#         ]
#         self.dpt_act(
#             account_number_debit=deposit_current_pending,
#             account_number_credit=gl_account_number,
#             enter_side='D',
#             debit_amount=amount_current_valid,
#             list_error_message=list_error_message,
#         )
#         self.dpt_act(
#             account_number_debit=deposit_savings_pending,
#             account_number_credit=gl_account_number,
#             enter_side='D',
#             debit_amount=amount_current_valid,
#             list_error_message=list_error_message,
#         )

#     def test_003_dpt_act_06_check_not_allowed_deposit_status_reject(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             f'InvalidDepositStatus: Invalid deposit status [{status_reject}]'
#         ]
#         self.dpt_act(
#             account_number_debit=deposit_current_reject,
#             account_number_credit=gl_account_number,
#             enter_side='D',
#             debit_amount=amount_current_valid,
#             list_error_message=list_error_message,
#         )
#         self.dpt_act(
#             account_number_debit=deposit_savings_reject,
#             account_number_credit=gl_account_number,
#             enter_side='D',
#             debit_amount=amount_current_valid,
#             list_error_message=list_error_message,
#         )

#     def test_003_dpt_act_07_check_not_allowed_deposit_status_new(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             f'InvalidDepositStatus: Invalid deposit status [{status_new}]'
#         ]
#         self.dpt_act(
#             account_number_debit=deposit_current_new,
#             account_number_credit=gl_account_number,
#             enter_side='D',
#             debit_amount=amount_current_valid,
#             list_error_message=list_error_message,
#         )
#         self.dpt_act(
#             account_number_debit=deposit_savings_new,
#             account_number_credit=gl_account_number,
#             enter_side='D',
#             debit_amount=amount_current_valid,
#             list_error_message=list_error_message,
#         )

#     def test_003_dpt_act_08_check_not_allowed_deposit_status_dormant(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             f'InvalidDepositStatus: Invalid deposit status [{status_dormant}]'
#         ]
#         self.dpt_act(
#             account_number_debit=deposit_current_dormant,
#             account_number_credit=gl_account_number,
#             enter_side='D',
#             debit_amount=amount_current_valid,
#             list_error_message=list_error_message,
#         )
#         self.dpt_act(
#             account_number_debit=deposit_savings_dormant,
#             account_number_credit=gl_account_number,
#             enter_side='D',
#             debit_amount=amount_current_valid,
#             list_error_message=list_error_message,
#         )

#     def test_003_dpt_act_09_check_available_balance_no_fee_invalid_current(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             f'InvalidAvailableAmt: Invalid available balance of account [{self.no_mask(deposit_current_normal)}]. Available balance must be more than [{self.format_number(amount_current_invalid)}] - en'
#         ]
#         self.dpt_act(
#             account_number_debit=deposit_current_normal,
#             account_number_credit=gl_account_number,
#             enter_side='D',
#             debit_amount=amount_current_invalid,
#             list_error_message=list_error_message,
#         )

#     def test_003_dpt_act_10_check_available_balance_no_fee_invalid_savings(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             f'InvalidAvailableAmt: Invalid available balance of account [{self.no_mask(deposit_savings_normal)}]. Available balance must be more than [{self.format_number(amount_savings_invalid)}] - en'
#         ]
#         self.dpt_act(
#             account_number_debit=deposit_savings_normal,
#             account_number_credit=gl_account_number,
#             enter_side='D',
#             debit_amount=amount_savings_invalid,
#             list_error_message=list_error_message,
#         )

# # DPT_CWR - INVALID CASE
#     def test_004_dpt_cwr_01_check_not_allowed_deposit_type_current(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             'Passbook number: Can not be blank'
#         ]
#         self.dpt_cwr(
#             account_number=deposit_current_normal,
#             withdraw_amount=amount_current_valid,
#             list_error_message=list_error_message
#         )

#     def test_004_dpt_cwr_02_check_not_allowed_deposit_type_fixed_deposit(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             'Passbook number: Can not be blank'
#         ]
#         self.dpt_cwr(
#             account_number=deposit_fixed_01m_normal,
#             withdraw_amount=amount_fixed_01m_valid,
#             list_error_message=list_error_message
#         )

#     def test_004_dpt_cwr_03_check_not_allowed_deposit_type_prepaid(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             'Passbook number: Can not be blank'
#         ]
#         self.dpt_cwr(
#             account_number=deposit_prepaid_normal,
#             withdraw_amount=amount_prepaid_valid,
#             list_error_message=list_error_message
#         )

#     def test_004_dpt_cwr_04_check_not_allowed_deposit_status_block(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             f'InvalidDepositStatus: Invalid deposit status [{status_block}]'
#         ]
#         self.dpt_cwr(
#             account_number=deposit_savings_block,
#             withdraw_amount=amount_savings_valid,
#             list_error_message=list_error_message
#         )

#     def test_004_dpt_cwr_05_check_not_allowed_deposit_status_closed(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             f'InvalidDepositStatus: Invalid deposit status [{status_closed}]'
#         ]
#         self.dpt_cwr(
#             account_number=deposit_savings_close,
#             withdraw_amount=amount_savings_valid,
#             list_error_message=list_error_message
#         )

#     def test_004_dpt_cwr_06_check_not_allowed_deposit_status_reject(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             'Passbook number: Can not be blank'
#         ]
#         self.dpt_cwr(
#             account_number=deposit_savings_reject,
#             withdraw_amount=amount_savings_valid,
#             list_error_message=list_error_message
#         )

#     def test_004_dpt_cwr_07_check_available_balance_no_fee_invalid_savings_pending(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             'Passbook number: Can not be blank'
#         ]
#         self.dpt_cwr(
#             account_number=deposit_savings_pending,
#             withdraw_amount=amount_savings_valid,
#             list_error_message=list_error_message
#         )

#     def test_004_dpt_cwr_08_check_available_balance_no_fee_invalid_savings_new(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             f'InvalidAvailableAmt: Invalid available balance of account [{self.no_mask(deposit_savings_new)}]. Available balance must be more than [{self.format_number(amount_savings_valid)}] - en'
#         ]
#         self.dpt_cwr(
#             account_number=deposit_savings_new,
#             withdraw_amount=amount_savings_valid,
#             list_error_message=list_error_message
#         )

#     def test_004_dpt_cwr_09_check_available_balance_no_fee_invalid_savings_normal(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             f'InvalidAvailableAmt: Invalid available balance of account [{self.no_mask(deposit_savings_normal)}]. Available balance must be more than [{self.format_number(amount_savings_invalid)}] - en'
#         ]
#         self.dpt_cwr(
#             account_number=deposit_savings_normal,
#             withdraw_amount=amount_savings_invalid,
#             list_error_message=list_error_message
#         )

# # DPT_MWR - INVALID CASE
#     def test_005_dpt_mwr_01_check_not_allowed_deposit_type_fixed_deposit(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             f'InvalidDpttype: Invalid deposit type of account [{self.no_mask(deposit_fixed_01m_normal)}]- en'
#         ]
#         self.dpt_mwr(
#             account_number=deposit_fixed_01m_normal,
#             withdraw_amount=amount_fixed_01m_valid,
#             credit_accounting=gl_account_number,
#             list_error_message=list_error_message,
#         )

#     def test_005_dpt_mwr_02_check_not_allowed_deposit_type_prepaid(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             f'InvalidDpttype: Invalid deposit type of account [{self.no_mask(deposit_prepaid_normal)}]- en'
#         ]
#         self.dpt_mwr(
#             account_number=deposit_prepaid_normal,
#             withdraw_amount=amount_prepaid_valid,
#             credit_accounting=gl_account_number,
#             list_error_message=list_error_message,
#         )

#     def test_005_dpt_mwr_03_check_not_allowed_deposit_status_current_block(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             f'InvalidDepositStatus: Invalid deposit status [{status_block}]'
#         ]
#         self.dpt_mwr(
#             account_number=deposit_current_block,
#             withdraw_amount=amount_current_valid,
#             credit_accounting=gl_account_number,
#             list_error_message=list_error_message,
#         )

#     def test_005_dpt_mwr_04_check_not_allowed_deposit_status_savings_block(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             f'InvalidDepositStatus: Invalid deposit status [{status_block}]'
#         ]
#         self.dpt_mwr(
#             account_number=deposit_savings_block,
#             withdraw_amount=amount_savings_valid,
#             credit_accounting=gl_account_number,
#             list_error_message=list_error_message,
#         )

#     def test_005_dpt_mwr_05_check_available_balance_no_fee_invalid_current_closed(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             f'InvalidAvailableAmt: Invalid available balance of account [{self.no_mask(deposit_current_close)}]. Available balance must be more than [{self.format_number(amount_current_valid)}] - en'
#         ]
#         self.dpt_mwr(
#             account_number=deposit_current_close,
#             withdraw_amount=amount_current_valid,
#             credit_accounting=gl_account_number,
#             list_error_message=list_error_message,
#         )

#     def test_005_dpt_mwr_06_check_available_balance_no_fee_invalid_current_reject(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             f'InvalidAvailableAmt: Invalid available balance of account [{self.no_mask(deposit_current_reject)}]. Available balance must be more than [{self.format_number(amount_current_valid)}] - en'
#         ]
#         self.dpt_mwr(
#             account_number=deposit_current_reject,
#             withdraw_amount=amount_current_valid,
#             credit_accounting=gl_account_number,
#             list_error_message=list_error_message,
#         )

#     def test_005_dpt_mwr_07_check_available_balance_no_fee_invalid_current_pending(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             f'InvalidAvailableAmt: Invalid available balance of account [{self.no_mask(deposit_current_pending)}]. Available balance must be more than [{self.format_number(amount_current_valid)}] - en'
#         ]
#         self.dpt_mwr(
#             account_number=deposit_current_pending,
#             withdraw_amount=amount_current_valid,
#             credit_accounting=gl_account_number,
#             list_error_message=list_error_message,
#         )

#     def test_005_dpt_mwr_08_check_available_balance_no_fee_invalid_current_new(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             f'InvalidAvailableAmt: Invalid available balance of account [{self.no_mask(deposit_current_new)}]. Available balance must be more than [{self.format_number(amount_current_valid)}] - en'
#         ]
#         self.dpt_mwr(
#             account_number=deposit_current_new,
#             withdraw_amount=amount_current_valid,
#             credit_accounting=gl_account_number,
#             list_error_message=list_error_message,
#         )

#     def test_005_dpt_mwr_09_check_available_balance_no_fee_invalid_current_normal(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             f'InvalidAvailableAmt: Invalid available balance of account [{self.no_mask(deposit_current_normal)}]. Available balance must be more than [{self.format_number(amount_current_invalid)}] - en'
#         ]
#         self.dpt_mwr(
#             account_number=deposit_current_normal,
#             withdraw_amount=amount_current_invalid,
#             credit_accounting=gl_account_number,
#             list_error_message=list_error_message,
#         )

#     def test_005_dpt_mwr_10_check_available_balance_no_fee_invalid_savings_closed(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             f'InvalidAvailableAmt: Invalid available balance of account [{self.no_mask(deposit_savings_close)}]. Available balance must be more than [{self.format_number(amount_savings_valid)}] - en'
#         ]
#         self.dpt_mwr(
#             account_number=deposit_savings_close,
#             withdraw_amount=amount_savings_valid,
#             credit_accounting=gl_account_number,
#             list_error_message=list_error_message,
#         )

#     def test_005_dpt_mwr_11_check_available_balance_no_fee_invalid_savings_reject(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             f'InvalidAvailableAmt: Invalid available balance of account [{self.no_mask(deposit_savings_reject)}]. Available balance must be more than [{self.format_number(amount_savings_valid)}] - en'
#         ]
#         self.dpt_mwr(
#             account_number=deposit_savings_reject,
#             withdraw_amount=amount_savings_valid,
#             credit_accounting=gl_account_number,
#             list_error_message=list_error_message,
#         )

#     def test_005_dpt_mwr_12_check_available_balance_no_fee_invalid_savings_pending(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             f'InvalidAvailableAmt: Invalid available balance of account [{self.no_mask(deposit_savings_pending)}]. Available balance must be more than [{self.format_number(amount_savings_valid)}] - en'
#         ]
#         self.dpt_mwr(
#             account_number=deposit_savings_pending,
#             withdraw_amount=amount_savings_valid,
#             credit_accounting=gl_account_number,
#             list_error_message=list_error_message,
#         )

#     def test_005_dpt_mwr_13_check_available_balance_no_fee_invalid_savings_new(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             f'InvalidAvailableAmt: Invalid available balance of account [{self.no_mask(deposit_savings_new)}]. Available balance must be more than [{self.format_number(amount_savings_valid)}] - en'
#         ]
#         self.dpt_mwr(
#             account_number=deposit_savings_new,
#             withdraw_amount=amount_savings_valid,
#             credit_accounting=gl_account_number,
#             list_error_message=list_error_message,
#         )

#     def test_005_dpt_mwr_14_check_available_balance_no_fee_invalid_savings_normal(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             f'InvalidAvailableAmt: Invalid available balance of account [{self.no_mask(deposit_savings_normal)}]. Available balance must be more than [{self.format_number(amount_savings_invalid)}] - en'
#         ]
#         self.dpt_mwr(
#             account_number=deposit_savings_normal,
#             withdraw_amount=amount_savings_invalid,
#             credit_accounting=gl_account_number,
#             list_error_message=list_error_message,
#         )

# # DPT_TRF (Debit account) - INVALID CASE
#     def test_006_dpt_trf_01_debit_check_not_allowed_deposit_type_fixed_deposit(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             f'InvalidDpttype: Invalid deposit type of account [{self.no_mask(deposit_fixed_01m_normal)}]- en'
#         ]
#         self.dpt_trf(
#             debit_account=deposit_fixed_01m_normal,
#             amount=amount_fixed_01m_valid,
#             credit_account=deposit_current_normal,
#             list_error_message=list_error_message,
#         )

#     def test_006_dpt_trf_02_debit_check_not_allowed_deposit_type_prepaid(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             f'InvalidDpttype: Invalid deposit type of account [{self.no_mask(deposit_prepaid_normal)}]- en'
#         ]
#         self.dpt_trf(
#             debit_account=deposit_prepaid_normal,
#             amount=amount_prepaid_valid,
#             credit_account=deposit_savings_normal,
#             list_error_message=list_error_message,
#         )

#     def test_006_dpt_trf_03_debit_check_not_allowed_deposit_status_current_block(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             f'InvalidDepositStatus: Invalid deposit status [{status_block}]'
#         ]
#         self.dpt_trf(
#             debit_account=deposit_current_block,
#             amount=amount_current_valid,
#             credit_account=deposit_current_normal,
#             list_error_message=list_error_message,
#         )

#     def test_006_dpt_trf_04_debit_check_not_allowed_deposit_status_current_closed(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             f'InvalidDepositStatus: Invalid deposit status [{status_closed}]'
#         ]
#         self.dpt_trf(
#             debit_account=deposit_current_close,
#             amount=amount_current_valid,
#             credit_account=deposit_current_normal,
#             list_error_message=list_error_message,
#         )

#     def test_006_dpt_trf_05_debit_check_not_allowed_deposit_status_current_pending(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             f'InvalidDepositStatus: Invalid deposit status [{status_pending}]'
#         ]
#         self.dpt_trf(
#             debit_account=deposit_current_pending,
#             amount=amount_current_valid,
#             credit_account=deposit_current_normal,
#             list_error_message=list_error_message,
#         )

#     def test_006_dpt_trf_06_debit_check_not_allowed_deposit_status_current_reject(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             f'InvalidDepositStatus: Invalid deposit status [{status_reject}]'
#         ]
#         self.dpt_trf(
#             debit_account=deposit_current_reject,
#             amount=amount_current_valid,
#             credit_account=deposit_current_normal,
#             list_error_message=list_error_message,
#         )

#     def test_006_dpt_trf_07_debit_check_not_allowed_deposit_status_current_new(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             f'InvalidDepositStatus: Invalid deposit status [{status_new}]'
#         ]
#         self.dpt_trf(
#             debit_account=deposit_current_new,
#             amount=amount_current_valid,
#             credit_account=deposit_current_normal,
#             list_error_message=list_error_message,
#         )

#     def test_006_dpt_trf_08_debit_check_not_allowed_deposit_status_savings_block(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             f'InvalidDepositStatus: Invalid deposit status [{status_block}]'
#         ]
#         self.dpt_trf(
#             debit_account=deposit_savings_block,
#             amount=amount_savings_valid,
#             credit_account=deposit_savings_normal,
#             list_error_message=list_error_message,
#         )

#     def test_006_dpt_trf_09_debit_check_not_allowed_deposit_status_savings_closed(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             f'InvalidDepositStatus: Invalid deposit status [{status_closed}]'
#         ]
#         self.dpt_trf(
#             debit_account=deposit_savings_close,
#             amount=amount_savings_valid,
#             credit_account=deposit_savings_normal,
#             list_error_message=list_error_message,
#         )

#     def test_006_dpt_trf_10_debit_check_not_allowed_deposit_status_savings_pending(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             f'InvalidDepositStatus: Invalid deposit status [{status_pending}]'
#         ]
#         self.dpt_trf(
#             debit_account=deposit_savings_pending,
#             amount=amount_savings_valid,
#             credit_account=deposit_savings_normal,
#             list_error_message=list_error_message,
#         )

#     def test_006_dpt_trf_11_debit_check_not_allowed_deposit_status_savings_reject(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             f'InvalidDepositStatus: Invalid deposit status [{status_reject}]'
#         ]
#         self.dpt_trf(
#             debit_account=deposit_savings_reject,
#             amount=amount_savings_valid,
#             credit_account=deposit_savings_normal,
#             list_error_message=list_error_message,
#         )

#     def test_006_dpt_trf_12_debit_check_not_allowed_deposit_status_savings_new(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             f'InvalidDepositStatus: Invalid deposit status [{status_new}]'
#         ]
#         self.dpt_trf(
#             debit_account=deposit_savings_new,
#             amount=amount_savings_valid,
#             credit_account=deposit_savings_normal,
#             list_error_message=list_error_message,
#         )

#     def test_006_dpt_trf_13_debit_check_available_balance_no_fee_invalid_current_dormant(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             f'InvalidAvailableAmt: Invalid available balance of account [{self.no_mask(deposit_current_dormant)}]. Available balance must be more than [{self.format_number(amount_current_invalid)}] - en'
#         ]
#         self.dpt_trf(
#             debit_account=deposit_current_dormant,
#             amount=amount_current_invalid,
#             credit_account=deposit_current_normal,
#             list_error_message=list_error_message,
#         )

#     def test_006_dpt_trf_14_debit_check_available_balance_no_fee_invalid_current_normal(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             f'InvalidAvailableAmt: Invalid available balance of account [{self.no_mask(deposit_current_normal)}]. Available balance must be more than [{self.format_number(amount_current_invalid)}] - en'
#         ]
#         self.dpt_trf(
#             debit_account=deposit_current_normal,
#             amount=amount_current_invalid,
#             credit_account=deposit_savings_normal,
#             list_error_message=list_error_message,
#         )

#     def test_006_dpt_trf_15_debit_check_available_balance_no_fee_invalid_savings_dormant(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             f'InvalidAvailableAmt: Invalid available balance of account [{self.no_mask(deposit_savings_dormant)}]. Available balance must be more than [{self.format_number(amount_savings_invalid)}] - en'
#         ]
#         self.dpt_trf(
#             debit_account=deposit_savings_dormant,
#             amount=amount_savings_invalid,
#             credit_account=deposit_current_normal,
#             list_error_message=list_error_message,
#         )

#     def test_006_dpt_trf_16_debit_check_available_balance_no_fee_invalid_savings_normal(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             f'InvalidAvailableAmt: Invalid available balance of account [{self.no_mask(deposit_savings_normal)}]. Available balance must be more than [{self.format_number(amount_savings_invalid)}] - en'
#         ]
#         self.dpt_trf(
#             debit_account=deposit_savings_normal,
#             amount=amount_savings_invalid,
#             credit_account=deposit_current_normal,
#             list_error_message=list_error_message,
#         )

#     def test_006_dpt_trf_17_debit_check_not_allowed_different_currency(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             f'DrCrCurrency: Debit and credit currency must be the same'
#         ]
#         self.dpt_trf(
#             debit_account=deposit_current_usd_normal,
#             amount=amount_current_usd_valid,
#             credit_account=deposit_savings_normal,
#             list_error_message=list_error_message,
#         )
#         self.dpt_trf(
#             debit_account=deposit_current_usd_normal,
#             amount=amount_current_usd_valid,
#             credit_account=deposit_current_normal,
#             list_error_message=list_error_message,
#         )

# # DPT_TRF (Credit account) - INVALID CASE
#     def test_006_dpt_trf_18_credit_check_not_allowed_deposit_status_current_block(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             f'InvalidDepositStatus: Invalid deposit status [{status_block}]'
#         ]
#         self.dpt_trf(
#             debit_account=other_current_deposit_account,
#             amount=amount_current_valid,
#             credit_account=deposit_current_block,
#             list_error_message=list_error_message,
#         )

#     def test_006_dpt_trf_19_credit_check_not_allowed_deposit_status_current_closed(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             f'InvalidDepositStatus: Invalid deposit status [{status_closed}]'
#         ]
#         self.dpt_trf(
#             debit_account=other_current_deposit_account,
#             amount=amount_current_valid,
#             credit_account=deposit_current_close,
#             list_error_message=list_error_message,
#         )

#     def test_006_dpt_trf_20_credit_check_not_allowed_deposit_status_current_pending(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             f'InvalidDepositStatus: Invalid deposit status [{status_pending}]'
#         ]
#         self.dpt_trf(
#             debit_account=other_current_deposit_account,
#             amount=amount_current_valid,
#             credit_account=deposit_current_pending,
#             list_error_message=list_error_message,
#         )

#     def test_006_dpt_trf_21_credit_check_not_allowed_deposit_status_current_reject(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             f'InvalidDepositStatus: Invalid deposit status [{status_reject}]'
#         ]
#         self.dpt_trf(
#             debit_account=other_current_deposit_account,
#             amount=amount_current_valid,
#             credit_account=deposit_current_reject,
#             list_error_message=list_error_message,
#         )

#     def test_006_dpt_trf_22_credit_check_not_allowed_deposit_status_savings_block(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             f'InvalidDepositStatus: Invalid deposit status [{status_block}]'
#         ]
#         self.dpt_trf(
#             debit_account=deposit_savings_normal,
#             amount=amount_savings_valid,
#             credit_account=deposit_savings_block,
#             list_error_message=list_error_message,
#         )

#     def test_006_dpt_trf_23_credit_check_not_allowed_deposit_status_savings_closed(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             f'InvalidDepositStatus: Invalid deposit status [{status_closed}]'
#         ]
#         self.dpt_trf(
#             debit_account=deposit_savings_normal,
#             amount=amount_savings_valid,
#             credit_account=deposit_savings_close,
#             list_error_message=list_error_message,
#         )

#     def test_006_dpt_trf_24_credit_check_not_allowed_deposit_status_savings_pending(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             f'InvalidDepositStatus: Invalid deposit status [{status_pending}]'
#         ]
#         self.dpt_trf(
#             debit_account=deposit_savings_normal,
#             amount=amount_savings_valid,
#             credit_account=deposit_savings_pending,
#             list_error_message=list_error_message,
#         )

#     def test_006_dpt_trf_25_credit_check_not_allowed_deposit_status_savings_reject(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             f'InvalidDepositStatus: Invalid deposit status [{status_reject}]'
#         ]
#         self.dpt_trf(
#             debit_account=deposit_savings_normal,
#             amount=amount_savings_valid,
#             credit_account=deposit_savings_reject,
#             list_error_message=list_error_message,
#         )

#     def test_006_dpt_trf_26_credit_check_not_allowed_deposit_status_fixed_deposit_block(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             f'InvalidDepositStatus: Invalid deposit status [{status_block}]'
#         ]
#         self.dpt_trf(
#             debit_account=deposit_savings_normal,
#             amount=amount_savings_valid,
#             credit_account=deposit_fixed_01m_block,
#             list_error_message=list_error_message,
#         )

#     def test_006_dpt_trf_27_credit_check_not_allowed_deposit_status_fixed_deposit_closed(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             f'InvalidDepositStatus: Invalid deposit status [{status_closed}]'
#         ]
#         self.dpt_trf(
#             debit_account=deposit_savings_normal,
#             amount=amount_savings_valid,
#             credit_account=deposit_fixed_01m_close,
#             list_error_message=list_error_message,
#         )

#     def test_006_dpt_trf_28_credit_check_not_allowed_deposit_status_fixed_deposit_pending(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             f'InvalidDepositStatus: Invalid deposit status [{status_pending}]'
#         ]
#         self.dpt_trf(
#             debit_account=deposit_savings_normal,
#             amount=amount_savings_valid,
#             credit_account=deposit_fixed_01m_pending,
#             list_error_message=list_error_message,
#         )

#     def test_006_dpt_trf_29_credit_check_not_allowed_deposit_status_fixed_deposit_reject(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             f'InvalidDepositStatus: Invalid deposit status [{status_reject}]'
#         ]
#         self.dpt_trf(
#             debit_account=deposit_savings_normal,
#             amount=amount_savings_valid,
#             credit_account=deposit_fixed_01m_reject,
#             list_error_message=list_error_message,
#         )

#     def test_006_dpt_trf_30_credit_check_not_allowed_deposit_status_prepaid_block(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             f'InvalidDepositStatus: Invalid deposit status [{status_block}]'
#         ]
#         self.dpt_trf(
#             debit_account=deposit_current_normal,
#             amount=amount_current_valid,
#             credit_account=deposit_prepaid_block,
#             list_error_message=list_error_message,
#         )

#     def test_006_dpt_trf_31_credit_check_not_allowed_deposit_status_prepaid_closed(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             f'InvalidDepositStatus: Invalid deposit status [{status_closed}]'
#         ]
#         self.dpt_trf(
#             debit_account=deposit_current_normal,
#             amount=amount_current_valid,
#             credit_account=deposit_prepaid_close,
#             list_error_message=list_error_message,
#         )

#     def test_006_dpt_trf_32_credit_check_not_allowed_deposit_status_prepaid_pending(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             f'InvalidDepositStatus: Invalid deposit status [{status_pending}]'
#         ]
#         self.dpt_trf(
#             debit_account=deposit_current_normal,
#             amount=amount_current_valid,
#             credit_account=deposit_prepaid_pending,
#             list_error_message=list_error_message,
#         )

#     def test_006_dpt_trf_33_credit_check_not_allowed_deposit_status_prepaid_reject(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             f'InvalidDepositStatus: Invalid deposit status [{status_reject}]'
#         ]
#         self.dpt_trf(
#             debit_account=deposit_current_normal,
#             amount=amount_current_valid,
#             credit_account=deposit_prepaid_reject,
#             list_error_message=list_error_message,
#         )

# # DPT_FEE - INVALID CASE
#     def test_007_dpt_fee_01_check_not_allowed_deposit_status_current_block(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             'Passbook number: Can not be blank'
#         ]
#         self.dpt_fee(
#             account_number=deposit_current_block,
#             ifc_codes=ifc_codes,
#             values=values_valid,
#             list_error_message=list_error_message,
#         )

#     def test_007_dpt_fee_02_check_not_allowed_deposit_status_current_closed(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             'Passbook number: Can not be blank'
#         ]
#         self.dpt_fee(
#             account_number=deposit_current_close,
#             ifc_codes=ifc_codes,
#             values=values_valid,
#             list_error_message=list_error_message,
#         )

#     def test_007_dpt_fee_03_check_not_allowed_deposit_status_current_pending(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             'Passbook number: Can not be blank'
#         ]
#         self.dpt_fee(
#             account_number=deposit_current_pending,
#             ifc_codes=ifc_codes,
#             values=values_valid,
#             list_error_message=list_error_message,
#         )

#     def test_007_dpt_fee_04_check_not_allowed_deposit_status_current_reject(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             'Passbook number: Can not be blank'
#         ]
#         self.dpt_fee(
#             account_number=deposit_current_reject,
#             ifc_codes=ifc_codes,
#             values=values_valid,
#             list_error_message=list_error_message,
#         )

#     def test_007_dpt_fee_05_check_not_allowed_deposit_status_current_new(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             'Passbook number: Can not be blank'
#         ]
#         self.dpt_fee(
#             account_number=deposit_current_new,
#             ifc_codes=ifc_codes,
#             values=values_valid,
#             list_error_message=list_error_message,
#         )

#     def test_007_dpt_fee_06_check_not_allowed_deposit_status_current_dormant(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             'Passbook number: Can not be blank'
#         ]
#         self.dpt_fee(
#             account_number=deposit_current_dormant,
#             ifc_codes=ifc_codes,
#             values=values_valid,
#             list_error_message=list_error_message,
#         )

#     def test_007_dpt_fee_07_check_not_allowed_deposit_status_savings_block(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             f'InvalidDepositStatus: Invalid deposit status [{status_block}]'
#         ]
#         self.dpt_fee(
#             account_number=deposit_savings_block,
#             ifc_codes=ifc_codes,
#             values=values_valid,
#             list_error_message=list_error_message,
#         )

#     def test_007_dpt_fee_08_check_not_allowed_deposit_status_savings_closed(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             f'InvalidDepositStatus: Invalid deposit status [{status_closed}]'
#         ]
#         self.dpt_fee(
#             account_number=deposit_savings_close,
#             ifc_codes=ifc_codes,
#             values=values_valid,
#             list_error_message=list_error_message,
#         )

#     def test_007_dpt_fee_09_check_not_allowed_deposit_status_savings_pending(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             'Passbook number: Can not be blank'
#         ]
#         self.dpt_fee(
#             account_number=deposit_savings_pending,
#             ifc_codes=ifc_codes,
#             values=values_valid,
#             list_error_message=list_error_message,
#         )

#     def test_007_dpt_fee_10_check_not_allowed_deposit_status_savings_reject(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             'Passbook number: Can not be blank'
#         ]
#         self.dpt_fee(
#             account_number=deposit_savings_reject,
#             ifc_codes=ifc_codes,
#             values=values_valid,
#             list_error_message=list_error_message,
#         )

#     def test_007_dpt_fee_11_check_not_allowed_deposit_status_savings_new(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             f'InvalidDepositStatus: Invalid deposit status [{status_new}]'
#         ]
#         self.dpt_fee(
#             account_number=deposit_savings_new,
#             ifc_codes=ifc_codes,
#             values=values_valid,
#             list_error_message=list_error_message,
#         )

#     def test_007_dpt_fee_12_check_not_allowed_deposit_status_savings_dormant(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             f'InvalidDepositStatus: Invalid deposit status [{status_dormant}]'
#         ]
#         self.dpt_fee(
#             account_number=deposit_savings_dormant,
#             ifc_codes=ifc_codes,
#             values=values_valid,
#             list_error_message=list_error_message,
#         )

#     def test_007_dpt_fee_13_check_not_allowed_deposit_status_fixed_deposit_block(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             f'InvalidDepositStatus: Invalid deposit status [{status_block}]'
#         ]
#         self.dpt_fee(
#             account_number=deposit_fixed_01m_block,
#             ifc_codes=ifc_codes,
#             values=values_valid,
#             list_error_message=list_error_message,
#         )

#     def test_007_dpt_fee_14_check_not_allowed_deposit_status_fixed_deposit_closed(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             f'InvalidDepositStatus: Invalid deposit status [{status_closed}]'
#         ]
#         self.dpt_fee(
#             account_number=deposit_fixed_01m_close,
#             ifc_codes=ifc_codes,
#             values=values_valid,
#             list_error_message=list_error_message,
#         )

#     def test_007_dpt_fee_15_check_not_allowed_deposit_status_fixed_deposit_pending(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             'Passbook number: Can not be blank'
#         ]
#         self.dpt_fee(
#             account_number=deposit_fixed_01m_pending,
#             ifc_codes=ifc_codes,
#             values=values_valid,
#             list_error_message=list_error_message,
#         )

#     def test_007_dpt_fee_16_check_not_allowed_deposit_status_fixed_deposit_reject(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             'Passbook number: Can not be blank'
#         ]
#         self.dpt_fee(
#             account_number=deposit_fixed_01m_reject,
#             ifc_codes=ifc_codes,
#             values=values_valid,
#             list_error_message=list_error_message,
#         )

#     def test_007_dpt_fee_17_check_not_allowed_deposit_status_fixed_deposit_new(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             f'InvalidDepositStatus: Invalid deposit status [{status_new}]'
#         ]
#         self.dpt_fee(
#             account_number=deposit_fixed_01m_new,
#             ifc_codes=ifc_codes,
#             values=values_valid,
#             list_error_message=list_error_message,
#         )

#     def test_007_dpt_fee_18_check_not_allowed_deposit_status_prepaid_block(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             f'InvalidDepositStatus: Invalid deposit status [{status_block}]'
#         ]
#         self.dpt_fee(
#             account_number=deposit_prepaid_block,
#             ifc_codes=ifc_codes,
#             values=values_valid,
#             list_error_message=list_error_message,
#         )

#     def test_007_dpt_fee_19_check_not_allowed_deposit_status_prepaid_closed(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             f'InvalidDepositStatus: Invalid deposit status [{status_closed}]'
#         ]
#         self.dpt_fee(
#             account_number=deposit_prepaid_close,
#             ifc_codes=ifc_codes,
#             values=values_valid,
#             list_error_message=list_error_message,
#         )

#     def test_007_dpt_fee_20_check_not_allowed_deposit_status_prepaid_pending(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             'Passbook number: Can not be blank'
#         ]
#         self.dpt_fee(
#             account_number=deposit_prepaid_pending,
#             ifc_codes=ifc_codes,
#             values=values_valid,
#             list_error_message=list_error_message,
#         )

#     def test_007_dpt_fee_21_check_not_allowed_deposit_status_prepaid_reject(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             'Passbook number: Can not be blank'
#         ]
#         self.dpt_fee(
#             account_number=deposit_prepaid_reject,
#             ifc_codes=ifc_codes,
#             values=values_valid,
#             list_error_message=list_error_message,
#         )

#     def test_007_dpt_fee_22_check_not_allowed_deposit_status_prepaid_new(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             f'InvalidDepositStatus: Invalid deposit status [{status_new}]'
#         ]
#         self.dpt_fee(
#             account_number=deposit_prepaid_new,
#             ifc_codes=ifc_codes,
#             values=values_valid,
#             list_error_message=list_error_message,
#         )

#     def test_007_dpt_fee_23_check_available_balance_no_fee_invalid_current_normal(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             'Passbook number: Can not be blank'
#         ]
#         self.dpt_fee(
#             account_number=deposit_current_normal,
#             ifc_codes=ifc_codes,
#             values=values_invalid,
#             list_error_message=list_error_message,
#         )

#     def test_007_dpt_fee_24_check_available_balance_no_fee_invalid_savings_normal(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             f'InvalidAvailableAmt: Invalid available balance of account [{self.no_mask(deposit_savings_normal)}]. Available balance must be more than [{self.format_number(value_invalid)}] - en'
#         ]
#         self.dpt_fee(
#             account_number=deposit_savings_normal,
#             ifc_codes=ifc_codes,
#             values=values_invalid,
#             list_error_message=list_error_message,
#         )

#     def test_007_dpt_fee_25_check_available_balance_no_fee_invalid_fixed_deposit_normal(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             f'InvalidAvailableAmt: Invalid available balance of account [{self.no_mask(deposit_fixed_01m_normal)}]. Available balance must be more than [{self.format_number(value_invalid)}] - en'
#         ]
#         self.dpt_fee(
#             account_number=deposit_fixed_01m_normal,
#             ifc_codes=ifc_codes,
#             values=values_invalid,
#             list_error_message=list_error_message,
#         )

#     def test_007_dpt_fee_26_check_available_balance_no_fee_invalid_prepaid_normal(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             f'InvalidAvailableAmt: Invalid available balance of account [{self.no_mask(deposit_prepaid_normal)}]. Available balance must be more than [{self.format_number(value_invalid)}] - en'
#         ]
#         self.dpt_fee(
#             account_number=deposit_prepaid_normal,
#             ifc_codes=ifc_codes,
#             values=values_invalid,
#             list_error_message=list_error_message,
#         )

#     def test_007_dpt_fee_27_check_not_allowed_deposit_type_current(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             'Passbook number: Can not be blank'
#         ]
#         self.dpt_fee(
#             account_number=deposit_current_normal,
#             ifc_codes=ifc_codes,
#             values=values_valid,
#             list_error_message=list_error_message
#         )

#     def test_007_dpt_fee_28_check_not_allowed_deposit_type_fixed_deposit(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             f'Invalid deposit type [Fixed Deposit] of account [{self.no_mask(deposit_fixed_01m_normal)}]- en'
#         ]
#         dpt_fee_result = self.dpt_fee(
#             account_number=deposit_fixed_01m_normal,
#             ifc_codes=ifc_codes,
#             values=values_valid,
#             approve_later='Y',
#         )
#         self.transaction_approve(
#             transaction_references=dpt_fee_result[0], 
#             username=username_approve,
#             password=password_approve,
#             allow_approve='N',
#             list_error_message=list_error_message
#         )
#         self.transaction_reject(
#             transaction_references=dpt_fee_result[0], 
#             username=username_reverse,
#             password=password_reverse
#         )

#     def test_007_dpt_fee_29_check_not_allowed_deposit_type_prepaid(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             f'Invalid deposit type [Fixed Deposit] of account [{self.no_mask(deposit_prepaid_normal)}]- en'
#         ]
#         dpt_fee_result = self.dpt_fee(
#             account_number=deposit_prepaid_normal,
#             ifc_codes=ifc_codes,
#             values=values_valid,
#             approve_later='Y',
#         )
#         self.transaction_approve(
#             transaction_references=dpt_fee_result[0], 
#             username=username_approve,
#             password=password_approve,
#             allow_approve='N',
#             list_error_message=list_error_message
#         )
#         self.transaction_reject(
#             transaction_references=dpt_fee_result[0], 
#             username=username_reverse,
#             password=password_reverse
#         )

# # DPT_CIS - INVALID CASE
#     def test_008_dpt_cis_00_create_data_use_for_testing(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         global from_serial_cq, to_serial_cq
#         generated_number = self.gen_serial_number(stock_prefix_cq, stock_type_cq, 24)
#         print(f'generated_number: {generated_number}')
#         from_serial = generated_number[0]
#         to_serial = generated_number[1]
#         dpt_srg_result = self.dpt_srg(
#             stock_type=stock_type_cq,
#             from_serial=from_serial,
#             to_serial=to_serial,
#             stock_prefix=stock_prefix_cq,
#             number_of_leaves=number_of_leaves_cq,
#             number_of_book=number_of_book_cq,
#             approve_on_form='Y',
#             username=username_approve,
#             password=password_approve
#         )
#         from_serial_cq = dpt_srg_result[1]
#         to_serial_cq = dpt_srg_result[2]
#         self.dpt_sat(
#             stock_type=stock_type_cq,
#             from_serial=from_serial_cq,
#             to_serial=to_serial_cq,
#             assigned_staff_code=username_login
#         )
#         self.dpt_ccr(
#             stock_type=stock_type_cq,
#             from_serial=from_serial_cq,
#             to_serial=to_serial_cq,
#             approve_on_form='Y',
#             username=username_approve,
#             password=password_approve
#         )

#     def test_008_dpt_cis_01_check_not_allowed_deposit_status_current_block(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             f'InvalidDepositStatus: Invalid deposit status [{status_block}]'
#         ]
#         self.dpt_cis(
#             account_number=deposit_current_block,
#             from_serial=from_serial_cq,
#             to_serial=to_serial_cq,
#             list_error_message=list_error_message,
#         )

#     def test_008_dpt_cis_02_check_not_allowed_deposit_status_current_closed(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             f'InvalidDepositStatus: Invalid deposit status [{status_closed}]'
#         ]
#         self.dpt_cis(
#             account_number=deposit_current_close,
#             from_serial=from_serial_cq,
#             to_serial=to_serial_cq,
#             list_error_message=list_error_message,
#         )

#     def test_008_dpt_cis_03_check_not_allowed_deposit_status_current_pending(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             f'InvalidDepositStatus: Invalid deposit status [{status_pending}]'
#         ]
#         self.dpt_cis(
#             account_number=deposit_current_pending,
#             from_serial=from_serial_cq,
#             to_serial=to_serial_cq,
#             list_error_message=list_error_message,
#         )

#     def test_008_dpt_cis_04_check_not_allowed_deposit_status_current_reject(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             f'InvalidDepositStatus: Invalid deposit status [{status_reject}]'
#         ]
#         self.dpt_cis(
#             account_number=deposit_current_reject,
#             from_serial=from_serial_cq,
#             to_serial=to_serial_cq,
#             list_error_message=list_error_message,
#         )

#     def test_008_dpt_cis_05_check_not_allowed_deposit_type_savings(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             f'Invalid deposit type of account [{self.no_mask(deposit_savings_normal)}]- en'
#         ]
#         dpt_cis_result = self.dpt_cis(
#             account_number=deposit_savings_normal,
#             from_serial=from_serial_cq,
#             to_serial=to_serial_cq,
#             approve_later='Y',
#         )
#         self.transaction_approve(
#             transaction_references=dpt_cis_result[0], 
#             username=username_approve,
#             password=password_approve,
#             allow_approve='N',
#             list_error_message=list_error_message
#         )
#         self.transaction_reject(
#             transaction_references=dpt_cis_result[0], 
#             username=username_reverse,
#             password=password_reverse
#         )

#     def test_008_dpt_cis_06_check_not_allowed_deposit_type_fixed_deposit(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             f'Invalid deposit type of account [{self.no_mask(deposit_fixed_01m_normal)}]- en'
#         ]
#         dpt_cis_result = self.dpt_cis(
#             account_number=deposit_fixed_01m_normal,
#             from_serial=from_serial_cq,
#             to_serial=to_serial_cq,
#             approve_later='Y',
#         )
#         self.transaction_approve(
#             transaction_references=dpt_cis_result[0], 
#             username=username_approve,
#             password=password_approve,
#             allow_approve='N',
#             list_error_message=list_error_message
#         )
#         self.transaction_reject(
#             transaction_references=dpt_cis_result[0], 
#             username=username_reverse,
#             password=password_reverse
#         )

#     def test_008_dpt_cis_07_check_not_allowed_deposit_type_prepaid(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             f'Invalid deposit type of account [{self.no_mask(deposit_prepaid_normal)}]- en'
#         ]
#         dpt_cis_result = self.dpt_cis(
#             account_number=deposit_prepaid_normal,
#             from_serial=from_serial_cq,
#             to_serial=to_serial_cq,
#             approve_later='Y',
#         )
#         self.transaction_approve(
#             transaction_references=dpt_cis_result[0], 
#             username=username_approve,
#             password=password_approve,
#             allow_approve='N',
#             list_error_message=list_error_message
#         )
#         self.transaction_reject(
#             transaction_references=dpt_cis_result[0], 
#             username=username_reverse,
#             password=password_reverse
#         )

#     def test_008_dpt_cis_08_fee_check_not_allowed_deposit_type_fixed_deposit(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             'InvalidAccount: Invalid account number [{0}]'
#         ]
#         self.dpt_cis(
#             account_number=deposit_current_normal,
#             from_serial=from_serial_cq,
#             to_serial=to_serial_cq,
#             list_error_message=list_error_message,
#             ifc_codes=ifc_codes,
#             values=values_valid,
#             fee_collect_method='Deposit',
#             account_number_for_fee=deposit_fixed_01m_normal,
#         )

#     def test_008_dpt_cis_09_fee_check_not_allowed_deposit_type_prepaid(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             'InvalidAccount: Invalid account number [{0}]'
#         ]
#         self.dpt_cis(
#             account_number=deposit_current_normal,
#             from_serial=from_serial_cq,
#             to_serial=to_serial_cq,
#             list_error_message=list_error_message,
#             ifc_codes=ifc_codes,
#             values=values_valid,
#             fee_collect_method='Deposit',
#             account_number_for_fee=deposit_prepaid_normal,
#         )

#     def test_008_dpt_cis_10_fee_check_not_allowed_deposit_status_current_block(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             'InvalidAccount: Invalid account number [{0}]'
#         ]
#         self.dpt_cis(
#             account_number=deposit_current_normal,
#             from_serial=from_serial_cq,
#             to_serial=to_serial_cq,
#             list_error_message=list_error_message,
#             ifc_codes=ifc_codes,
#             values=values_valid,
#             fee_collect_method='Deposit',
#             account_number_for_fee=deposit_current_block,
#         )

#     def test_008_dpt_cis_11_fee_check_not_allowed_deposit_status_current_closed(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             'InvalidAccount: Invalid account number [{0}]'
#         ]
#         self.dpt_cis(
#             account_number=deposit_current_normal,
#             from_serial=from_serial_cq,
#             to_serial=to_serial_cq,
#             list_error_message=list_error_message,
#             ifc_codes=ifc_codes,
#             values=values_valid,
#             fee_collect_method='Deposit',
#             account_number_for_fee=deposit_current_close,
#         )

#     def test_008_dpt_cis_12_fee_check_not_allowed_deposit_status_current_pending(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             'InvalidAccount: Invalid account number [{0}]'
#         ]
#         self.dpt_cis(
#             account_number=deposit_current_normal,
#             from_serial=from_serial_cq,
#             to_serial=to_serial_cq,
#             list_error_message=list_error_message,
#             ifc_codes=ifc_codes,
#             values=values_valid,
#             fee_collect_method='Deposit',
#             account_number_for_fee=deposit_current_pending,
#         )

#     def test_008_dpt_cis_13_fee_check_not_allowed_deposit_status_current_reject(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             'InvalidAccount: Invalid account number [{0}]'
#         ]
#         self.dpt_cis(
#             account_number=deposit_current_normal,
#             from_serial=from_serial_cq,
#             to_serial=to_serial_cq,
#             list_error_message=list_error_message,
#             ifc_codes=ifc_codes,
#             values=values_valid,
#             fee_collect_method='Deposit',
#             account_number_for_fee=deposit_current_reject,
#         )

#     def test_008_dpt_cis_14_fee_check_not_allowed_deposit_status_current_new(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             f'InvalidDepositStatus: Invalid deposit status [{status_new}]'
#         ]
#         self.dpt_cis(
#             account_number=deposit_current_normal,
#             from_serial=from_serial_cq,
#             to_serial=to_serial_cq,
#             list_error_message=list_error_message,
#             ifc_codes=ifc_codes,
#             values=values_valid,
#             fee_collect_method='Deposit',
#             account_number_for_fee=deposit_current_new,
#         )

#     def test_008_dpt_cis_15_fee_check_not_allowed_deposit_status_current_dormant(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             'InvalidAccount: Invalid account number [{0}]'
#         ]
#         self.dpt_cis(
#             account_number=deposit_current_normal,
#             from_serial=from_serial_cq,
#             to_serial=to_serial_cq,
#             list_error_message=list_error_message,
#             ifc_codes=ifc_codes,
#             values=values_valid,
#             fee_collect_method='Deposit',
#             account_number_for_fee=deposit_current_dormant,
#         )

#     def test_008_dpt_cis_16_fee_check_not_allowed_deposit_status_savings_block(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             'InvalidAccount: Invalid account number [{0}]'
#         ]
#         self.dpt_cis(
#             account_number=deposit_current_normal,
#             from_serial=from_serial_cq,
#             to_serial=to_serial_cq,
#             list_error_message=list_error_message,
#             ifc_codes=ifc_codes,
#             values=values_valid,
#             fee_collect_method='Deposit',
#             account_number_for_fee=deposit_savings_block,
#         )

#     def test_008_dpt_cis_17_fee_check_not_allowed_deposit_status_savings_closed(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             'InvalidAccount: Invalid account number [{0}]'
#         ]
#         self.dpt_cis(
#             account_number=deposit_current_normal,
#             from_serial=from_serial_cq,
#             to_serial=to_serial_cq,
#             list_error_message=list_error_message,
#             ifc_codes=ifc_codes,
#             values=values_valid,
#             fee_collect_method='Deposit',
#             account_number_for_fee=deposit_savings_close,
#         )

#     def test_008_dpt_cis_18_fee_check_not_allowed_deposit_status_savings_pending(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             'InvalidAccount: Invalid account number [{0}]'
#         ]
#         self.dpt_cis(
#             account_number=deposit_current_normal,
#             from_serial=from_serial_cq,
#             to_serial=to_serial_cq,
#             list_error_message=list_error_message,
#             ifc_codes=ifc_codes,
#             values=values_valid,
#             fee_collect_method='Deposit',
#             account_number_for_fee=deposit_savings_pending,
#         )

#     def test_008_dpt_cis_19_fee_check_not_allowed_deposit_status_savings_reject(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             'InvalidAccount: Invalid account number [{0}]'
#         ]
#         self.dpt_cis(
#             account_number=deposit_current_normal,
#             from_serial=from_serial_cq,
#             to_serial=to_serial_cq,
#             list_error_message=list_error_message,
#             ifc_codes=ifc_codes,
#             values=values_valid,
#             fee_collect_method='Deposit',
#             account_number_for_fee=deposit_savings_reject,
#         )

#     def test_008_dpt_cis_20_fee_check_not_allowed_deposit_status_savings_new(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             f'InvalidDepositStatus: Invalid deposit status [{status_new}]'
#         ]
#         self.dpt_cis(
#             account_number=deposit_current_normal,
#             from_serial=from_serial_cq,
#             to_serial=to_serial_cq,
#             list_error_message=list_error_message,
#             ifc_codes=ifc_codes,
#             values=values_valid,
#             fee_collect_method='Deposit',
#             account_number_for_fee=deposit_savings_new,
#         )

#     def test_008_dpt_cis_21_fee_check_not_allowed_deposit_status_savings_dormant(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             'InvalidAccount: Invalid account number [{0}]'
#         ]
#         self.dpt_cis(
#             account_number=deposit_current_normal,
#             from_serial=from_serial_cq,
#             to_serial=to_serial_cq,
#             list_error_message=list_error_message,
#             ifc_codes=ifc_codes,
#             values=values_valid,
#             fee_collect_method='Deposit',
#             account_number_for_fee=deposit_savings_dormant,
#         )

#     def test_008_dpt_cis_22_fee_check_not_allowed_different_currency_current_usd_normal(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             'InvalidAccount: Invalid account number [{0}]'
#         ]
#         self.dpt_cis(
#             account_number=deposit_current_normal,
#             from_serial=from_serial_cq,
#             to_serial=to_serial_cq,
#             list_error_message=list_error_message,
#             ifc_codes=ifc_codes,
#             values=values_valid,
#             fee_collect_method='Deposit',
#             account_number_for_fee=deposit_current_usd_normal,
#         )

#     def test_008_dpt_cis_23_fee_check_available_balance_invalid_current_normal(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             f'InvalidAvailableAmt: Invalid available balance of account [{self.no_mask(other_current_deposit_account)}]. Available balance must be more than [{self.format_number(value_invalid)}] - en'
#         ]
#         self.dpt_cis(
#             account_number=deposit_current_normal,
#             from_serial=from_serial_cq,
#             to_serial=to_serial_cq,
#             list_error_message=list_error_message,
#             ifc_codes=ifc_codes,
#             values=values_invalid,
#             fee_collect_method='Deposit',
#             account_number_for_fee=other_current_deposit_account,
#         )

#     def test_008_dpt_cis_24_fee_check_available_balance_invalid_savings_normal(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             f'InvalidAvailableAmt: Invalid available balance of account [{self.no_mask(other_savings_deposit_account)}]. Available balance must be more than [{self.format_number(value_invalid)}] - en'
#         ]
#         self.dpt_cis(
#             account_number=deposit_current_normal,
#             from_serial=from_serial_cq,
#             to_serial=to_serial_cq,
#             list_error_message=list_error_message,
#             ifc_codes=ifc_codes,
#             values=values_invalid,
#             fee_collect_method='Deposit',
#             account_number_for_fee=other_savings_deposit_account,
#         )

# # DPT_CER - INVALID CASE
#     def test_009_dpt_cer_00_create_data_use_for_testing(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         global deposit_prepaid_normal_valid
#         dpt_opn_result = self.dpt_opn(
#             customer_code=customer_code_personal,
#             customer_type='Single customer',
#             catalogue_code=catalogue_code_prepaid,
#             reason_of_account_opening='Enter value reason of account opening',
#             to_account_number=other_current_deposit_account,
#         )
#         deposit_prepaid_normal_valid=dpt_opn_result[1]
#         self.dpt_apr(
#             account_number=deposit_prepaid_normal_valid,
#             approve_on_form='Y',
#             username=username_approve,
#             password=password_approve
#         )
#         self.dpt_cdp(
#             account_number=deposit_prepaid_normal_valid,
#             amount_deposit=deposit_amount_prepaid,
#             approve_on_form='Y',
#             username=username_approve,
#             password=password_approve
#         )
#         global from_serial_fr, to_serial_fr
#         generated_number = self.gen_serial_number(stock_prefix_fr, stock_type_fr, 0)
#         print(f'generated_number: {generated_number}')
#         from_serial = generated_number[0]
#         to_serial = generated_number[1]
#         dpt_srg_result = self.dpt_srg(
#             stock_type=stock_type_fr,
#             from_serial=from_serial,
#             to_serial=to_serial,
#             stock_prefix=stock_prefix_fr,
#             number_of_leaves=number_of_leaves_fr,
#             number_of_book=number_of_book_fr,
#             approve_on_form='Y',
#             username=username_approve,
#             password=password_approve
#         )
#         from_serial_fr = dpt_srg_result[1]
#         to_serial_fr = dpt_srg_result[2]
#         self.dpt_sat(
#             stock_type=stock_type_fr,
#             from_serial=from_serial_fr,
#             to_serial=to_serial_fr,
#             assigned_staff_code=username_login
#         )
#         self.dpt_ccr(
#             stock_type=stock_type_fr,
#             from_serial=from_serial_fr,
#             to_serial=to_serial_fr,
#             approve_on_form='Y',
#             username=username_approve,
#             password=password_approve
#         )

#     def test_009_dpt_cer_01_check_not_allowed_deposit_type_current(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             'InvalidDptSubType: Deposit Subtype is invalid'
#         ]
#         self.dpt_cer(
#             account_number=deposit_current_normal,
#             cerfiticate_serial=from_serial_fr,
#             list_error_message=list_error_message,
#         )

#     def test_009_dpt_cer_02_check_not_allowed_deposit_type_savings(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             'InvalidDptSubType: Deposit Subtype is invalid'
#         ]
#         self.dpt_cer(
#             account_number=deposit_savings_normal,
#             cerfiticate_serial=from_serial_fr,
#             list_error_message=list_error_message,
#         )

#     def test_009_dpt_cer_03_check_not_allowed_deposit_type_fixed_deposit(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             'InvalidDptSubType: Deposit Subtype is invalid'
#         ]
#         self.dpt_cer(
#             account_number=deposit_fixed_01m_normal,
#             cerfiticate_serial=from_serial_fr,
#             list_error_message=list_error_message,
#         )

#     def test_009_dpt_cer_04_check_not_allowed_deposit_status_block(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             f'InvalidDepositStatus: Invalid deposit status [{status_block}]'
#         ]
#         self.dpt_cer(
#             account_number=deposit_prepaid_block,
#             cerfiticate_serial=from_serial_fr,
#             list_error_message=list_error_message,
#         )

#     def test_009_dpt_cer_05_check_not_allowed_deposit_status_closed(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             f'InvalidDepositStatus: Invalid deposit status [{status_closed}]'
#         ]
#         self.dpt_cer(
#             account_number=deposit_prepaid_close,
#             cerfiticate_serial=from_serial_fr,
#             list_error_message=list_error_message,
#         )

#     def test_009_dpt_cer_06_check_not_allowed_deposit_status_pending(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             f'InvalidDepositStatus: Invalid deposit status [{status_pending}]'
#         ]
#         self.dpt_cer(
#             account_number=deposit_prepaid_pending,
#             cerfiticate_serial=from_serial_fr,
#             list_error_message=list_error_message,
#         )

#     def test_009_dpt_cer_07_check_not_allowed_deposit_status_reject(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             f'InvalidDepositStatus: Invalid deposit status [{status_reject}]'
#         ]
#         self.dpt_cer(
#             account_number=deposit_prepaid_reject,
#             cerfiticate_serial=from_serial_fr,
#             list_error_message=list_error_message,
#         )

#     def test_009_dpt_cer_08_fee_check_not_allowed_deposit_status_current_block(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             f'InvalidDepositStatus: Invalid deposit status [{status_block}]'
#         ]
#         self.dpt_cer(
#             account_number=deposit_prepaid_normal_valid,
#             cerfiticate_serial=from_serial_fr,
#             list_error_message=list_error_message,
#             ifc_codes=ifc_codes,
#             values=values_valid,
#             fee_collect_method='Deposit',
#             account_number_for_fee=deposit_current_block,
#         )

#     def test_009_dpt_cer_09_fee_check_not_allowed_deposit_status_savings_block(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             f'InvalidDepositStatus: Invalid deposit status [{status_block}]'
#         ]
#         self.dpt_cer(
#             account_number=deposit_prepaid_normal_valid,
#             cerfiticate_serial=from_serial_fr,
#             list_error_message=list_error_message,
#             ifc_codes=ifc_codes,
#             values=values_valid,
#             fee_collect_method='Deposit',
#             account_number_for_fee=deposit_savings_block,
#         )

#     def test_009_dpt_cer_10_fee_check_available_balance_invalid_current_closed(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             f'InvalidAvailableAmt: Invalid available balance of account [{self.no_mask(deposit_current_close)}]. Available balance must be more than [{self.format_number(value_valid)}] - en'
#         ]
#         self.dpt_cer(
#             account_number=deposit_prepaid_normal_valid,
#             cerfiticate_serial=from_serial_fr,
#             list_error_message=list_error_message,
#             ifc_codes=ifc_codes,
#             values=values_valid,
#             fee_collect_method='Deposit',
#             account_number_for_fee=deposit_current_close,
#         )

#     def test_009_dpt_cer_11_fee_check_available_balance_invalid_current_pending(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             f'InvalidAvailableAmt: Invalid available balance of account [{self.no_mask(deposit_current_pending)}]. Available balance must be more than [{self.format_number(value_valid)}] - en'
#         ]
#         self.dpt_cer(
#             account_number=deposit_prepaid_normal_valid,
#             cerfiticate_serial=from_serial_fr,
#             list_error_message=list_error_message,
#             ifc_codes=ifc_codes,
#             values=values_valid,
#             fee_collect_method='Deposit',
#             account_number_for_fee=deposit_current_pending,
#         )

#     def test_009_dpt_cer_12_fee_check_available_balance_invalid_current_reject(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             f'InvalidAvailableAmt: Invalid available balance of account [{self.no_mask(deposit_current_reject)}]. Available balance must be more than [{self.format_number(value_valid)}] - en'
#         ]
#         self.dpt_cer(
#             account_number=deposit_prepaid_normal_valid,
#             cerfiticate_serial=from_serial_fr,
#             list_error_message=list_error_message,
#             ifc_codes=ifc_codes,
#             values=values_valid,
#             fee_collect_method='Deposit',
#             account_number_for_fee=deposit_current_reject,
#         )

#     def test_009_dpt_cer_13_fee_check_available_balance_invalid_current_new(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             f'InvalidAvailableAmt: Invalid available balance of account [{self.no_mask(deposit_current_new)}]. Available balance must be more than [{self.format_number(value_valid)}] - en'
#         ]
#         self.dpt_cer(
#             account_number=deposit_prepaid_normal_valid,
#             cerfiticate_serial=from_serial_fr,
#             list_error_message=list_error_message,
#             ifc_codes=ifc_codes,
#             values=values_valid,
#             fee_collect_method='Deposit',
#             account_number_for_fee=deposit_current_new,
#         )

#     def test_009_dpt_cer_14_fee_check_available_balance_invalid_current_dormant(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             f'Invalid account status [{status_dormant}]'
#         ]
#         dpt_cer_result = self.dpt_cer(
#             account_number=deposit_prepaid_normal_valid,
#             cerfiticate_serial=from_serial_fr,
#             ifc_codes=ifc_codes,
#             values=values_valid,
#             fee_collect_method='Deposit',
#             account_number_for_fee=deposit_current_dormant,
#             approve_later='Y',
#         )
#         self.transaction_approve(
#             transaction_references=dpt_cer_result[0], 
#             username=username_approve,
#             password=password_approve,
#             allow_approve='N',
#             list_error_message=list_error_message
#         )
#         self.transaction_reject(
#             transaction_references=dpt_cer_result[0], 
#             username=username_reverse,
#             password=password_reverse
#         )

#     def test_009_dpt_cer_15_fee_check_available_balance_invalid_current_normal(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             f'InvalidAvailableAmt: Invalid available balance of account [{self.no_mask(deposit_current_normal)}]. Available balance must be more than [{self.format_number(value_invalid)}] - en'
#         ]
#         self.dpt_cer(
#             account_number=deposit_prepaid_normal_valid,
#             cerfiticate_serial=from_serial_fr,
#             list_error_message=list_error_message,
#             ifc_codes=ifc_codes,
#             values=values_invalid,
#             fee_collect_method='Deposit',
#             account_number_for_fee=deposit_current_normal,
#         )

#     def test_009_dpt_cer_16_fee_check_available_balance_invalid_savings_closed(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             f'InvalidAvailableAmt: Invalid available balance of account [{self.no_mask(deposit_savings_close)}]. Available balance must be more than [{self.format_number(value_valid)}] - en'
#         ]
#         self.dpt_cer(
#             account_number=deposit_prepaid_normal_valid,
#             cerfiticate_serial=from_serial_fr,
#             list_error_message=list_error_message,
#             ifc_codes=ifc_codes,
#             values=values_valid,
#             fee_collect_method='Deposit',
#             account_number_for_fee=deposit_savings_close,
#         )

#     def test_009_dpt_cer_17_fee_check_available_balance_invalid_savings_pending(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             f'InvalidAvailableAmt: Invalid available balance of account [{self.no_mask(deposit_savings_pending)}]. Available balance must be more than [{self.format_number(value_valid)}] - en'
#         ]
#         self.dpt_cer(
#             account_number=deposit_prepaid_normal_valid,
#             cerfiticate_serial=from_serial_fr,
#             list_error_message=list_error_message,
#             ifc_codes=ifc_codes,
#             values=values_valid,
#             fee_collect_method='Deposit',
#             account_number_for_fee=deposit_savings_pending,
#         )

#     def test_009_dpt_cer_18_fee_check_available_balance_invalid_savings_reject(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             f'InvalidAvailableAmt: Invalid available balance of account [{self.no_mask(deposit_savings_reject)}]. Available balance must be more than [{self.format_number(value_valid)}] - en'
#         ]
#         self.dpt_cer(
#             account_number=deposit_prepaid_normal_valid,
#             cerfiticate_serial=from_serial_fr,
#             list_error_message=list_error_message,
#             ifc_codes=ifc_codes,
#             values=values_valid,
#             fee_collect_method='Deposit',
#             account_number_for_fee=deposit_savings_reject,
#         )

#     def test_009_dpt_cer_19_fee_check_available_balance_invalid_savings_new(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             f'InvalidAvailableAmt: Invalid available balance of account [{self.no_mask(deposit_savings_new)}]. Available balance must be more than [{self.format_number(value_valid)}] - en'
#         ]
#         self.dpt_cer(
#             account_number=deposit_prepaid_normal_valid,
#             cerfiticate_serial=from_serial_fr,
#             list_error_message=list_error_message,
#             ifc_codes=ifc_codes,
#             values=values_valid,
#             fee_collect_method='Deposit',
#             account_number_for_fee=deposit_savings_new,
#         )

#     def test_009_dpt_cer_20_fee_check_available_balance_invalid_savings_dormant(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             f'Invalid account status [{status_dormant}]'
#         ]
#         dpt_cer_result = self.dpt_cer(
#             account_number=deposit_prepaid_normal_valid,
#             cerfiticate_serial=from_serial_fr,
#             ifc_codes=ifc_codes,
#             values=values_valid,
#             fee_collect_method='Deposit',
#             account_number_for_fee=deposit_savings_dormant,
#             approve_later='Y',
#         )
#         self.transaction_approve(
#             transaction_references=dpt_cer_result[0], 
#             username=username_approve,
#             password=password_approve,
#             allow_approve='N',
#             list_error_message=list_error_message
#         )
#         self.transaction_reject(
#             transaction_references=dpt_cer_result[0], 
#             username=username_reverse,
#             password=password_reverse
#         )

#     def test_009_dpt_cer_21_fee_check_available_balance_invalid_savings_normal(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             f'InvalidAvailableAmt: Invalid available balance of account [{self.no_mask(deposit_savings_normal)}]. Available balance must be more than [{self.format_number(value_invalid)}] - en'
#         ]
#         self.dpt_cer(
#             account_number=deposit_prepaid_normal_valid,
#             cerfiticate_serial=from_serial_fr,
#             list_error_message=list_error_message,
#             ifc_codes=ifc_codes,
#             values=values_invalid,
#             fee_collect_method='Deposit',
#             account_number_for_fee=deposit_savings_normal,
#         )

#     def test_009_dpt_cer_22_fee_check_not_allowed_deposit_type_fixed_deposit(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             f'Invalid deposit type of account [{self.no_mask(deposit_fixed_01m_normal)}]- en'
#         ]
#         dpt_cer_result = self.dpt_cer(
#             account_number=deposit_prepaid_normal_valid,
#             cerfiticate_serial=from_serial_fr,
#             ifc_codes=ifc_codes,
#             values=values_valid,
#             fee_collect_method='Deposit',
#             account_number_for_fee=deposit_fixed_01m_normal,
#             approve_later='Y',
#         )
#         self.transaction_approve(
#             transaction_references=dpt_cer_result[0], 
#             username=username_approve,
#             password=password_approve,
#             allow_approve='N',
#             list_error_message=list_error_message
#         )
#         self.transaction_reject(
#             transaction_references=dpt_cer_result[0], 
#             username=username_reverse,
#             password=password_reverse
#         )

#     def test_009_dpt_cer_23_fee_check_not_allowed_deposit_type_prepaid(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             f'Invalid deposit type of account [{self.no_mask(deposit_prepaid_normal)}]- en'
#         ]
#         dpt_cer_result = self.dpt_cer(
#             account_number=deposit_prepaid_normal_valid,
#             cerfiticate_serial=from_serial_fr,
#             ifc_codes=ifc_codes,
#             values=values_valid,
#             fee_collect_method='Deposit',
#             account_number_for_fee=deposit_prepaid_normal,
#             approve_later='Y',
#         )
#         self.transaction_approve(
#             transaction_references=dpt_cer_result[0], 
#             username=username_approve,
#             password=password_approve,
#             allow_approve='N',
#             list_error_message=list_error_message
#         )
#         self.transaction_reject(
#             transaction_references=dpt_cer_result[0], 
#             username=username_reverse,
#             password=password_reverse
#         )

# # DPT_FBI - INVALID CASE
#     def test_010_dpt_fbi_00_create_data_use_for_testing(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         global deposit_fixed_01m_normal_valid
#         dpt_opn_result = self.dpt_opn(
#             customer_code=customer_code_personal,
#             customer_type='Single customer',
#             catalogue_code=catalogue_code_fixed_01m,
#             reason_of_account_opening='Enter value reason of account opening'
#         )
#         deposit_fixed_01m_normal_valid=dpt_opn_result[1]
#         self.dpt_apr(
#             account_number=deposit_fixed_01m_normal_valid,
#             approve_on_form='Y',
#             username=username_approve,
#             password=password_approve
#         )
#         self.dpt_cdp(
#             account_number=deposit_fixed_01m_normal_valid,
#             amount_deposit=deposit_amount_fixed_01m,
#             approve_on_form='Y',
#             username=username_approve,
#             password=password_approve
#         )
#         global from_serial_fb_01, to_serial_fb_01
#         generated_number = self.gen_serial_number(stock_prefix_fb, stock_type_fb, 0)
#         print(f'generated_number 01m: {generated_number}')
#         from_serial = generated_number[0]
#         to_serial = generated_number[1]
#         dpt_srg_result = self.dpt_srg(
#             stock_type=stock_type_fb,
#             from_serial=from_serial,
#             to_serial=to_serial,
#             stock_prefix=stock_prefix_fb,
#             approve_on_form='Y',
#             username=username_approve,
#             password=password_approve
#         )
#         from_serial_fb_01 = dpt_srg_result[1]
#         to_serial_fb_01 = dpt_srg_result[2]
#         self.dpt_sat(
#             stock_type=stock_type_fb,
#             from_serial=from_serial_fb_01,
#             to_serial=to_serial_fb_01,
#             assigned_staff_code=username_login
#         )
#         self.dpt_ccr(
#             stock_type=stock_type_fb,
#             from_serial=from_serial_fb_01,
#             to_serial=to_serial_fb_01,
#             approve_on_form='Y',
#             username=username_approve,
#             password=password_approve
#         )
#         global deposit_fixed_03m_normal_valid
#         dpt_opn_result = self.dpt_opn(
#             customer_code=customer_code_personal,
#             customer_type='Single customer',
#             catalogue_code=catalogue_code_fixed_01m,
#             reason_of_account_opening='Enter value reason of account opening'
#         )
#         deposit_fixed_03m_normal_valid=dpt_opn_result[1]
#         self.dpt_apr(
#             account_number=deposit_fixed_03m_normal_valid,
#             approve_on_form='Y',
#             username=username_approve,
#             password=password_approve
#         )
#         self.dpt_cdp(
#             account_number=deposit_fixed_03m_normal_valid,
#             amount_deposit=deposit_amount_fixed_01m,
#             approve_on_form='Y',
#             username=username_approve,
#             password=password_approve
#         )
#         global from_serial_fb_03, to_serial_fb_03
#         generated_number = self.gen_serial_number(stock_prefix_fb, stock_type_fb, 0)
#         print(f'generated_number 03m: {generated_number}')
#         from_serial = generated_number[0]
#         to_serial = generated_number[1]
#         dpt_srg_result = self.dpt_srg(
#             stock_type=stock_type_fb,
#             from_serial=from_serial,
#             to_serial=to_serial,
#             stock_prefix=stock_prefix_fb,
#             approve_on_form='Y',
#             username=username_approve,
#             password=password_approve
#         )
#         from_serial_fb_03 = dpt_srg_result[1]
#         to_serial_fb_03 = dpt_srg_result[2]
#         self.dpt_sat(
#             stock_type=stock_type_fb,
#             from_serial=from_serial_fb_03,
#             to_serial=to_serial_fb_03,
#             assigned_staff_code=username_login
#         )
#         self.dpt_ccr(
#             stock_type=stock_type_fb,
#             from_serial=from_serial_fb_03,
#             to_serial=to_serial_fb_03,
#             approve_on_form='Y',
#             username=username_approve,
#             password=password_approve
#         )
#         global deposit_fixed_06m_normal_valid
#         dpt_opn_result = self.dpt_opn(
#             customer_code=customer_code_personal,
#             customer_type='Single customer',
#             catalogue_code=catalogue_code_fixed_01m,
#             reason_of_account_opening='Enter value reason of account opening'
#         )
#         deposit_fixed_06m_normal_valid=dpt_opn_result[1]
#         self.dpt_apr(
#             account_number=deposit_fixed_06m_normal_valid,
#             approve_on_form='Y',
#             username=username_approve,
#             password=password_approve
#         )
#         self.dpt_cdp(
#             account_number=deposit_fixed_06m_normal_valid,
#             amount_deposit=deposit_amount_fixed_01m,
#             approve_on_form='Y',
#             username=username_approve,
#             password=password_approve
#         )
#         global from_serial_fb_06, to_serial_fb_06
#         generated_number = self.gen_serial_number(stock_prefix_fb, stock_type_fb, 0)
#         print(f'generated_number 06m: {generated_number}')
#         from_serial = generated_number[0]
#         to_serial = generated_number[1]
#         dpt_srg_result = self.dpt_srg(
#             stock_type=stock_type_fb,
#             from_serial=from_serial,
#             to_serial=to_serial,
#             stock_prefix=stock_prefix_fb,
#             approve_on_form='Y',
#             username=username_approve,
#             password=password_approve
#         )
#         from_serial_fb_06 = dpt_srg_result[1]
#         to_serial_fb_06 = dpt_srg_result[2]
#         self.dpt_sat(
#             stock_type=stock_type_fb,
#             from_serial=from_serial_fb_06,
#             to_serial=to_serial_fb_06,
#             assigned_staff_code=username_login
#         )
#         self.dpt_ccr(
#             stock_type=stock_type_fb,
#             from_serial=from_serial_fb_06,
#             to_serial=to_serial_fb_06,
#             approve_on_form='Y',
#             username=username_approve,
#             password=password_approve
#         )
#         global deposit_fixed_09m_normal_valid
#         dpt_opn_result = self.dpt_opn(
#             customer_code=customer_code_personal,
#             customer_type='Single customer',
#             catalogue_code=catalogue_code_fixed_01m,
#             reason_of_account_opening='Enter value reason of account opening'
#         )
#         deposit_fixed_09m_normal_valid=dpt_opn_result[1]
#         self.dpt_apr(
#             account_number=deposit_fixed_09m_normal_valid,
#             approve_on_form='Y',
#             username=username_approve,
#             password=password_approve
#         )
#         self.dpt_cdp(
#             account_number=deposit_fixed_09m_normal_valid,
#             amount_deposit=deposit_amount_fixed_01m,
#             approve_on_form='Y',
#             username=username_approve,
#             password=password_approve
#         )
#         global from_serial_fb_09, to_serial_fb_09
#         generated_number = self.gen_serial_number(stock_prefix_fb, stock_type_fb, 0)
#         print(f'generated_number 09m: {generated_number}')
#         from_serial = generated_number[0]
#         to_serial = generated_number[1]
#         dpt_srg_result = self.dpt_srg(
#             stock_type=stock_type_fb,
#             from_serial=from_serial,
#             to_serial=to_serial,
#             stock_prefix=stock_prefix_fb,
#             approve_on_form='Y',
#             username=username_approve,
#             password=password_approve
#         )
#         from_serial_fb_09 = dpt_srg_result[1]
#         to_serial_fb_09 = dpt_srg_result[2]
#         self.dpt_sat(
#             stock_type=stock_type_fb,
#             from_serial=from_serial_fb_09,
#             to_serial=to_serial_fb_09,
#             assigned_staff_code=username_login
#         )
#         self.dpt_ccr(
#             stock_type=stock_type_fb,
#             from_serial=from_serial_fb_09,
#             to_serial=to_serial_fb_09,
#             approve_on_form='Y',
#             username=username_approve,
#             password=password_approve
#         )
#         global deposit_fixed_12m_normal_valid
#         dpt_opn_result = self.dpt_opn(
#             customer_code=customer_code_personal,
#             customer_type='Single customer',
#             catalogue_code=catalogue_code_fixed_01m,
#             reason_of_account_opening='Enter value reason of account opening'
#         )
#         deposit_fixed_12m_normal_valid=dpt_opn_result[1]
#         self.dpt_apr(
#             account_number=deposit_fixed_12m_normal_valid,
#             approve_on_form='Y',
#             username=username_approve,
#             password=password_approve
#         )
#         self.dpt_cdp(
#             account_number=deposit_fixed_12m_normal_valid,
#             amount_deposit=deposit_amount_fixed_01m,
#             approve_on_form='Y',
#             username=username_approve,
#             password=password_approve
#         )
#         global from_serial_fb_12, to_serial_fb_12
#         generated_number = self.gen_serial_number(stock_prefix_fb, stock_type_fb, 0)
#         print(f'generated_number 12m: {generated_number}')
#         from_serial = generated_number[0]
#         to_serial = generated_number[1]
#         dpt_srg_result = self.dpt_srg(
#             stock_type=stock_type_fb,
#             from_serial=from_serial,
#             to_serial=to_serial,
#             stock_prefix=stock_prefix_fb,
#             approve_on_form='Y',
#             username=username_approve,
#             password=password_approve
#         )
#         from_serial_fb_12 = dpt_srg_result[1]
#         to_serial_fb_12 = dpt_srg_result[2]
#         self.dpt_sat(
#             stock_type=stock_type_fb,
#             from_serial=from_serial_fb_12,
#             to_serial=to_serial_fb_12,
#             assigned_staff_code=username_login
#         )
#         self.dpt_ccr(
#             stock_type=stock_type_fb,
#             from_serial=from_serial_fb_12,
#             to_serial=to_serial_fb_12,
#             approve_on_form='Y',
#             username=username_approve,
#             password=password_approve
#         )

#     def test_010_dpt_fbi_01_check_not_allowed_deposit_type_current(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             'InvalidDptSubType: Deposit Subtype is invalid'
#         ]
#         self.dpt_fbi(
#             account_number=deposit_current_normal,
#             serial_no=from_serial_fb_01,
#             list_error_message=list_error_message,
#         )

#     def test_010_dpt_fbi_02_check_not_allowed_deposit_type_savings(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             'InvalidDptSubType: Deposit Subtype is invalid'
#         ]
#         self.dpt_fbi(
#             account_number=deposit_savings_normal,
#             serial_no=from_serial_fb_01,
#             list_error_message=list_error_message,
#         )

#     def test_010_dpt_fbi_03_check_not_allowed_deposit_type_prepaid(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             'InvalidDptSubType: Deposit Subtype is invalid'
#         ]
#         self.dpt_fbi(
#             account_number=deposit_prepaid_normal,
#             serial_no=from_serial_fb_01,
#             list_error_message=list_error_message,
#         )

#     def test_010_dpt_fbi_04_check_not_allowed_deposit_status_block(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             f'InvalidDepositStatus: Invalid deposit status [{status_block}]'
#         ]
#         self.dpt_fbi(
#             account_number=deposit_fixed_01m_block,
#             serial_no=from_serial_fb_01,
#             list_error_message=list_error_message,
#         )

#     def test_010_dpt_fbi_05_check_not_allowed_deposit_status_closed(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             f'InvalidDepositStatus: Invalid deposit status [{status_closed}]'
#         ]
#         self.dpt_fbi(
#             account_number=deposit_fixed_01m_close,
#             serial_no=from_serial_fb_01,
#             list_error_message=list_error_message,
#         )

#     def test_010_dpt_fbi_06_check_not_allowed_deposit_status_pending(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             f'InvalidDepositStatus: Invalid deposit status [{status_pending}]'
#         ]
#         self.dpt_fbi(
#             account_number=deposit_fixed_01m_pending,
#             serial_no=from_serial_fb_01,
#             list_error_message=list_error_message,
#         )

#     def test_010_dpt_fbi_07_check_not_allowed_deposit_status_reject(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             f'InvalidDepositStatus: Invalid deposit status [{status_reject}]'
#         ]
#         self.dpt_fbi(
#             account_number=deposit_fixed_01m_reject,
#             serial_no=from_serial_fb_01,
#             list_error_message=list_error_message,
#         )

#     def test_010_dpt_fbi_08_fee_check_not_allowed_deposit_status_current_block(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             f'InvalidDepositStatus: Invalid deposit status [{status_block}]'
#         ]
#         self.dpt_fbi(
#             account_number=deposit_fixed_01m_normal_valid,
#             serial_no=from_serial_fb_01,
#             list_error_message=list_error_message,
#             ifc_codes=ifc_codes,
#             values=values_valid,
#             fee_collect_method='Deposit',
#             account_number_for_fee=deposit_current_block,
#         )

#     def test_010_dpt_fbi_09_fee_check_not_allowed_deposit_status_savings_block(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             f'InvalidDepositStatus: Invalid deposit status [{status_block}]'
#         ]
#         self.dpt_fbi(
#             account_number=deposit_fixed_01m_normal_valid,
#             serial_no=from_serial_fb_01,
#             list_error_message=list_error_message,
#             ifc_codes=ifc_codes,
#             values=values_valid,
#             fee_collect_method='Deposit',
#             account_number_for_fee=deposit_savings_block,
#         )

#     def test_010_dpt_fbi_10_fee_check_available_balance_invalid_current_closed(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             f'InvalidAvailableAmt: Invalid available balance of account [{self.no_mask(deposit_current_close)}]. Available balance must be more than [{self.format_number(value_valid)}] - en'
#         ]
#         self.dpt_fbi(
#             account_number=deposit_fixed_01m_normal_valid,
#             serial_no=from_serial_fb_01,
#             list_error_message=list_error_message,
#             ifc_codes=ifc_codes,
#             values=values_valid,
#             fee_collect_method='Deposit',
#             account_number_for_fee=deposit_current_close,
#         )

#     def test_010_dpt_fbi_11_fee_check_available_balance_invalid_current_pending(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             f'InvalidAvailableAmt: Invalid available balance of account [{self.no_mask(deposit_current_pending)}]. Available balance must be more than [{self.format_number(value_valid)}] - en'
#         ]
#         self.dpt_fbi(
#             account_number=deposit_fixed_01m_normal_valid,
#             serial_no=from_serial_fb_01,
#             list_error_message=list_error_message,
#             ifc_codes=ifc_codes,
#             values=values_valid,
#             fee_collect_method='Deposit',
#             account_number_for_fee=deposit_current_pending,
#         )

#     def test_010_dpt_fbi_12_fee_check_available_balance_invalid_current_reject(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             f'InvalidAvailableAmt: Invalid available balance of account [{self.no_mask(deposit_current_reject)}]. Available balance must be more than [{self.format_number(value_valid)}] - en'
#         ]
#         self.dpt_fbi(
#             account_number=deposit_fixed_01m_normal_valid,
#             serial_no=from_serial_fb_01,
#             list_error_message=list_error_message,
#             ifc_codes=ifc_codes,
#             values=values_valid,
#             fee_collect_method='Deposit',
#             account_number_for_fee=deposit_current_reject,
#         )

#     def test_010_dpt_fbi_13_fee_check_available_balance_invalid_current_new(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             f'InvalidAvailableAmt: Invalid available balance of account [{self.no_mask(deposit_current_new)}]. Available balance must be more than [{self.format_number(value_valid)}] - en'
#         ]
#         self.dpt_fbi(
#             account_number=deposit_fixed_01m_normal_valid,
#             serial_no=from_serial_fb_01,
#             list_error_message=list_error_message,
#             ifc_codes=ifc_codes,
#             values=values_valid,
#             fee_collect_method='Deposit',
#             account_number_for_fee=deposit_current_new,
#         )

#     def test_010_dpt_fbi_14_fee_check_available_balance_invalid_current_dormant(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             f'Invalid account status [{status_dormant}]'
#         ]
#         dpt_fbi_result = self.dpt_fbi(
#             account_number=deposit_fixed_01m_normal_valid,
#             serial_no=from_serial_fb_01,
#             ifc_codes=ifc_codes,
#             values=values_valid,
#             fee_collect_method='Deposit',
#             account_number_for_fee=deposit_current_dormant,
#             approve_later='Y',
#         )
#         self.transaction_approve(
#             transaction_references=dpt_fbi_result[0], 
#             username=username_approve,
#             password=password_approve,
#             allow_approve='N',
#             list_error_message=list_error_message
#         )
#         self.transaction_reject(
#             transaction_references=dpt_fbi_result[0], 
#             username=username_reverse,
#             password=password_reverse
#         )

#     def test_010_dpt_fbi_15_fee_check_available_balance_invalid_current_normal(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             f'InvalidAvailableAmt: Invalid available balance of account [{self.no_mask(deposit_current_normal)}]. Available balance must be more than [{self.format_number(value_invalid)}] - en'
#         ]
#         self.dpt_fbi(
#             account_number=deposit_fixed_01m_normal_valid,
#             serial_no=from_serial_fb_01,
#             list_error_message=list_error_message,
#             ifc_codes=ifc_codes,
#             values=values_invalid,
#             fee_collect_method='Deposit',
#             account_number_for_fee=deposit_current_normal,
#         )

#     def test_010_dpt_fbi_16_fee_check_available_balance_invalid_savings_closed(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             f'InvalidAvailableAmt: Invalid available balance of account [{self.no_mask(deposit_savings_close)}]. Available balance must be more than [{self.format_number(value_valid)}] - en'
#         ]
#         self.dpt_fbi(
#             account_number=deposit_fixed_01m_normal_valid,
#             serial_no=from_serial_fb_01,
#             list_error_message=list_error_message,
#             ifc_codes=ifc_codes,
#             values=values_valid,
#             fee_collect_method='Deposit',
#             account_number_for_fee=deposit_savings_close,
#         )

#     def test_010_dpt_fbi_17_fee_check_available_balance_invalid_savings_pending(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             f'InvalidAvailableAmt: Invalid available balance of account [{self.no_mask(deposit_savings_pending)}]. Available balance must be more than [{self.format_number(value_valid)}] - en'
#         ]
#         self.dpt_fbi(
#             account_number=deposit_fixed_01m_normal_valid,
#             serial_no=from_serial_fb_01,
#             list_error_message=list_error_message,
#             ifc_codes=ifc_codes,
#             values=values_valid,
#             fee_collect_method='Deposit',
#             account_number_for_fee=deposit_savings_pending,
#         )

#     def test_010_dpt_fbi_18_fee_check_available_balance_invalid_savings_reject(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             f'InvalidAvailableAmt: Invalid available balance of account [{self.no_mask(deposit_savings_reject)}]. Available balance must be more than [{self.format_number(value_valid)}] - en'
#         ]
#         self.dpt_fbi(
#             account_number=deposit_fixed_01m_normal_valid,
#             serial_no=from_serial_fb_01,
#             list_error_message=list_error_message,
#             ifc_codes=ifc_codes,
#             values=values_valid,
#             fee_collect_method='Deposit',
#             account_number_for_fee=deposit_savings_reject,
#         )

#     def test_010_dpt_fbi_19_fee_check_available_balance_invalid_savings_new(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             f'InvalidAvailableAmt: Invalid available balance of account [{self.no_mask(deposit_savings_new)}]. Available balance must be more than [{self.format_number(value_valid)}] - en'
#         ]
#         self.dpt_fbi(
#             account_number=deposit_fixed_01m_normal_valid,
#             serial_no=from_serial_fb_01,
#             list_error_message=list_error_message,
#             ifc_codes=ifc_codes,
#             values=values_valid,
#             fee_collect_method='Deposit',
#             account_number_for_fee=deposit_savings_new,
#         )

#     def test_010_dpt_fbi_20_fee_check_available_balance_invalid_savings_dormant(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             f'Invalid account status [{status_dormant}]'
#         ]
#         dpt_fbi_result = self.dpt_fbi(
#             account_number=deposit_fixed_01m_normal_valid,
#             serial_no=from_serial_fb_01,
#             ifc_codes=ifc_codes,
#             values=values_valid,
#             fee_collect_method='Deposit',
#             account_number_for_fee=deposit_savings_dormant,
#             approve_later='Y',
#         )
#         self.transaction_approve(
#             transaction_references=dpt_fbi_result[0], 
#             username=username_approve,
#             password=password_approve,
#             allow_approve='N',
#             list_error_message=list_error_message
#         )
#         self.transaction_reject(
#             transaction_references=dpt_fbi_result[0], 
#             username=username_reverse,
#             password=password_reverse
#         )

#     def test_010_dpt_fbi_21_fee_check_available_balance_invalid_savings_normal(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             f'InvalidAvailableAmt: Invalid available balance of account [{self.no_mask(deposit_savings_normal)}]. Available balance must be more than [{self.format_number(value_invalid)}] - en'
#         ]
#         self.dpt_fbi(
#             account_number=deposit_fixed_01m_normal_valid,
#             serial_no=from_serial_fb_01,
#             list_error_message=list_error_message,
#             ifc_codes=ifc_codes,
#             values=values_invalid,
#             fee_collect_method='Deposit',
#             account_number_for_fee=deposit_savings_normal,
#         )

#     def test_010_dpt_fbi_22_fee_check_not_allowed_deposit_type_fixed_deposit(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             f'Invalid deposit type [Fixed Deposit] of account [{self.no_mask(deposit_fixed_01m_normal)}]- en'
#         ]
#         dpt_fbi_result = self.dpt_fbi(
#             account_number=deposit_fixed_01m_normal_valid,
#             serial_no=from_serial_fb_01,
#             ifc_codes=ifc_codes,
#             values=values_valid,
#             fee_collect_method='Deposit',
#             account_number_for_fee=deposit_fixed_01m_normal,
#             approve_later='Y',
#         )
#         self.transaction_approve(
#             transaction_references=dpt_fbi_result[0], 
#             username=username_approve,
#             password=password_approve,
#             allow_approve='N',
#             list_error_message=list_error_message
#         )
#         self.transaction_reject(
#             transaction_references=dpt_fbi_result[0], 
#             username=username_reverse,
#             password=password_reverse
#         )

#     def test_010_dpt_fbi_23_fee_check_not_allowed_deposit_type_prepaid(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             f'Invalid deposit type [Fixed Deposit] of account [{self.no_mask(deposit_prepaid_normal)}]- en'
#         ]
#         dpt_fbi_result = self.dpt_fbi(
#             account_number=deposit_fixed_01m_normal_valid,
#             serial_no=from_serial_fb_01,
#             ifc_codes=ifc_codes,
#             values=values_valid,
#             fee_collect_method='Deposit',
#             account_number_for_fee=deposit_prepaid_normal,
#             approve_later='Y',
#         )
#         self.transaction_approve(
#             transaction_references=dpt_fbi_result[0], 
#             username=username_approve,
#             password=password_approve,
#             allow_approve='N',
#             list_error_message=list_error_message
#         )
#         self.transaction_reject(
#             transaction_references=dpt_fbi_result[0], 
#             username=username_reverse,
#             password=password_reverse
#         )

# # DPT_SBI - INVALID CASE
#     def test_011_dpt_sbi_00_create_data_use_for_testing(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         global deposit_savings_normal_valid
#         dpt_opn_result = self.dpt_opn(
#             customer_code=customer_code_personal,
#             customer_type='Single customer',
#             catalogue_code=catalogue_code_savings,
#             reason_of_account_opening='Enter value reason of account opening'
#         )
#         deposit_savings_normal_valid=dpt_opn_result[1]
#         self.dpt_apr(
#             account_number=deposit_savings_normal_valid,
#             approve_on_form='Y',
#             username=username_approve,
#             password=password_approve
#         )
#         self.dpt_cdp(
#             account_number=deposit_savings_normal_valid,
#             amount_deposit=deposit_amount_savings,
#             approve_on_form='Y',
#             username=username_approve,
#             password=password_approve
#         )
#         global from_serial_sb, to_serial_sb
#         generated_number = self.gen_serial_number(stock_prefix_sb, stock_type_sb, 0)
#         print(f'generated_number: {generated_number}')
#         from_serial = generated_number[0]
#         to_serial = generated_number[1]
#         dpt_srg_result = self.dpt_srg(
#             stock_type=stock_type_sb,
#             from_serial=from_serial,
#             to_serial=to_serial,
#             stock_prefix=stock_prefix_sb,
#             approve_on_form='Y',
#             username=username_approve,
#             password=password_approve
#         )
#         from_serial_sb = dpt_srg_result[1]
#         to_serial_sb = dpt_srg_result[2]
#         self.dpt_sat(
#             stock_type=stock_type_sb,
#             from_serial=from_serial_sb,
#             to_serial=to_serial_sb,
#             assigned_staff_code=username_login
#         )
#         self.dpt_ccr(
#             stock_type=stock_type_sb,
#             from_serial=from_serial_sb,
#             to_serial=to_serial_sb,
#             approve_on_form='Y',
#             username=username_approve,
#             password=password_approve
#         )

#     def test_011_dpt_sbi_01_check_not_allowed_deposit_type_current(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             f'Invalid deposit type [Current] of account [{self.no_mask(deposit_current_normal)}]- en'
#         ]
#         dpt_sbi_result = self.dpt_sbi(
#             account_number=deposit_current_normal,
#             serial_no=from_serial_sb,
#             approve_later='Y',
#         )
#         self.transaction_approve(
#             transaction_references=dpt_sbi_result[0], 
#             username=username_approve,
#             password=password_approve,
#             allow_approve='N',
#             list_error_message=list_error_message
#         )
#         self.transaction_reject(
#             transaction_references=dpt_sbi_result[0], 
#             username=username_reverse,
#             password=password_reverse
#         )

#     def test_011_dpt_sbi_02_check_not_allowed_deposit_type_fixed_deposit(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             f'Invalid deposit type [Fixed Deposit] of account [{self.no_mask(deposit_fixed_01m_normal_valid)}]- en'
#         ]
#         dpt_sbi_result = self.dpt_sbi(
#             account_number=deposit_fixed_01m_normal_valid,
#             serial_no=from_serial_sb,
#             approve_later='Y',
#         )
#         self.transaction_approve(
#             transaction_references=dpt_sbi_result[0], 
#             username=username_approve,
#             password=password_approve,
#             allow_approve='N',
#             list_error_message=list_error_message
#         )
#         self.transaction_reject(
#             transaction_references=dpt_sbi_result[0], 
#             username=username_reverse,
#             password=password_reverse
#         )

#     def test_011_dpt_sbi_03_check_not_allowed_deposit_type_prepaid(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             f'Invalid deposit type [Fixed Deposit] of account [{self.no_mask(deposit_prepaid_normal_valid)}]- en'
#         ]
#         dpt_sbi_result = self.dpt_sbi(
#             account_number=deposit_prepaid_normal_valid,
#             serial_no=from_serial_sb,
#             approve_later='Y',
#         )
#         self.transaction_approve(
#             transaction_references=dpt_sbi_result[0], 
#             username=username_approve,
#             password=password_approve,
#             allow_approve='N',
#             list_error_message=list_error_message
#         )
#         self.transaction_reject(
#             transaction_references=dpt_sbi_result[0], 
#             username=username_reverse,
#             password=password_reverse
#         )

#     def test_011_dpt_sbi_04_check_not_allowed_deposit_status_block(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             f'InvalidDepositStatus: Invalid deposit status [{status_block}]'
#         ]
#         self.dpt_sbi(
#             account_number=deposit_savings_block,
#             serial_no=from_serial_sb,
#             list_error_message=list_error_message,
#         )

#     def test_011_dpt_sbi_05_check_not_allowed_deposit_status_closed(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             f'InvalidDepositStatus: Invalid deposit status [{status_closed}]'
#         ]
#         self.dpt_sbi(
#             account_number=deposit_savings_close,
#             serial_no=from_serial_sb,
#             list_error_message=list_error_message,
#         )

#     def test_011_dpt_sbi_06_check_not_allowed_deposit_status_pending(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             f'InvalidDepositStatus: Invalid deposit status [{status_pending}]'
#         ]
#         self.dpt_sbi(
#             account_number=deposit_savings_pending,
#             serial_no=from_serial_sb,
#             list_error_message=list_error_message,
#         )

#     def test_011_dpt_sbi_07_check_not_allowed_deposit_status_reject(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             f'InvalidDepositStatus: Invalid deposit status [{status_reject}]'
#         ]
#         self.dpt_sbi(
#             account_number=deposit_savings_reject,
#             serial_no=from_serial_sb,
#             list_error_message=list_error_message,
#         )

#     def test_011_dpt_sbi_08_fee_check_not_allowed_deposit_status_current_block(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             f'InvalidDepositStatus: Invalid deposit status [{status_block}]'
#         ]
#         self.dpt_sbi(
#             account_number=deposit_savings_normal_valid,
#             serial_no=from_serial_sb,
#             list_error_message=list_error_message,
#             ifc_codes=ifc_codes,
#             values=values_valid,
#             fee_collect_method='Deposit',
#             account_number_for_fee=deposit_current_block,
#         )

#     def test_011_dpt_sbi_09_fee_check_not_allowed_deposit_status_savings_block(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             f'InvalidDepositStatus: Invalid deposit status [{status_block}]'
#         ]
#         self.dpt_sbi(
#             account_number=deposit_savings_normal_valid,
#             serial_no=from_serial_sb,
#             list_error_message=list_error_message,
#             ifc_codes=ifc_codes,
#             values=values_valid,
#             fee_collect_method='Deposit',
#             account_number_for_fee=deposit_savings_block,
#         )

#     def test_011_dpt_sbi_10_fee_check_available_balance_invalid_current_closed(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             f'InvalidAvailableAmt: Invalid available balance of account [{self.no_mask(deposit_current_close)}]. Available balance must be more than [{self.format_number(value_valid)}] - en'
#         ]
#         self.dpt_sbi(
#             account_number=deposit_savings_normal_valid,
#             serial_no=from_serial_sb,
#             list_error_message=list_error_message,
#             ifc_codes=ifc_codes,
#             values=values_valid,
#             fee_collect_method='Deposit',
#             account_number_for_fee=deposit_current_close,
#         )

#     def test_011_dpt_sbi_11_fee_check_available_balance_invalid_current_pending(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             f'InvalidAvailableAmt: Invalid available balance of account [{self.no_mask(deposit_current_pending)}]. Available balance must be more than [{self.format_number(value_valid)}] - en'
#         ]
#         self.dpt_sbi(
#             account_number=deposit_savings_normal_valid,
#             serial_no=from_serial_sb,
#             list_error_message=list_error_message,
#             ifc_codes=ifc_codes,
#             values=values_valid,
#             fee_collect_method='Deposit',
#             account_number_for_fee=deposit_current_pending,
#         )

#     def test_011_dpt_sbi_12_fee_check_available_balance_invalid_current_reject(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             f'InvalidAvailableAmt: Invalid available balance of account [{self.no_mask(deposit_current_reject)}]. Available balance must be more than [{self.format_number(value_valid)}] - en'
#         ]
#         self.dpt_sbi(
#             account_number=deposit_savings_normal_valid,
#             serial_no=from_serial_sb,
#             list_error_message=list_error_message,
#             ifc_codes=ifc_codes,
#             values=values_valid,
#             fee_collect_method='Deposit',
#             account_number_for_fee=deposit_current_reject,
#         )

#     def test_011_dpt_sbi_13_fee_check_available_balance_invalid_current_new(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             f'InvalidAvailableAmt: Invalid available balance of account [{self.no_mask(deposit_current_new)}]. Available balance must be more than [{self.format_number(value_valid)}] - en'
#         ]
#         self.dpt_sbi(
#             account_number=deposit_savings_normal_valid,
#             serial_no=from_serial_sb,
#             list_error_message=list_error_message,
#             ifc_codes=ifc_codes,
#             values=values_valid,
#             fee_collect_method='Deposit',
#             account_number_for_fee=deposit_current_new,
#         )

#     def test_011_dpt_sbi_14_fee_check_available_balance_invalid_current_dormant(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             f'Invalid account status [{status_dormant}]'
#         ]
#         dpt_sbi_result = self.dpt_sbi(
#             account_number=deposit_savings_normal_valid,
#             serial_no=from_serial_sb,
#             ifc_codes=ifc_codes,
#             values=values_valid,
#             fee_collect_method='Deposit',
#             account_number_for_fee=deposit_current_dormant,
#             approve_later='Y',
#         )
#         self.transaction_approve(
#             transaction_references=dpt_sbi_result[0], 
#             username=username_approve,
#             password=password_approve,
#             allow_approve='N',
#             list_error_message=list_error_message
#         )
#         self.transaction_reject(
#             transaction_references=dpt_sbi_result[0], 
#             username=username_reverse,
#             password=password_reverse
#         )

#     def test_011_dpt_sbi_15_fee_check_available_balance_invalid_current_normal(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             f'InvalidAvailableAmt: Invalid available balance of account [{self.no_mask(deposit_current_normal)}]. Available balance must be more than [{self.format_number(value_invalid)}] - en'
#         ]
#         self.dpt_sbi(
#             account_number=deposit_savings_normal_valid,
#             serial_no=from_serial_sb,
#             list_error_message=list_error_message,
#             ifc_codes=ifc_codes,
#             values=values_invalid,
#             fee_collect_method='Deposit',
#             account_number_for_fee=deposit_current_normal,
#         )

#     def test_011_dpt_sbi_16_fee_check_available_balance_invalid_savings_closed(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             f'InvalidAvailableAmt: Invalid available balance of account [{self.no_mask(deposit_savings_close)}]. Available balance must be more than [{self.format_number(value_valid)}] - en'
#         ]
#         self.dpt_sbi(
#             account_number=deposit_savings_normal_valid,
#             serial_no=from_serial_sb,
#             list_error_message=list_error_message,
#             ifc_codes=ifc_codes,
#             values=values_valid,
#             fee_collect_method='Deposit',
#             account_number_for_fee=deposit_savings_close,
#         )

#     def test_011_dpt_sbi_17_fee_check_available_balance_invalid_savings_pending(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             f'InvalidAvailableAmt: Invalid available balance of account [{self.no_mask(deposit_savings_pending)}]. Available balance must be more than [{self.format_number(value_valid)}] - en'
#         ]
#         self.dpt_sbi(
#             account_number=deposit_savings_normal_valid,
#             serial_no=from_serial_sb,
#             list_error_message=list_error_message,
#             ifc_codes=ifc_codes,
#             values=values_valid,
#             fee_collect_method='Deposit',
#             account_number_for_fee=deposit_savings_pending,
#         )

#     def test_011_dpt_sbi_18_fee_check_available_balance_invalid_savings_reject(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             f'InvalidAvailableAmt: Invalid available balance of account [{self.no_mask(deposit_savings_reject)}]. Available balance must be more than [{self.format_number(value_valid)}] - en'
#         ]
#         self.dpt_sbi(
#             account_number=deposit_savings_normal_valid,
#             serial_no=from_serial_sb,
#             list_error_message=list_error_message,
#             ifc_codes=ifc_codes,
#             values=values_valid,
#             fee_collect_method='Deposit',
#             account_number_for_fee=deposit_savings_reject,
#         )

#     def test_011_dpt_sbi_19_fee_check_available_balance_invalid_savings_new(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             f'InvalidAvailableAmt: Invalid available balance of account [{self.no_mask(deposit_savings_new)}]. Available balance must be more than [{self.format_number(value_valid)}] - en'
#         ]
#         self.dpt_sbi(
#             account_number=deposit_savings_normal_valid,
#             serial_no=from_serial_sb,
#             list_error_message=list_error_message,
#             ifc_codes=ifc_codes,
#             values=values_valid,
#             fee_collect_method='Deposit',
#             account_number_for_fee=deposit_savings_new,
#         )

#     def test_011_dpt_sbi_20_fee_check_available_balance_invalid_savings_dormant(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             f'Invalid account status [{status_dormant}]'
#         ]
#         dpt_sbi_result = self.dpt_sbi(
#             account_number=deposit_savings_normal_valid,
#             serial_no=from_serial_sb,
#             ifc_codes=ifc_codes,
#             values=values_valid,
#             fee_collect_method='Deposit',
#             account_number_for_fee=deposit_savings_dormant,
#             approve_later='Y',
#         )
#         self.transaction_approve(
#             transaction_references=dpt_sbi_result[0], 
#             username=username_approve,
#             password=password_approve,
#             allow_approve='N',
#             list_error_message=list_error_message
#         )
#         self.transaction_reject(
#             transaction_references=dpt_sbi_result[0], 
#             username=username_reverse,
#             password=password_reverse
#         )

#     def test_011_dpt_sbi_21_fee_check_available_balance_invalid_savings_normal(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             f'InvalidAvailableAmt: Invalid available balance of account [{self.no_mask(deposit_savings_normal)}]. Available balance must be more than [{self.format_number(value_invalid)}] - en'
#         ]
#         self.dpt_sbi(
#             account_number=deposit_savings_normal_valid,
#             serial_no=from_serial_sb,
#             list_error_message=list_error_message,
#             ifc_codes=ifc_codes,
#             values=values_invalid,
#             fee_collect_method='Deposit',
#             account_number_for_fee=deposit_savings_normal,
#         )

#     def test_011_dpt_sbi_22_fee_check_not_allowed_deposit_type_fixed_deposit(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             f'Invalid deposit type [Fixed Deposit] of account [{self.no_mask(deposit_fixed_01m_normal)}]- en'
#         ]
#         dpt_sbi_result = self.dpt_sbi(
#             account_number=deposit_savings_normal_valid,
#             serial_no=from_serial_sb,
#             ifc_codes=ifc_codes,
#             values=values_valid,
#             fee_collect_method='Deposit',
#             account_number_for_fee=deposit_fixed_01m_normal,
#             approve_later='Y',
#         )
#         self.transaction_approve(
#             transaction_references=dpt_sbi_result[0], 
#             username=username_approve,
#             password=password_approve,
#             allow_approve='N',
#             list_error_message=list_error_message
#         )
#         self.transaction_reject(
#             transaction_references=dpt_sbi_result[0], 
#             username=username_reverse,
#             password=password_reverse
#         )

#     def test_011_dpt_sbi_23_fee_check_not_allowed_deposit_type_prepaid(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         list_error_message = [
#             f'Invalid deposit type [Fixed Deposit] of account [{self.no_mask(deposit_prepaid_normal)}]- en'
#         ]
#         dpt_sbi_result = self.dpt_sbi(
#             account_number=deposit_savings_normal_valid,
#             serial_no=from_serial_sb,
#             ifc_codes=ifc_codes,
#             values=values_valid,
#             fee_collect_method='Deposit',
#             account_number_for_fee=deposit_prepaid_normal,
#             approve_later='Y',
#         )
#         self.transaction_approve(
#             transaction_references=dpt_sbi_result[0], 
#             username=username_approve,
#             password=password_approve,
#             allow_approve='N',
#             list_error_message=list_error_message
#         )
#         self.transaction_reject(
#             transaction_references=dpt_sbi_result[0], 
#             username=username_reverse,
#             password=password_reverse
#         )

# DPT_CEI - INVALID CASE
    def test_012_dpt_cei_00_create_data_use_for_testing(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        global deposit_current_new_dpt_cei, from_serial_cq_new, to_serial_cq_new
        dpt_opn_result = self.dpt_opn(
            customer_code=customer_code_personal,
            customer_type='Single customer',
            catalogue_code=catalogue_code_current,
            reason_of_account_opening='Enter value reason of account opening'
        )
        deposit_current_new_dpt_cei=dpt_opn_result[1]
        self.dpt_apr(
            account_number=deposit_current_new_dpt_cei,
            approve_on_form='Y',
            username=username_approve,
            password=password_approve
        )
        generated_number = self.gen_serial_number(stock_prefix_cq, stock_type_cq, 24)
        print(f'generated_number new: {generated_number}')
        from_serial = generated_number[0]
        to_serial = generated_number[1]
        dpt_srg_result = self.dpt_srg(
            stock_type=stock_type_cq,
            from_serial=from_serial,
            to_serial=to_serial,
            stock_prefix=stock_prefix_cq,
            number_of_leaves=number_of_leaves_cq,
            number_of_book=number_of_book_cq,
            approve_on_form='Y',
            username=username_approve,
            password=password_approve
        )
        from_serial_cq_new = dpt_srg_result[1]
        to_serial_cq_new = dpt_srg_result[2]
        self.dpt_sat(
            stock_type=stock_type_cq,
            from_serial=from_serial_cq_new,
            to_serial=to_serial_cq_new,
            assigned_staff_code=username_login
        )
        self.dpt_ccr(
            stock_type=stock_type_cq,
            from_serial=from_serial_cq_new,
            to_serial=to_serial_cq_new,
            approve_on_form='Y',
            username=username_approve,
            password=password_approve
        )
        self.dpt_cis(
            account_number=deposit_current_new_dpt_cei,
            from_serial=from_serial_cq_new,
            to_serial=to_serial_cq_new,
            approve_on_form='Y',
            username=username_approve,
            password=password_approve,
        )
        global deposit_current_normal_dpt_cei, from_serial_cq_normal, to_serial_cq_normal
        dpt_opn_result = self.dpt_opn(
            customer_code=customer_code_personal,
            customer_type='Single customer',
            catalogue_code=catalogue_code_current,
            reason_of_account_opening='Enter value reason of account opening'
        )
        deposit_current_normal_dpt_cei=dpt_opn_result[1]
        self.dpt_apr(
            account_number=deposit_current_normal_dpt_cei,
            approve_on_form='Y',
            username=username_approve,
            password=password_approve
        )
        self.dpt_cdp(
            account_number=deposit_current_normal_dpt_cei,
            amount_deposit=deposit_amount_current,
            approve_on_form='Y',
            username=username_approve,
            password=password_approve
        )
        generated_number = self.gen_serial_number(stock_prefix_cq, stock_type_cq, 24)
        print(f'generated_number normal: {generated_number}')
        from_serial = generated_number[0]
        to_serial = generated_number[1]
        dpt_srg_result = self.dpt_srg(
            stock_type=stock_type_cq,
            from_serial=from_serial,
            to_serial=to_serial,
            stock_prefix=stock_prefix_cq,
            number_of_leaves=number_of_leaves_cq,
            number_of_book=number_of_book_cq,
            approve_on_form='Y',
            username=username_approve,
            password=password_approve
        )
        from_serial_cq_normal = dpt_srg_result[1]
        to_serial_cq_normal = dpt_srg_result[2]
        self.dpt_sat(
            stock_type=stock_type_cq,
            from_serial=from_serial_cq_normal,
            to_serial=to_serial_cq_normal,
            assigned_staff_code=username_login
        )
        self.dpt_ccr(
            stock_type=stock_type_cq,
            from_serial=from_serial_cq_normal,
            to_serial=to_serial_cq_normal,
            approve_on_form='Y',
            username=username_approve,
            password=password_approve
        )
        self.dpt_cis(
            account_number=deposit_current_normal_dpt_cei,
            from_serial=from_serial_cq_normal,
            to_serial=to_serial_cq_normal,
            approve_on_form='Y',
            username=username_approve,
            password=password_approve,
        )
        global deposit_current_dormant_dpt_cei, from_serial_cq_dormant, to_serial_cq_dormant
        dpt_opn_result = self.dpt_opn(
            customer_code=customer_code_personal,
            customer_type='Single customer',
            catalogue_code=catalogue_code_current,
            reason_of_account_opening='Enter value reason of account opening'
        )
        deposit_current_dormant_dpt_cei=dpt_opn_result[1]
        self.dpt_apr(
            account_number=deposit_current_dormant_dpt_cei,
            approve_on_form='Y',
            username=username_approve,
            password=password_approve
        )
        self.dpt_cdp(
            account_number=deposit_current_dormant_dpt_cei,
            amount_deposit=deposit_amount_current,
            approve_on_form='Y',
            username=username_approve,
            password=password_approve
        )
        self.dpt_cas(
            account_number=deposit_current_dormant_dpt_cei,
            new_status=status_dormant,
            current_status=status_normal,
            approve_on_form='Y',
            username=username_approve,
            password=password_approve
        )
        generated_number = self.gen_serial_number(stock_prefix_cq, stock_type_cq, 24)
        print(f'generated_number dormant: {generated_number}')
        from_serial = generated_number[0]
        to_serial = generated_number[1]
        dpt_srg_result = self.dpt_srg(
            stock_type=stock_type_cq,
            from_serial=from_serial,
            to_serial=to_serial,
            stock_prefix=stock_prefix_cq,
            number_of_leaves=number_of_leaves_cq,
            number_of_book=number_of_book_cq,
            approve_on_form='Y',
            username=username_approve,
            password=password_approve
        )
        from_serial_cq_dormant = dpt_srg_result[1]
        to_serial_cq_dormant = dpt_srg_result[2]
        self.dpt_sat(
            stock_type=stock_type_cq,
            from_serial=from_serial_cq_dormant,
            to_serial=to_serial_cq_dormant,
            assigned_staff_code=username_login
        )
        self.dpt_ccr(
            stock_type=stock_type_cq,
            from_serial=from_serial_cq_dormant,
            to_serial=to_serial_cq_dormant,
            approve_on_form='Y',
            username=username_approve,
            password=password_approve
        )
        self.dpt_cis(
            account_number=deposit_current_dormant_dpt_cei,
            from_serial=from_serial_cq_dormant,
            to_serial=to_serial_cq_dormant,
            approve_on_form='Y',
            username=username_approve,
            password=password_approve,
        )
        global deposit_current_block_dpt_cei, from_serial_cq_block, to_serial_cq_block
        dpt_opn_result = self.dpt_opn(
            customer_code=customer_code_personal,
            customer_type='Single customer',
            catalogue_code=catalogue_code_current,
            reason_of_account_opening='Enter value reason of account opening'
        )
        deposit_current_block_dpt_cei=dpt_opn_result[1]
        self.dpt_apr(
            account_number=deposit_current_block_dpt_cei,
            approve_on_form='Y',
            username=username_approve,
            password=password_approve
        )
        self.dpt_cdp(
            account_number=deposit_current_block_dpt_cei,
            amount_deposit=deposit_amount_current,
            approve_on_form='Y',
            username=username_approve,
            password=password_approve
        )
        generated_number = self.gen_serial_number(stock_prefix_cq, stock_type_cq, 24)
        print(f'generated_number block: {generated_number}')
        from_serial = generated_number[0]
        to_serial = generated_number[1]
        dpt_srg_result = self.dpt_srg(
            stock_type=stock_type_cq,
            from_serial=from_serial,
            to_serial=to_serial,
            stock_prefix=stock_prefix_cq,
            number_of_leaves=number_of_leaves_cq,
            number_of_book=number_of_book_cq,
            approve_on_form='Y',
            username=username_approve,
            password=password_approve
        )
        from_serial_cq_block = dpt_srg_result[1]
        to_serial_cq_block = dpt_srg_result[2]
        self.dpt_sat(
            stock_type=stock_type_cq,
            from_serial=from_serial_cq_block,
            to_serial=to_serial_cq_block,
            assigned_staff_code=username_login
        )
        self.dpt_ccr(
            stock_type=stock_type_cq,
            from_serial=from_serial_cq_block,
            to_serial=to_serial_cq_block,
            approve_on_form='Y',
            username=username_approve,
            password=password_approve
        )
        self.dpt_cis(
            account_number=deposit_current_block_dpt_cei,
            from_serial=from_serial_cq_block,
            to_serial=to_serial_cq_block,
            approve_on_form='Y',
            username=username_approve,
            password=password_approve,
        )
        self.dpt_blk(
            account_number=deposit_current_block_dpt_cei,
            approve_on_form='Y',
            username=username_approve,
            password=password_approve
        )
        global deposit_current_close_dpt_cei, from_serial_cq_close, to_serial_cq_close
        dpt_opn_result = self.dpt_opn(
            customer_code=customer_code_personal,
            customer_type='Single customer',
            catalogue_code=catalogue_code_current,
            reason_of_account_opening='Enter value reason of account opening'
        )
        deposit_current_close_dpt_cei=dpt_opn_result[1]
        self.dpt_apr(
            account_number=deposit_current_close_dpt_cei,
            approve_on_form='Y',
            username=username_approve,
            password=password_approve
        )
        generated_number = self.gen_serial_number(stock_prefix_cq, stock_type_cq, 24)
        print(f'generated_number close: {generated_number}')
        from_serial = generated_number[0]
        to_serial = generated_number[1]
        dpt_srg_result = self.dpt_srg(
            stock_type=stock_type_cq,
            from_serial=from_serial,
            to_serial=to_serial,
            stock_prefix=stock_prefix_cq,
            number_of_leaves=number_of_leaves_cq,
            number_of_book=number_of_book_cq,
            approve_on_form='Y',
            username=username_approve,
            password=password_approve
        )
        from_serial_cq_close = dpt_srg_result[1]
        to_serial_cq_close = dpt_srg_result[2]
        self.dpt_sat(
            stock_type=stock_type_cq,
            from_serial=from_serial_cq_close,
            to_serial=to_serial_cq_close,
            assigned_staff_code=username_login
        )
        self.dpt_ccr(
            stock_type=stock_type_cq,
            from_serial=from_serial_cq_close,
            to_serial=to_serial_cq_close,
            approve_on_form='Y',
            username=username_approve,
            password=password_approve
        )
        self.dpt_cis(
            account_number=deposit_current_close_dpt_cei,
            from_serial=from_serial_cq_close,
            to_serial=to_serial_cq_close,
            approve_on_form='Y',
            username=username_approve,
            password=password_approve,
        )
        self.dpt_cls(
            account_number=deposit_current_close_dpt_cei,
        )

    def test_012_dpt_cei_01_check_not_allowed_deposit_status_block(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        list_error_message = [
            f'InvalidDepositStatus: Invalid deposit status [{status_block}]'
        ]
        self.dpt_cei(
            cheque_no=from_serial_cq_block,
            cheque_amount=amount_current_valid,
            account_number=deposit_current_block_dpt_cei,
            list_error_message=list_error_message,
        )

    def test_012_dpt_cei_02_check_not_allowed_deposit_status_closed(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        list_error_message = [
            f'InvalidDepositStatus: Invalid deposit status [{status_closed}]'
        ]
        self.dpt_cei(
            cheque_no=from_serial_cq_close,
            cheque_amount=amount_current_valid,
            account_number=deposit_current_close_dpt_cei,
            list_error_message=list_error_message,
        )

    def test_012_dpt_cei_03_check_not_allowed_deposit_status_new(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        list_error_message = [
            f'InvalidDepositStatus: Invalid deposit status [{status_new}]'
        ]
        self.dpt_cei(
            cheque_no=from_serial_cq_new,
            cheque_amount=amount_current_valid,
            account_number=deposit_current_new_dpt_cei,
            list_error_message=list_error_message,
        )

    def test_012_dpt_cei_04_check_not_allowed_deposit_status_dormant(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        list_error_message = [
            f'InvalidDepositStatus: Invalid deposit status [{status_dormant}]'
        ]
        self.dpt_cei(
            cheque_no=from_serial_cq_dormant,
            cheque_amount=amount_current_valid,
            account_number=deposit_current_dormant_dpt_cei,
            list_error_message=list_error_message,
        )

    def test_012_dpt_cei_05_check_available_balance_invalid_normal(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        list_error_message = [
            f'InvalidAvailableAmt: Invalid available balance of account [{self.no_mask(deposit_current_normal_dpt_cei)}]. Available balance must be more than [{self.format_number(amount_current_invalid)}] - en'
        ]
        dpt_cei_result = self.dpt_cei(
            cheque_no=from_serial_cq_normal,
            cheque_amount=amount_current_invalid,
            account_number=deposit_current_normal_dpt_cei,
            approve_later='Y',
        )
        self.transaction_approve(
            transaction_references=dpt_cei_result[0], 
            username=username_approve,
            password=password_approve,
            allow_approve='N',
            list_error_message=list_error_message
        )
        self.transaction_reject(
            transaction_references=dpt_cei_result[0], 
            username=username_reverse,
            password=password_reverse
        )

    def test_012_dpt_cei_06_fee_check_available_balance_invalid_normal(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        list_error_message = [
            f'InvalidAvailableAmt: Invalid available balance of account [{self.no_mask(deposit_current_normal_dpt_cei)}]. Available balance must be more than [{self.format_number(value_invalid)}] - en'
        ]
        self.dpt_cei(
            cheque_no=from_serial_cq_normal,
            cheque_amount=amount_current_valid,
            account_number=deposit_current_normal_dpt_cei,
            list_error_message=list_error_message,
            ifc_codes=ifc_codes,
            values=values_invalid,
        )

# # DPT_CSH - VALID CASE
#     def test_00_dpt_csh_01_check_allowed_deposit_type_current(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         dpt_csh_result = self.dpt_csh(
#             account_number_debit=deposit_current_normal,
#             enter_side='D',
#             debit_amount=amount_current_valid,
#             approve_later='Y'
#         )
#         transaction_references=dpt_csh_result
#         self.transaction_approve(
#             transaction_references=transaction_references, 
#             username=username_approve,
#             password=password_approve
#         )

#     def test_00_dpt_csh_02_check_allowed_deposit_type_savings(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         dpt_csh_result = self.dpt_csh(
#             account_number_debit=deposit_savings_normal,
#             enter_side='D',
#             debit_amount=amount_savings_valid,
#             approve_later='Y'
#         )
#         transaction_references=dpt_csh_result
#         self.transaction_approve(
#             transaction_references=transaction_references, 
#             username=username_approve,
#             password=password_approve
#         )

# # DPT_DPT - VALID CASE
#     def test_00_dpt_dpt_01_check_allowed_deposit_type_current(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         dpt_dpt_result = self.dpt_dpt(
#             account_number_debit=deposit_current_normal,
#             account_number_credit=deposit_current_normal,
#             enter_side='D',
#             debit_amount=amount_current_valid,
#             approve_later='Y'
#         )
#         transaction_references=dpt_dpt_result
#         self.transaction_approve(
#             transaction_references=transaction_references, 
#             username=username_approve,
#             password=password_approve
#         )

#     def test_00_dpt_dpt_02_check_allowed_deposit_type_savings(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         dpt_dpt_result = self.dpt_dpt(
#             account_number_debit=deposit_savings_normal,
#             account_number_credit=deposit_current_normal,
#             enter_side='D',
#             debit_amount=amount_savings_valid,
#             approve_later='Y'
#         )
#         transaction_references=dpt_dpt_result
#         self.transaction_approve(
#             transaction_references=transaction_references, 
#             username=username_approve,
#             password=password_approve
#         )

# # DPT_ACT - VALID CASE
#     def test_00_dpt_act_01_check_allowed_deposit_type_current(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         dpt_act_result = self.dpt_act(
#             account_number_debit=deposit_current_normal,
#             account_number_credit=gl_account_number,
#             enter_side='D',
#             debit_amount=amount_current_valid,
#             approve_later='Y'
#         )
#         transaction_references=dpt_act_result
#         self.transaction_approve(
#             transaction_references=transaction_references, 
#             username=username_approve,
#             password=password_approve
#         )

#     def test_00_dpt_act_02_check_allowed_deposit_type_savings(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         dpt_act_result = self.dpt_act(
#             account_number_debit=deposit_savings_normal,
#             account_number_credit=gl_account_number,
#             enter_side='D',
#             debit_amount=amount_savings_valid,
#             approve_later='Y'
#         )
#         transaction_references=dpt_act_result
#         self.transaction_approve(
#             transaction_references=transaction_references, 
#             username=username_approve,
#             password=password_approve
#         )

# # DPT_CWR - VALID CASE
#     def test_00_dpt_cwr_01_check_allowed_deposit_type_savings(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         # verify deposit account
#         self.deposit_account_view(
#             account_number=deposit_savings_normal,
#             account_status=status_normal,
#         )
#         dpt_cwr_result = self.dpt_cwr(
#             account_number=deposit_savings_normal,
#             withdraw_amount=amount_savings_valid,
#             approve_later='Y',
#         )
#         self.transaction_approve(
#             transaction_references=dpt_cwr_result[0], 
#             username=username_approve,
#             password=password_approve
#         )
#         self.transaction_reverse(
#             transaction_references=dpt_cwr_result[0], 
#             username=username_reverse,
#             password=password_reverse
#         )
#         # verify deposit account
#         self.deposit_account_view(
#             account_number=deposit_savings_normal,
#             account_status=status_normal,
#         )

#     def test_00_dpt_cwr_02_handle_dormant_savings(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         # verify deposit account
#         self.deposit_account_view(
#             account_number=deposit_savings_dormant,
#             account_status=status_dormant,
#         )
#         dpt_cwr_result = self.dpt_cwr(
#             account_number=deposit_savings_dormant,
#             withdraw_amount=amount_savings_valid,
#             approve_later='Y',
#         )
#         self.transaction_approve(
#             transaction_references=dpt_cwr_result[0], 
#             username=username_approve,
#             password=password_approve
#         )
#         # verify deposit account
#         self.deposit_account_view(
#             account_number=deposit_savings_dormant,
#             account_status=status_normal,
#         )
#         self.dpt_cas(
#             account_number=deposit_savings_dormant,
#             new_status=status_dormant,
#             current_status=status_normal,
#             approve_on_form='Y',
#             username=username_approve,
#             password=password_approve
#         )

# # DPT_MWR - VALID CASE
#     def test_00_dpt_mwr_01_check_allowed_deposit_type_current(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         # verify deposit account
#         self.deposit_account_view(
#             account_number=deposit_current_normal,
#             account_status=status_normal,
#         )
#         dpt_mwr_result = self.dpt_mwr(
#             account_number=deposit_current_normal,
#             withdraw_amount=amount_current_valid,
#             credit_accounting=gl_account_number,
#             approve_later='Y',
#         )
#         self.transaction_approve(
#             transaction_references=dpt_mwr_result[0], 
#             username=username_approve,
#             password=password_approve
#         )
#         self.transaction_reverse(
#             transaction_references=dpt_mwr_result[0], 
#             username=username_reverse,
#             password=password_reverse
#         )
#         # verify deposit account
#         self.deposit_account_view(
#             account_number=deposit_current_normal,
#             account_status=status_normal,
#         )

#     def test_00_dpt_mwr_02_check_allowed_deposit_type_savings(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         # verify deposit account
#         self.deposit_account_view(
#             account_number=deposit_savings_normal,
#             account_status=status_normal,
#         )
#         dpt_mwr_result = self.dpt_mwr(
#             account_number=deposit_savings_normal,
#             withdraw_amount=amount_savings_valid,
#             credit_accounting=gl_account_number,
#             approve_later='Y',
#         )
#         self.transaction_approve(
#             transaction_references=dpt_mwr_result[0], 
#             username=username_approve,
#             password=password_approve
#         )
#         self.transaction_reverse(
#             transaction_references=dpt_mwr_result[0], 
#             username=username_reverse,
#             password=password_reverse
#         )
#         # verify deposit account
#         self.deposit_account_view(
#             account_number=deposit_savings_normal,
#             account_status=status_normal,
#         )

#     def test_00_dpt_mwr_03_handle_dormant_current(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         # verify deposit account
#         self.deposit_account_view(
#             account_number=deposit_current_dormant,
#             account_status=status_dormant,
#         )
#         dpt_mwr_result = self.dpt_mwr(
#             account_number=deposit_current_dormant,
#             withdraw_amount=amount_current_valid,
#             credit_accounting=gl_account_number,
#             approve_later='Y',
#         )
#         self.transaction_approve(
#             transaction_references=dpt_mwr_result[0], 
#             username=username_approve,
#             password=password_approve
#         )
#         # verify deposit account
#         self.deposit_account_view(
#             account_number=deposit_current_dormant,
#             account_status=status_normal,
#         )
#         self.dpt_cas(
#             account_number=deposit_current_dormant,
#             new_status=status_dormant,
#             current_status=status_normal,
#             approve_on_form='Y',
#             username=username_approve,
#             password=password_approve
#         )

#     def test_00_dpt_mwr_04_handle_dormant_savings(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         # verify deposit account
#         self.deposit_account_view(
#             account_number=deposit_savings_dormant,
#             account_status=status_dormant,
#         )
#         dpt_mwr_result = self.dpt_mwr(
#             account_number=deposit_savings_dormant,
#             withdraw_amount=amount_savings_valid,
#             credit_accounting=gl_account_number,
#             approve_later='Y',
#         )
#         self.transaction_approve(
#             transaction_references=dpt_mwr_result[0], 
#             username=username_approve,
#             password=password_approve
#         )
#         # verify deposit account
#         self.deposit_account_view(
#             account_number=deposit_savings_dormant,
#             account_status=status_normal,
#         )
#         self.dpt_cas(
#             account_number=deposit_savings_dormant,
#             new_status=status_dormant,
#             current_status=status_normal,
#             approve_on_form='Y',
#             username=username_approve,
#             password=password_approve
#         )

# # DPT_TRF - VALID CASE
#     def test_00_dpt_trf_01_check_allowed_deposit_type_current(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         dpt_trf_result = self.dpt_trf(
#             debit_account=deposit_current_normal,
#             amount=amount_current_valid,
#             credit_account=other_current_deposit_account,
#             approve_later='Y',
#         )
#         self.transaction_approve(
#             transaction_references=dpt_trf_result[0], 
#             username=username_approve,
#             password=password_approve
#         )
#         self.transaction_reverse(
#             transaction_references=dpt_trf_result[0], 
#             username=username_reverse,
#             password=password_reverse
#         )
#         dpt_trf_result = self.dpt_trf(
#             debit_account=other_current_deposit_account,
#             amount=amount_current_valid,
#             credit_account=deposit_current_normal,
#             approve_later='Y',
#         )
#         self.transaction_approve(
#             transaction_references=dpt_trf_result[0], 
#             username=username_approve,
#             password=password_approve
#         )
#         self.transaction_reverse(
#             transaction_references=dpt_trf_result[0], 
#             username=username_reverse,
#             password=password_reverse
#         )

#     def test_00_dpt_trf_02_check_allowed_deposit_type_savings(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         dpt_trf_result = self.dpt_trf(
#             debit_account=deposit_savings_normal,
#             amount=amount_savings_valid,
#             credit_account=other_savings_deposit_account,
#             approve_later='Y',
#         )
#         self.transaction_approve(
#             transaction_references=dpt_trf_result[0], 
#             username=username_approve,
#             password=password_approve
#         )
#         self.transaction_reverse(
#             transaction_references=dpt_trf_result[0], 
#             username=username_reverse,
#             password=password_reverse
#         )
#         dpt_trf_result = self.dpt_trf(
#             debit_account=other_savings_deposit_account,
#             amount=amount_savings_valid,
#             credit_account=deposit_savings_normal,
#             approve_later='Y',
#         )
#         self.transaction_approve(
#             transaction_references=dpt_trf_result[0], 
#             username=username_approve,
#             password=password_approve
#         )
#         self.transaction_reverse(
#             transaction_references=dpt_trf_result[0], 
#             username=username_reverse,
#             password=password_reverse
#         )

#     def test_00_dpt_trf_03_handle_dormant_current(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         # verify deposit account
#         self.deposit_account_view(
#             account_number=deposit_current_dormant,
#             account_status=status_dormant,
#         )
#         dpt_trf_result = self.dpt_trf(
#             debit_account=deposit_current_dormant,
#             amount=amount_current_valid,
#             credit_account=other_current_deposit_account,
#             approve_later='Y',
#         )
#         self.transaction_approve(
#             transaction_references=dpt_trf_result[0], 
#             username=username_approve,
#             password=password_approve
#         )
#         # verify deposit account
#         self.deposit_account_view(
#             account_number=deposit_current_dormant,
#             account_status=status_normal,
#         )
#         self.dpt_cas(
#             account_number=deposit_current_dormant,
#             new_status=status_dormant,
#             current_status=status_normal,
#             approve_on_form='Y',
#             username=username_approve,
#             password=password_approve
#         )
#         # verify deposit account
#         self.deposit_account_view(
#             account_number=deposit_current_dormant,
#             account_status=status_dormant,
#         )
#         dpt_trf_result = self.dpt_trf(
#             debit_account=other_current_deposit_account,
#             amount=amount_current_valid,
#             credit_account=deposit_current_dormant,
#             approve_later='Y',
#         )
#         self.transaction_approve(
#             transaction_references=dpt_trf_result[0], 
#             username=username_approve,
#             password=password_approve
#         )
#         # verify deposit account
#         self.deposit_account_view(
#             account_number=deposit_current_dormant,
#             account_status=status_normal,
#         )
#         self.dpt_cas(
#             account_number=deposit_current_dormant,
#             new_status=status_dormant,
#             current_status=status_normal,
#             approve_on_form='Y',
#             username=username_approve,
#             password=password_approve
#         )

#     def test_00_dpt_trf_04_handle_dormant_savings(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         # verify deposit account
#         self.deposit_account_view(
#             account_number=deposit_savings_dormant,
#             account_status=status_dormant,
#         )
#         dpt_trf_result = self.dpt_trf(
#             debit_account=deposit_savings_dormant,
#             amount=amount_savings_valid,
#             credit_account=other_savings_deposit_account,
#             approve_later='Y',
#         )
#         self.transaction_approve(
#             transaction_references=dpt_trf_result[0], 
#             username=username_approve,
#             password=password_approve
#         )
#         # verify deposit account
#         self.deposit_account_view(
#             account_number=deposit_savings_dormant,
#             account_status=status_normal,
#         )
#         self.dpt_cas(
#             account_number=deposit_savings_dormant,
#             new_status=status_dormant,
#             current_status=status_normal,
#             approve_on_form='Y',
#             username=username_approve,
#             password=password_approve
#         )
#         # verify deposit account
#         self.deposit_account_view(
#             account_number=deposit_savings_dormant,
#             account_status=status_dormant,
#         )
#         dpt_trf_result = self.dpt_trf(
#             debit_account=other_savings_deposit_account,
#             amount=amount_savings_valid,
#             credit_account=deposit_savings_dormant,
#             approve_later='Y',
#         )
#         self.transaction_approve(
#             transaction_references=dpt_trf_result[0], 
#             username=username_approve,
#             password=password_approve
#         )
#         # verify deposit account
#         self.deposit_account_view(
#             account_number=deposit_savings_dormant,
#             account_status=status_normal,
#         )
#         self.dpt_cas(
#             account_number=deposit_savings_dormant,
#             new_status=status_dormant,
#             current_status=status_normal,
#             approve_on_form='Y',
#             username=username_approve,
#             password=password_approve
#         )

# # DPT_FEE - VALID CASE
#     def test_00_dpt_fee_02_check_allowed_deposit_type_savings(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         dpt_fee_result = self.dpt_fee(
#             account_number=deposit_savings_normal,
#             ifc_codes=ifc_codes,
#             values=values_valid,
#             approve_later='Y',
#         )
#         self.transaction_approve(
#             transaction_references=dpt_fee_result[0], 
#             username=username_approve,
#             password=password_approve
#         )
#         self.transaction_reverse(
#             transaction_references=dpt_fee_result[0], 
#             username=username_reverse,
#             password=password_reverse
#         )

# # DPT_CIS - VALID CASE
#     def test_00_dpt_cis_01_fee_check_allowed_deposit_type_current(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         dpt_cis_result = self.dpt_cis(
#             account_number=deposit_current_normal,
#             from_serial=from_serial_cq,
#             to_serial=to_serial_cq,
#             ifc_codes=ifc_codes,
#             values=values_valid,
#             fee_collect_method='Deposit',
#             account_number_for_fee=other_current_deposit_account,
#             approve_later='Y',
#         )
#         self.transaction_approve(
#             transaction_references=dpt_cis_result[0], 
#             username=username_approve,
#             password=password_approve
#         )
#         self.transaction_reverse(
#             transaction_references=dpt_cis_result[0], 
#             username=username_reverse,
#             password=password_reverse
#         )

#     def test_00_dpt_cis_02_fee_check_allowed_deposit_type_savings(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         dpt_cis_result = self.dpt_cis(
#             account_number=deposit_current_normal,
#             from_serial=from_serial_cq,
#             to_serial=to_serial_cq,
#             ifc_codes=ifc_codes,
#             values=values_valid,
#             fee_collect_method='Deposit',
#             account_number_for_fee=other_savings_deposit_account,
#             approve_later='Y',
#         )
#         self.transaction_approve(
#             transaction_references=dpt_cis_result[0], 
#             username=username_approve,
#             password=password_approve
#         )
#         self.transaction_reverse(
#             transaction_references=dpt_cis_result[0], 
#             username=username_reverse,
#             password=password_reverse
#         )

# # DPT_CER - VALID CASE
#     def test_00_dpt_cer_01_fee_check_allowed_deposit_type_current(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         dpt_cer_result = self.dpt_cer(
#             account_number=deposit_prepaid_normal_valid,
#             cerfiticate_serial=from_serial_fr,
#             ifc_codes=ifc_codes,
#             values=values_valid,
#             fee_collect_method='Deposit',
#             account_number_for_fee=other_current_deposit_account,
#             approve_later='Y',
#         )
#         self.transaction_approve(
#             transaction_references=dpt_cer_result[0], 
#             username=username_approve,
#             password=password_approve
#         )
#         self.transaction_reverse(
#             transaction_references=dpt_cer_result[0], 
#             username=username_reverse,
#             password=password_reverse
#         )

#     def test_00_dpt_cer_02_fee_check_allowed_deposit_type_savings(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         dpt_cer_result = self.dpt_cer(
#             account_number=deposit_prepaid_normal_valid,
#             cerfiticate_serial=from_serial_fr,
#             ifc_codes=ifc_codes,
#             values=values_valid,
#             fee_collect_method='Deposit',
#             account_number_for_fee=other_savings_deposit_account,
#             approve_later='Y',
#         )
#         self.transaction_approve(
#             transaction_references=dpt_cer_result[0], 
#             username=username_approve,
#             password=password_approve
#         )
#         self.transaction_reverse(
#             transaction_references=dpt_cer_result[0], 
#             username=username_reverse,
#             password=password_reverse
#         )

# # DPT_FBI - VALID CASE
#     def test_00_dpt_fbi_01_fee_check_allowed_deposit_type_current_01m(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         dpt_fbi_result = self.dpt_fbi(
#             account_number=deposit_fixed_01m_normal_valid,
#             serial_no=from_serial_fb_01,
#             ifc_codes=ifc_codes,
#             values=values_valid,
#             fee_collect_method='Deposit',
#             account_number_for_fee=other_current_deposit_account,
#             approve_later='Y',
#         )
#         self.transaction_approve(
#             transaction_references=dpt_fbi_result[0], 
#             username=username_approve,
#             password=password_approve
#         )
#         self.transaction_reverse(
#             transaction_references=dpt_fbi_result[0], 
#             username=username_reverse,
#             password=password_reverse
#         )

#     def test_00_dpt_fbi_02_fee_check_allowed_deposit_type_current_03m(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         dpt_fbi_result = self.dpt_fbi(
#             account_number=deposit_fixed_03m_normal_valid,
#             serial_no=from_serial_fb_03,
#             ifc_codes=ifc_codes,
#             values=values_valid,
#             fee_collect_method='Deposit',
#             account_number_for_fee=other_current_deposit_account,
#             approve_later='Y',
#         )
#         self.transaction_approve(
#             transaction_references=dpt_fbi_result[0], 
#             username=username_approve,
#             password=password_approve
#         )
#         self.transaction_reverse(
#             transaction_references=dpt_fbi_result[0], 
#             username=username_reverse,
#             password=password_reverse
#         )

#     def test_00_dpt_fbi_03_fee_check_allowed_deposit_type_current_06m(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         dpt_fbi_result = self.dpt_fbi(
#             account_number=deposit_fixed_06m_normal_valid,
#             serial_no=from_serial_fb_06,
#             ifc_codes=ifc_codes,
#             values=values_valid,
#             fee_collect_method='Deposit',
#             account_number_for_fee=other_current_deposit_account,
#             approve_later='Y',
#         )
#         self.transaction_approve(
#             transaction_references=dpt_fbi_result[0], 
#             username=username_approve,
#             password=password_approve
#         )
#         self.transaction_reverse(
#             transaction_references=dpt_fbi_result[0], 
#             username=username_reverse,
#             password=password_reverse
#         )

#     def test_00_dpt_fbi_04_fee_check_allowed_deposit_type_current_09m(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         dpt_fbi_result = self.dpt_fbi(
#             account_number=deposit_fixed_09m_normal_valid,
#             serial_no=from_serial_fb_09,
#             ifc_codes=ifc_codes,
#             values=values_valid,
#             fee_collect_method='Deposit',
#             account_number_for_fee=other_current_deposit_account,
#             approve_later='Y',
#         )
#         self.transaction_approve(
#             transaction_references=dpt_fbi_result[0], 
#             username=username_approve,
#             password=password_approve
#         )
#         self.transaction_reverse(
#             transaction_references=dpt_fbi_result[0], 
#             username=username_reverse,
#             password=password_reverse
#         )

#     def test_00_dpt_fbi_05_fee_check_allowed_deposit_type_current_12m(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         dpt_fbi_result = self.dpt_fbi(
#             account_number=deposit_fixed_12m_normal_valid,
#             serial_no=from_serial_fb_12,
#             ifc_codes=ifc_codes,
#             values=values_valid,
#             fee_collect_method='Deposit',
#             account_number_for_fee=other_current_deposit_account,
#             approve_later='Y',
#         )
#         self.transaction_approve(
#             transaction_references=dpt_fbi_result[0], 
#             username=username_approve,
#             password=password_approve
#         )
#         self.transaction_reverse(
#             transaction_references=dpt_fbi_result[0], 
#             username=username_reverse,
#             password=password_reverse
#         )

#     def test_00_dpt_fbi_06_fee_check_allowed_deposit_type_savings_01m(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         dpt_fbi_result = self.dpt_fbi(
#             account_number=deposit_fixed_01m_normal_valid,
#             serial_no=from_serial_fb_01,
#             ifc_codes=ifc_codes,
#             values=values_valid,
#             fee_collect_method='Deposit',
#             account_number_for_fee=other_savings_deposit_account,
#             approve_later='Y',
#         )
#         self.transaction_approve(
#             transaction_references=dpt_fbi_result[0], 
#             username=username_approve,
#             password=password_approve
#         )
#         self.transaction_reverse(
#             transaction_references=dpt_fbi_result[0], 
#             username=username_reverse,
#             password=password_reverse
#         )

#     def test_00_dpt_fbi_07_fee_check_allowed_deposit_type_savings_03m(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         dpt_fbi_result = self.dpt_fbi(
#             account_number=deposit_fixed_03m_normal_valid,
#             serial_no=from_serial_fb_03,
#             ifc_codes=ifc_codes,
#             values=values_valid,
#             fee_collect_method='Deposit',
#             account_number_for_fee=other_savings_deposit_account,
#             approve_later='Y',
#         )
#         self.transaction_approve(
#             transaction_references=dpt_fbi_result[0], 
#             username=username_approve,
#             password=password_approve
#         )
#         self.transaction_reverse(
#             transaction_references=dpt_fbi_result[0], 
#             username=username_reverse,
#             password=password_reverse
#         )

#     def test_00_dpt_fbi_08_fee_check_allowed_deposit_type_savings_06m(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         dpt_fbi_result = self.dpt_fbi(
#             account_number=deposit_fixed_06m_normal_valid,
#             serial_no=from_serial_fb_06,
#             ifc_codes=ifc_codes,
#             values=values_valid,
#             fee_collect_method='Deposit',
#             account_number_for_fee=other_savings_deposit_account,
#             approve_later='Y',
#         )
#         self.transaction_approve(
#             transaction_references=dpt_fbi_result[0], 
#             username=username_approve,
#             password=password_approve
#         )
#         self.transaction_reverse(
#             transaction_references=dpt_fbi_result[0], 
#             username=username_reverse,
#             password=password_reverse
#         )

#     def test_00_dpt_fbi_09_fee_check_allowed_deposit_type_savings_09m(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         dpt_fbi_result = self.dpt_fbi(
#             account_number=deposit_fixed_09m_normal_valid,
#             serial_no=from_serial_fb_09,
#             ifc_codes=ifc_codes,
#             values=values_valid,
#             fee_collect_method='Deposit',
#             account_number_for_fee=other_savings_deposit_account,
#             approve_later='Y',
#         )
#         self.transaction_approve(
#             transaction_references=dpt_fbi_result[0], 
#             username=username_approve,
#             password=password_approve
#         )
#         self.transaction_reverse(
#             transaction_references=dpt_fbi_result[0], 
#             username=username_reverse,
#             password=password_reverse
#         )

#     def test_00_dpt_fbi_10_fee_check_allowed_deposit_type_savings_12m(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         dpt_fbi_result = self.dpt_fbi(
#             account_number=deposit_fixed_12m_normal_valid,
#             serial_no=from_serial_fb_12,
#             ifc_codes=ifc_codes,
#             values=values_valid,
#             fee_collect_method='Deposit',
#             account_number_for_fee=other_savings_deposit_account,
#             approve_later='Y',
#         )
#         self.transaction_approve(
#             transaction_references=dpt_fbi_result[0], 
#             username=username_approve,
#             password=password_approve
#         )
#         self.transaction_reverse(
#             transaction_references=dpt_fbi_result[0], 
#             username=username_reverse,
#             password=password_reverse
#         )

# # DPT_SBI - VALID CASE
#     def test_00_dpt_sbi_01_fee_check_allowed_deposit_type_current(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         dpt_sbi_result = self.dpt_sbi(
#             account_number=deposit_savings_normal_valid,
#             serial_no=from_serial_sb,
#             ifc_codes=ifc_codes,
#             values=values_valid,
#             fee_collect_method='Deposit',
#             account_number_for_fee=other_current_deposit_account,
#             approve_later='Y',
#         )
#         self.transaction_approve(
#             transaction_references=dpt_sbi_result[0], 
#             username=username_approve,
#             password=password_approve
#         )
#         self.transaction_reverse(
#             transaction_references=dpt_sbi_result[0], 
#             username=username_reverse,
#             password=password_reverse
#         )

#     def test_00_dpt_sbi_02_fee_check_allowed_deposit_type_savings(self):
#         print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
#         dpt_sbi_result = self.dpt_sbi(
#             account_number=deposit_savings_normal_valid,
#             serial_no=from_serial_sb,
#             ifc_codes=ifc_codes,
#             values=values_valid,
#             fee_collect_method='Deposit',
#             account_number_for_fee=other_savings_deposit_account,
#             approve_later='Y',
#         )
#         self.transaction_approve(
#             transaction_references=dpt_sbi_result[0], 
#             username=username_approve,
#             password=password_approve
#         )
#         self.transaction_reverse(
#             transaction_references=dpt_sbi_result[0], 
#             username=username_reverse,
#             password=password_reverse
#         )

    def test_013_dpt_cei_01_fee_check_allowed_normal(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        dpt_cei_result = self.dpt_cei(
            cheque_no=from_serial_cq_normal,
            cheque_amount=amount_current_valid,
            account_number=deposit_current_normal_dpt_cei,
            ifc_codes=ifc_codes,
            values=value_valid,
            approve_later='Y',
        )
        self.transaction_approve(
            transaction_references=dpt_cei_result[0], 
            username=username_approve,
            password=password_approve
        )
        self.transaction_reverse(
            transaction_references=dpt_cei_result[0], 
            username=username_reverse,
            password=password_reverse
        )


if __name__ == '__main__': 
    webui_test.main()