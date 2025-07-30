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

customer_code_single_mask = CUSTOMER_CODE

# data test need to check and update
# Branch 003
# dpt_usd ='12-003-822674-4'
# dpt_mmk = '11-003-010329-2'
# Branch 004
dpt_usd ='12-004-884133-5'
dpt_mmk = '11-004-369071-4'
# data test
catalogue_code_buy = 'TFXBUY0001'
trade_type_buy = 'Buy'
reference_rate_bk = '2,422.000000000'
contract_rate_buy_gain = '2,400.000000000'
swap_point_buy_gain = '-22.000000000'
contract_rate_buy_loss = '2,500.000000000'
swap_point_buy_loss = '78.000000000'
catalogue_code_sell = 'TFXSEL0001'
trade_type_sell = 'Sell'
contract_rate_sell_gain = '2,500.000000000'
swap_point_sell_gain = '78.000000000'
contract_rate_sell_loss = '2,400.000000000'
swap_point_sell_loss = '-22.000000000'
amount_usd = '30,000.00'
amount_mmk = '72,660,000.00'
amount_mmk_up = '75,000,000.00'
amount_mmk_down = '72,000,000.00'
amount_dif_up = '2,340,000.00'
amount_dif_down = '660,000.00'
# data test update
contract_rate_buy_gain_update_loss = '2,500.000000000'
swap_point_buy_gain_update_loss = '78.000000000'
contract_rate_buy_loss_update_gain = '2,400.000000000'
swap_point_buy_loss_update_gain = '-22.000000000'
contract_rate_sell_gain_update = '2,600.000000000'
swap_point_sell_gain_update = '178.000000000'
contract_rate_sell_loss_update = '2,300.000000000'
swap_point_sell_loss_update = '-122.000000000'
amount_usd_update = '35,000.00'
amount_mmk_update = '84,770,000.00'
amount_mmk_up_update = '91,000,000.00'
amount_mmk_down_update = '80,500,000.00'
amount_dif_up_update = '6,230,000.00'
amount_dif_down_update = '4,270,000.00'

class RegressionForexTest(FormAction):
    def get_url(self):
        return RUN_ON_URL

    def data_begin(self):
        global username_approve, password_approve, username_reverse, password_reverse, username, password
        username_approve = USERNAME_APPROVE
        password_approve = PASSWORD_APPROVE
        username_reverse = USERNAME_REVERSE
        password_reverse = PASSWORD_REVERSE
        username = USERNAME_LOGIN
        password = PASSWORD_LOGIN
        self.login(username, password, one_app=ONE_APP)
        global working_date, branch_code
        working_date = self.get_working_date()
        branch_code = self.get_logged_branch_code()
        global gl_usd, gl_mmk
        gl_usd = f'{branch_code}-1010106666666-02'
        gl_mmk = f'{branch_code}-1010105555555-01'

    def start_class(self):
        self.data_begin()

    def end_class(self):
        self.logout()

    def reset_browser(self):
        self.logout()
        self.restart_browser()
        self.data_begin()

# Check the data used for testing
    def test_000_check_test_data_must_exist(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        self.add_gl_level_9_use_for_testing(
            branch_code=branch_code,
            currency_code='USD',
            account_number=gl_usd
        )
        self.add_gl_level_9_use_for_testing(
            branch_code=branch_code,
            currency_code='MMK',
            account_number=gl_mmk
        )
        if self.check_customer_profile_not_exist(customer_code_single_mask):
            self.stop()
            self.fail()
        if self.check_deposit_account_not_exist(dpt_usd):
            self.stop()
            self.fail()
        if self.check_deposit_account_not_exist(dpt_mmk):
            self.stop()
            self.fail()


# CASE 01: BUY GAIN
    def test_001_buy_gain_01_tfx_ofo_open_forex_account_success(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        global forex_account_buy_gain_mask, forex_account_buy_gain
        tfx_ofo_result = self.tfx_ofo(
            counterparty_code=customer_code_single_mask,
            catalogue_code=catalogue_code_buy,
            trade_rate=contract_rate_buy_gain,
            debit_currency='USD',
            credit_currency='MMK',
            reference_rate=reference_rate_bk,
            value_date=working_date,
            swap_point=swap_point_buy_gain,
            debit_by='GL',
            debit_account_no_act=gl_usd,
            debit_amount=amount_usd,
            credit_amount=amount_mmk_down,
            credit_by='GL',
            credit_account_no_act=gl_mmk,
            approve_later='Y'
        )
        transaction_references=tfx_ofo_result[0]
        forex_account_buy_gain_mask=tfx_ofo_result[1]
        # view transaction before approve
        self.tfx_ofo_view(
            transaction_references=transaction_references, 
            counterparty_code=customer_code_single_mask,
            catalogue_code=catalogue_code_buy,
            trade_type=trade_type_buy,
            contract_rate=contract_rate_buy_gain,
            debit_currency='USD',
            credit_currency='MMK',
            reference_rate=reference_rate_bk,
            value_date=working_date,
            swap_point=swap_point_buy_gain,
            debit_by='GL',
            debit_account_no_act=gl_usd,
            debit_amount=amount_usd,
            credit_amount=amount_mmk_down,
            credit_by='GL',
            credit_account_no_act=gl_mmk
        )
        # approve transaction
        self.transaction_approve(
            transaction_references=transaction_references, 
            username=username_approve,
            password=password_approve
        )
        forex_account_buy_gain=self.get_text_table_data('Account Number', 1)
        print(f'forex_account_buy_gain: {forex_account_buy_gain}')
        # view account information
        self.treasury_account_view(
            account_number=forex_account_buy_gain,
            account_status='Authoring',
            counterparty_code=customer_code_single_mask,
            catalogue_code=catalogue_code_buy,
            trade_type=trade_type_buy,
            trade_rate=contract_rate_buy_gain,
            debit_currency='USD',
            credit_currency='MMK',
            reference_rate=reference_rate_bk,
            value_date=working_date,
            swap_point=swap_point_buy_gain,
            debit_by='GL',
            debit_account=gl_usd,
            debit_amount=amount_usd,
            credit_amount=amount_mmk_down,
            credit_by='GL',
            credit_account=gl_mmk
        )
        # view transaction after approve
        self.tfx_ofo_view(
            transaction_references=transaction_references, 
            account_number=forex_account_buy_gain,
            counterparty_code=customer_code_single_mask,
            catalogue_code=catalogue_code_buy,
            trade_type=trade_type_buy,
            contract_rate=contract_rate_buy_gain,
            debit_currency='USD',
            credit_currency='MMK',
            reference_rate=reference_rate_bk,
            value_date=working_date,
            swap_point=swap_point_buy_gain,
            debit_by='GL',
            debit_account_no_act=gl_usd,
            debit_amount=amount_usd,
            credit_amount=amount_mmk_down,
            credit_by='GL',
            credit_account_no_act=gl_mmk
        )

    def test_001_buy_gain_02_tfx_fac_approve_forex_account_success(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        tfx_fac_result = self.tfx_fac(
            account_number=forex_account_buy_gain,
            counterparty_code=customer_code_single_mask,
            catalogue_code=catalogue_code_buy,
            trade_type=trade_type_buy,
            contract_rate=contract_rate_buy_gain,
            debit_currency='USD',
            credit_currency='MMK',
            reference_rate=reference_rate_bk,
            value_date=working_date,
            swap_point=swap_point_buy_gain,
            debit_by='GL',
            debit_account_no_act=gl_usd,
            debit_amount=amount_usd,
            credit_amount=amount_mmk_down,
            credit_by='GL',
            credit_account_no_act=gl_mmk,
            approve_later='Y'
        )
        transaction_references=tfx_fac_result[0]
        forex_account_buy_gain_mask=tfx_fac_result[1]
        # approve transaction
        self.transaction_approve(
            transaction_references=transaction_references, 
            username=username_approve,
            password=password_approve
        )
        # view transaction
        self.tfx_fac_view(
            transaction_references=transaction_references, 
            account_number=forex_account_buy_gain_mask,
            counterparty_code=customer_code_single_mask,
            catalogue_code=catalogue_code_buy,
            trade_type=trade_type_buy,
            contract_rate=contract_rate_buy_gain,
            debit_currency='USD',
            credit_currency='MMK',
            reference_rate=reference_rate_bk,
            value_date=working_date,
            swap_point=swap_point_buy_gain,
            debit_by='GL',
            debit_account_no_act=gl_usd,
            debit_amount=amount_usd,
            credit_amount=amount_mmk_down,
            credit_by='GL',
            credit_account_no_act=gl_mmk
        )
        # check account number of posting
        self.assert_posting_debit_account_number('1', branch_code+'-5020101000101-01')
        self.assert_posting_debit_amount('1', amount_mmk_down)
        self.assert_posting_credit_account_number('1', gl_mmk)
        self.assert_posting_credit_amount('1', amount_mmk_down)
        self.assert_posting_debit_account_number('2', gl_usd)
        self.assert_posting_debit_amount('2', amount_usd)
        self.assert_posting_credit_account_number('2', branch_code+'-6020101000101-02')
        self.assert_posting_credit_amount('2', amount_usd)
        self.assert_posting_debit_account_number('3', branch_code+'-5020101000101-01')
        self.assert_posting_debit_amount('3', amount_dif_down)
        self.assert_posting_credit_account_number('3', branch_code+'-3040101000101-01')
        self.assert_posting_credit_amount('3', amount_dif_down)
        # view account information
        self.treasury_account_view(
            account_number=forex_account_buy_gain,
            account_status='Approved contingent',
            counterparty_code=customer_code_single_mask,
            catalogue_code=catalogue_code_buy,
            trade_type=trade_type_buy,
            trade_rate=contract_rate_buy_gain,
            debit_currency='USD',
            credit_currency='MMK',
            reference_rate=reference_rate_bk,
            value_date=working_date,
            swap_point=swap_point_buy_gain,
            debit_by='GL',
            debit_account=gl_usd,
            debit_amount=amount_usd,
            credit_amount=amount_mmk_down,
            credit_by='GL',
            credit_account=gl_mmk
        )


# CASE 02: BUY LOSS
    def test_002_buy_loss_01_tfx_ofo_open_forex_account_success(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        global forex_account_buy_loss_mask, forex_account_buy_loss
        tfx_ofo_result = self.tfx_ofo(
            counterparty_code=customer_code_single_mask,
            catalogue_code=catalogue_code_buy,
            contract_rate=contract_rate_buy_loss,
            debit_currency='USD',
            credit_currency='MMK',
            reference_rate=reference_rate_bk,
            value_date=working_date,
            swap_point=swap_point_buy_loss,
            debit_by='Cash',
            debit_amount=amount_usd,
            credit_amount=amount_mmk_up,
            credit_by='GL',
            credit_account_no_act=gl_mmk,
            approve_later='Y'
        )
        transaction_references=tfx_ofo_result[0]
        forex_account_buy_loss_mask=tfx_ofo_result[1]
        # view transaction before approve
        self.tfx_ofo_view(
            transaction_references=transaction_references, 
            counterparty_code=customer_code_single_mask,
            catalogue_code=catalogue_code_buy,
            trade_type=trade_type_buy,
            contract_rate=contract_rate_buy_loss,
            debit_currency='USD',
            credit_currency='MMK',
            reference_rate=reference_rate_bk,
            value_date=working_date,
            swap_point=swap_point_buy_loss,
            debit_by='Cash',
            debit_amount=amount_usd,
            credit_amount=amount_mmk_up,
            credit_by='GL',
            credit_account_no_act=gl_mmk
        )
        # approve transaction
        self.transaction_approve(
            transaction_references=transaction_references, 
            username=username_approve,
            password=password_approve
        )
        forex_account_buy_loss=self.get_text_table_data('Account Number', 1)
        print(f'forex_account_buy_loss: {forex_account_buy_loss}')
        # view account information
        self.treasury_account_view(
            account_number=forex_account_buy_loss,
            account_status='Authoring',
            counterparty_code=customer_code_single_mask,
            catalogue_code=catalogue_code_buy,
            trade_type=trade_type_buy,
            trade_rate=contract_rate_buy_loss,
            debit_currency='USD',
            credit_currency='MMK',
            reference_rate=reference_rate_bk,
            value_date=working_date,
            swap_point=swap_point_buy_loss,
            debit_by='Cash',
            debit_amount=amount_usd,
            credit_amount=amount_mmk_up,
            credit_by='GL',
            credit_account=gl_mmk
        )
        # view transaction after approve
        self.tfx_ofo_view(
            transaction_references=transaction_references, 
            account_number=forex_account_buy_loss,
            counterparty_code=customer_code_single_mask,
            catalogue_code=catalogue_code_buy,
            trade_type=trade_type_buy,
            contract_rate=contract_rate_buy_loss,
            debit_currency='USD',
            credit_currency='MMK',
            reference_rate=reference_rate_bk,
            value_date=working_date,
            swap_point=swap_point_buy_loss,
            debit_by='Cash',
            debit_amount=amount_usd,
            credit_amount=amount_mmk_up,
            credit_by='GL',
            credit_account_no_act=gl_mmk
        )

    def test_002_buy_loss_02_tfx_fac_approve_forex_account_success(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        tfx_fac_result = self.tfx_fac(
            account_number=forex_account_buy_loss,
            counterparty_code=customer_code_single_mask,
            catalogue_code=catalogue_code_buy,
            trade_type=trade_type_buy,
            contract_rate=contract_rate_buy_loss,
            debit_currency='USD',
            credit_currency='MMK',
            reference_rate=reference_rate_bk,
            value_date=working_date,
            swap_point=swap_point_buy_loss,
            debit_by='Cash',
            debit_amount=amount_usd,
            credit_amount=amount_mmk_up,
            credit_by='GL',
            credit_account_no_act=gl_mmk,
            approve_later='Y'
        )
        transaction_references=tfx_fac_result[0]
        forex_account_buy_loss_mask=tfx_fac_result[1]
        # approve transaction
        self.transaction_approve(
            transaction_references=transaction_references, 
            username=username_approve,
            password=password_approve
        )
        # view transaction
        self.tfx_fac_view(
            transaction_references=transaction_references, 
            account_number=forex_account_buy_loss_mask,
            counterparty_code=customer_code_single_mask,
            catalogue_code=catalogue_code_buy,
            trade_type=trade_type_buy,
            contract_rate=contract_rate_buy_loss,
            debit_currency='USD',
            credit_currency='MMK',
            reference_rate=reference_rate_bk,
            value_date=working_date,
            swap_point=swap_point_buy_loss,
            debit_by='Cash',
            debit_amount=amount_usd,
            credit_amount=amount_mmk_up,
            credit_by='GL',
            credit_account_no_act=gl_mmk
        )
        # check account number of posting
        self.assert_posting_debit_account_number('1', branch_code+'-5020101000101-01')
        self.assert_posting_debit_amount('1', amount_mmk_up)
        self.assert_posting_credit_account_number('1', gl_mmk)
        self.assert_posting_credit_amount('1', amount_mmk_up)
        self.assert_posting_debit_account_number('2', branch_code+'-1010301000101-02')
        self.assert_posting_debit_amount('2', amount_usd)
        self.assert_posting_credit_account_number('2', branch_code+'-6020101000101-02')
        self.assert_posting_credit_amount('2', amount_usd)
        self.assert_posting_debit_account_number('3', branch_code+'-4030101000101-01')
        self.assert_posting_debit_amount('3', amount_dif_up)
        self.assert_posting_credit_account_number('3', branch_code+'-5020101000101-01')
        self.assert_posting_credit_amount('3', amount_dif_up)
        # view account information
        self.treasury_account_view(
            account_number=forex_account_buy_loss_mask,
            account_status='Approved contingent',
            counterparty_code=customer_code_single_mask,
            catalogue_code=catalogue_code_buy,
            trade_type=trade_type_buy,
            trade_rate=contract_rate_buy_loss,
            debit_currency='USD',
            credit_currency='MMK',
            reference_rate=reference_rate_bk,
            value_date=working_date,
            swap_point=swap_point_buy_loss,
            debit_by='Cash',
            debit_amount=amount_usd,
            credit_amount=amount_mmk_up,
            credit_by='GL',
            credit_account=gl_mmk
        )


# CASE 03: SELL GAIN
    def test_003_sell_gain_01_tfx_ofo_open_forex_account_success(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        global forex_account_sell_gain_mask, forex_account_sell_gain
        tfx_ofo_result = self.tfx_ofo(
            counterparty_code=customer_code_single_mask,
            catalogue_code=catalogue_code_sell,
            contract_rate=contract_rate_sell_gain,
            debit_currency='MMK',
            credit_currency='USD',
            reference_rate=reference_rate_bk,
            value_date=working_date,
            swap_point=swap_point_sell_gain,
            debit_by='Cash',
            debit_amount=amount_mmk_up,
            credit_amount=amount_usd,
            credit_by='Cash',
            approve_later='Y'
        )
        transaction_references=tfx_ofo_result[0]
        forex_account_sell_gain_mask=tfx_ofo_result[1]
        # view transaction before approve
        self.tfx_ofo_view(
            transaction_references=transaction_references, 
            counterparty_code=customer_code_single_mask,
            catalogue_code=catalogue_code_sell,
            trade_type=trade_type_sell,
            contract_rate=contract_rate_sell_gain,
            debit_currency='MMK',
            credit_currency='USD',
            reference_rate=reference_rate_bk,
            value_date=working_date,
            swap_point=swap_point_sell_gain,
            debit_by='Cash',
            debit_amount=amount_mmk_up,
            credit_amount=amount_usd,
            credit_by='Cash'
        )
        # approve transaction
        self.transaction_approve(
            transaction_references=transaction_references, 
            username=username_approve,
            password=password_approve
        )
        forex_account_sell_gain=self.get_text_table_data('Account Number', 1)
        print(f'forex_account_sell_gain: {forex_account_sell_gain}')
        # view account information
        self.treasury_account_view(
            account_number=forex_account_sell_gain,
            account_status='Authoring',
            counterparty_code=customer_code_single_mask,
            catalogue_code=catalogue_code_sell,
            trade_type=trade_type_sell,
            trade_rate=contract_rate_sell_gain,
            debit_currency='MMK',
            credit_currency='USD',
            reference_rate=reference_rate_bk,
            value_date=working_date,
            swap_point=swap_point_sell_gain,
            debit_by='Cash',
            debit_amount=amount_mmk_up,
            credit_amount=amount_usd,
            credit_by='Cash'
        )
        # view transaction after approve
        self.tfx_ofo_view(
            transaction_references=transaction_references, 
            account_number=forex_account_sell_gain,
            counterparty_code=customer_code_single_mask,
            catalogue_code=catalogue_code_sell,
            trade_type=trade_type_sell,
            contract_rate=contract_rate_sell_gain,
            debit_currency='MMK',
            credit_currency='USD',
            reference_rate=reference_rate_bk,
            value_date=working_date,
            swap_point=swap_point_sell_gain,
            debit_by='Cash',
            debit_amount=amount_mmk_up,
            credit_amount=amount_usd,
            credit_by='Cash'
        )

    def test_003_sell_gain_02_tfx_fac_approve_forex_account_success(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        tfx_fac_result = self.tfx_fac(
            account_number=forex_account_sell_gain,
            counterparty_code=customer_code_single_mask,
            catalogue_code=catalogue_code_sell,
            trade_type=trade_type_sell,
            contract_rate=contract_rate_sell_gain,
            debit_currency='MMK',
            credit_currency='USD',
            reference_rate=reference_rate_bk,
            value_date=working_date,
            swap_point=swap_point_sell_gain,
            debit_by='Cash',
            debit_amount=amount_mmk_up,
            credit_amount=amount_usd,
            credit_by='Cash',
            approve_later='Y'
        )
        transaction_references=tfx_fac_result[0]
        forex_account_sell_gain_mask=tfx_fac_result[1]
        # approve transaction
        self.transaction_approve(
            transaction_references=transaction_references, 
            username=username_approve,
            password=password_approve
        )
        # view transaction
        self.tfx_fac_view(
            transaction_references=transaction_references, 
            account_number=forex_account_sell_gain_mask,
            counterparty_code=customer_code_single_mask,
            catalogue_code=catalogue_code_sell,
            trade_type=trade_type_sell,
            contract_rate=contract_rate_sell_gain,
            debit_currency='MMK',
            credit_currency='USD',
            reference_rate=reference_rate_bk,
            value_date=working_date,
            swap_point=swap_point_sell_gain,
            debit_by='Cash',
            debit_amount=amount_mmk_up,
            credit_amount=amount_usd,
            credit_by='Cash'
        )
        # check account number of posting
        self.assert_posting_debit_account_number('1', branch_code+'-1010301000101-01')
        self.assert_posting_debit_amount('1', amount_mmk_up)
        self.assert_posting_credit_account_number('1', branch_code+'-5020101000101-01')
        self.assert_posting_credit_amount('1', amount_mmk_up)
        self.assert_posting_debit_account_number('2', branch_code+'-6020101000101-02')
        self.assert_posting_debit_amount('2', amount_usd)
        self.assert_posting_credit_account_number('2', branch_code+'-1010301000101-02')
        self.assert_posting_credit_amount('2', amount_usd)
        self.assert_posting_debit_account_number('3', branch_code+'-5020101000101-01')
        self.assert_posting_debit_amount('3', amount_dif_up)
        self.assert_posting_credit_account_number('3', branch_code+'-3040101000101-01')
        self.assert_posting_credit_amount('3', amount_dif_up)
        # view account information
        self.treasury_account_view(
            account_number=forex_account_sell_gain_mask,
            account_status='Approved contingent',
            counterparty_code=customer_code_single_mask,
            catalogue_code=catalogue_code_sell,
            trade_type=trade_type_sell,
            trade_rate=contract_rate_sell_gain,
            debit_currency='MMK',
            credit_currency='USD',
            reference_rate=reference_rate_bk,
            value_date=working_date,
            swap_point=swap_point_sell_gain,
            debit_by='Cash',
            debit_amount=amount_mmk_up,
            credit_amount=amount_usd,
            credit_by='Cash'
        )


# CASE 04: SELL LOSS
    def test_004_sell_loss_01_tfx_ofo_open_forex_account_success(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        print('working_date: ' + working_date)
        global forex_account_sell_loss_mask, forex_account_sell_loss
        tfx_ofo_result = self.tfx_ofo(
            counterparty_code=customer_code_single_mask,
            catalogue_code=catalogue_code_sell,
            contract_rate=contract_rate_sell_loss,
            debit_currency='MMK',
            credit_currency='USD',
            reference_rate=reference_rate_bk,
            value_date=working_date,
            swap_point=swap_point_sell_loss,
            debit_by='Cash',
            debit_amount=amount_mmk_down,
            credit_amount=amount_usd,
            credit_by='Deposit',
            credit_account_no_dpt=dpt_usd,
            approve_later='Y'
        )
        transaction_references=tfx_ofo_result[0]
        forex_account_sell_loss_mask=tfx_ofo_result[1]
        # view transaction before approve
        self.tfx_ofo_view(
            transaction_references=transaction_references, 
            counterparty_code=customer_code_single_mask,
            catalogue_code=catalogue_code_sell,
            trade_type=trade_type_sell,
            contract_rate=contract_rate_sell_loss,
            debit_currency='MMK',
            credit_currency='USD',
            reference_rate=reference_rate_bk,
            value_date=working_date,
            swap_point=swap_point_sell_loss,
            debit_by='Cash',
            debit_amount=amount_mmk_down,
            credit_amount=amount_usd,
            credit_by='Deposit',
            credit_account_no_dpt=dpt_usd
        )
        # approve transaction
        self.transaction_approve(
            transaction_references=transaction_references, 
            username=username_approve,
            password=password_approve
        )
        forex_account_sell_loss=self.get_text_table_data('Account Number', 1)
        print(f'forex_account_sell_loss: {forex_account_sell_loss}')
        # view account information
        self.treasury_account_view(
            account_number=forex_account_sell_loss,
            account_status='Authoring',
            counterparty_code=customer_code_single_mask,
            catalogue_code=catalogue_code_sell,
            trade_type=trade_type_sell,
            trade_rate=contract_rate_sell_loss,
            debit_currency='MMK',
            credit_currency='USD',
            reference_rate=reference_rate_bk,
            value_date=working_date,
            swap_point=swap_point_sell_loss,
            debit_by='Cash',
            debit_amount=amount_mmk_down,
            credit_amount=amount_usd,
            credit_by='Deposit',
            credit_account=dpt_usd
        )
        # view transaction after approve
        self.tfx_ofo_view(
            transaction_references=transaction_references, 
            account_number=forex_account_sell_loss,
            counterparty_code=customer_code_single_mask,
            catalogue_code=catalogue_code_sell,
            trade_type=trade_type_sell,
            contract_rate=contract_rate_sell_loss,
            debit_currency='MMK',
            credit_currency='USD',
            reference_rate=reference_rate_bk,
            value_date=working_date,
            swap_point=swap_point_sell_loss,
            debit_by='Cash',
            debit_amount=amount_mmk_down,
            credit_amount=amount_usd,
            credit_by='Deposit',
            credit_account_no_dpt=dpt_usd
        )

    def test_004_sell_loss_02_tfx_fac_approve_forex_account_success(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        tfx_fac_result = self.tfx_fac(
            account_number=forex_account_sell_loss,
            counterparty_code=customer_code_single_mask,
            catalogue_code=catalogue_code_sell,
            trade_type=trade_type_sell,
            contract_rate=contract_rate_sell_loss,
            debit_currency='MMK',
            credit_currency='USD',
            reference_rate=reference_rate_bk,
            value_date=working_date,
            swap_point=swap_point_sell_loss,
            debit_by='Cash',
            debit_amount=amount_mmk_down,
            credit_amount=amount_usd,
            credit_by='Deposit',
            credit_account_no_dpt=dpt_usd,
            approve_later='Y'
        )
        transaction_references=tfx_fac_result[0]
        forex_account_sell_loss_mask=tfx_fac_result[1]
        # approve transaction
        self.transaction_approve(
            transaction_references=transaction_references, 
            username=username_approve,
            password=password_approve
        )
        # view transaction
        self.tfx_fac_view(
            transaction_references=transaction_references, 
            account_number=forex_account_sell_loss_mask,
            counterparty_code=customer_code_single_mask,
            catalogue_code=catalogue_code_sell,
            trade_type=trade_type_sell,
            contract_rate=contract_rate_sell_loss,
            debit_currency='MMK',
            credit_currency='USD',
            reference_rate=reference_rate_bk,
            value_date=working_date,
            swap_point=swap_point_sell_loss,
            debit_by='Cash',
            debit_amount=amount_mmk_down,
            credit_amount=amount_usd,
            credit_by='Deposit',
            credit_account_no_dpt=dpt_usd
        )
        # check account number of posting
        self.assert_posting_debit_account_number('1', branch_code+'-1010301000101-01')
        self.assert_posting_debit_amount('1', amount_mmk_down)
        self.assert_posting_credit_account_number('1', branch_code+'-5020101000101-01')
        self.assert_posting_credit_amount('1', amount_mmk_down)
        self.assert_posting_debit_account_number('2', branch_code+'-6020101000101-02')
        self.assert_posting_debit_amount('2', amount_usd)
        self.assert_posting_credit_account_number('2', branch_code+'-2020301010101-02')
        self.assert_posting_credit_amount('2', amount_usd)
        self.assert_posting_debit_account_number('3', branch_code+'-4030101000101-01')
        self.assert_posting_debit_amount('3', amount_dif_down)
        self.assert_posting_credit_account_number('3', branch_code+'-5020101000101-01')
        self.assert_posting_credit_amount('3', amount_dif_down)
        # view account information
        self.treasury_account_view(
            account_number=forex_account_sell_loss_mask,
            account_status='Approved contingent',
            counterparty_code=customer_code_single_mask,
            catalogue_code=catalogue_code_sell,
            trade_type=trade_type_sell,
            trade_rate=contract_rate_sell_loss,
            debit_currency='MMK',
            credit_currency='USD',
            reference_rate=reference_rate_bk,
            value_date=working_date,
            swap_point=swap_point_sell_loss,
            debit_by='Cash',
            debit_amount=amount_mmk_down,
            credit_amount=amount_usd,
            credit_by='Deposit',
            credit_account=dpt_usd
        )


# CASE 05: BUY NO GAIN LOSS
    def test_005_buy_01_tfx_ofo_open_forex_account_success(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        global forex_account_buy_mask, forex_account_buy
        tfx_ofo_result = self.tfx_ofo(
            counterparty_code=customer_code_single_mask,
            catalogue_code=catalogue_code_buy,
            contract_rate=reference_rate_bk,
            debit_currency='USD',
            credit_currency='MMK',
            reference_rate=reference_rate_bk,
            value_date=working_date,
            swap_point='0.000000000',
            debit_by='GL',
            debit_account_no_act=gl_usd,
            debit_amount=amount_usd,
            credit_amount=amount_mmk,
            credit_by='Cash',
            approve_later='Y'
        )
        transaction_references=tfx_ofo_result[0]
        forex_account_buy_mask=tfx_ofo_result[1]
        # view transaction before approve
        self.tfx_ofo_view(
            transaction_references=transaction_references, 
            counterparty_code=customer_code_single_mask,
            catalogue_code=catalogue_code_buy,
            trade_type=trade_type_buy,
            contract_rate=reference_rate_bk,
            debit_currency='USD',
            credit_currency='MMK',
            reference_rate=reference_rate_bk,
            value_date=working_date,
            swap_point='0.000000000',
            debit_by='GL',
            debit_account_no_act=gl_usd,
            debit_amount=amount_usd,
            credit_amount=amount_mmk,
            credit_by='Cash'
        )
        # approve transaction
        self.transaction_approve(
            transaction_references=transaction_references, 
            username=username_approve,
            password=password_approve
        )
        forex_account_buy=self.get_text_table_data('Account Number', 1)
        print(f'forex_account_buy: {forex_account_buy}')
        # view account information
        self.treasury_account_view(
            account_number=forex_account_buy,
            account_status='Authoring',
            counterparty_code=customer_code_single_mask,
            catalogue_code=catalogue_code_buy,
            trade_type=trade_type_buy,
            trade_rate=reference_rate_bk,
            debit_currency='USD',
            credit_currency='MMK',
            reference_rate=reference_rate_bk,
            value_date=working_date,
            swap_point='0.000000000',
            debit_by='GL',
            debit_account=gl_usd,
            debit_amount=amount_usd,
            credit_amount=amount_mmk,
            credit_by='Cash'
        )
        # view transaction after approve
        self.tfx_ofo_view(
            transaction_references=transaction_references, 
            account_number=forex_account_buy,
            counterparty_code=customer_code_single_mask,
            catalogue_code=catalogue_code_buy,
            trade_type=trade_type_buy,
            contract_rate=reference_rate_bk,
            debit_currency='USD',
            credit_currency='MMK',
            reference_rate=reference_rate_bk,
            value_date=working_date,
            swap_point='0.000000000',
            debit_by='GL',
            debit_account_no_act=gl_usd,
            debit_amount=amount_usd,
            credit_amount=amount_mmk,
            credit_by='Cash'
        )

    def test_005_buy_02_tfx_fac_approve_forex_account_success(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        tfx_fac_result = self.tfx_fac(
            account_number=forex_account_buy,
            counterparty_code=customer_code_single_mask,
            catalogue_code=catalogue_code_buy,
            trade_type=trade_type_buy,
            contract_rate=reference_rate_bk,
            debit_currency='USD',
            credit_currency='MMK',
            reference_rate=reference_rate_bk,
            value_date=working_date,
            swap_point='0.000000000',
            debit_by='GL',
            debit_account_no_act=gl_usd,
            debit_amount=amount_usd,
            credit_amount=amount_mmk,
            credit_by='Cash',
            approve_later='Y'
        )
        transaction_references=tfx_fac_result[0]
        forex_account_buy_mask=tfx_fac_result[1]
        # approve transaction
        self.transaction_approve(
            transaction_references=transaction_references, 
            username=username_approve,
            password=password_approve
        )
        # view transaction
        self.tfx_fac_view(
            transaction_references=transaction_references, 
            account_number=forex_account_buy_mask,
            counterparty_code=customer_code_single_mask,
            catalogue_code=catalogue_code_buy,
            trade_type=trade_type_buy,
            contract_rate=reference_rate_bk,
            debit_currency='USD',
            credit_currency='MMK',
            reference_rate=reference_rate_bk,
            value_date=working_date,
            swap_point='0.000000000',
            debit_by='GL',
            debit_account_no_act=gl_usd,
            debit_amount=amount_usd,
            credit_amount=amount_mmk,
            credit_by='Cash'
        )
        # check account number of posting
        self.assert_posting_debit_account_number('1', branch_code+'-5020101000101-01')
        self.assert_posting_debit_amount('1', amount_mmk)
        self.assert_posting_credit_account_number('1', branch_code+'-1010301000101-01')
        self.assert_posting_credit_amount('1', amount_mmk)
        self.assert_posting_debit_account_number('2', gl_usd)
        self.assert_posting_debit_amount('2', amount_usd)
        self.assert_posting_credit_account_number('2', branch_code+'-6020101000101-02')
        self.assert_posting_credit_amount('2', amount_usd)
        # view account information
        self.treasury_account_view(
            account_number=forex_account_buy_mask,
            account_status='Approved contingent',
            counterparty_code=customer_code_single_mask,
            catalogue_code=catalogue_code_buy,
            trade_type=trade_type_buy,
            trade_rate=reference_rate_bk,
            debit_currency='USD',
            credit_currency='MMK',
            reference_rate=reference_rate_bk,
            value_date=working_date,
            swap_point='0.000000000',
            debit_by='GL',
            debit_account=gl_usd,
            debit_amount=amount_usd,
            credit_amount=amount_mmk,
            credit_by='Cash'
        )


# CASE 06: SELL NO GAIN LOSS
    def test_006_sell_01_tfx_ofo_open_forex_account_success(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        print('working_date: ' + working_date)
        global forex_account_sell_mask, forex_account_sell
        tfx_ofo_result = self.tfx_ofo(
            counterparty_code=customer_code_single_mask,
            catalogue_code=catalogue_code_sell,
            contract_rate=reference_rate_bk,
            debit_currency='MMK',
            credit_currency='USD',
            reference_rate=reference_rate_bk,
            value_date=working_date,
            swap_point='0.000000000',
            debit_by='Deposit',
            debit_account_no_dpt=dpt_mmk,
            debit_amount=amount_mmk,
            credit_amount=amount_usd,
            credit_by='Deposit',
            credit_account_no_dpt=dpt_usd,
            approve_later='Y'
        )
        transaction_references=tfx_ofo_result[0]
        forex_account_sell_mask=tfx_ofo_result[1]
        # view transaction before approve
        self.tfx_ofo_view(
            transaction_references=transaction_references, 
            counterparty_code=customer_code_single_mask,
            catalogue_code=catalogue_code_sell,
            trade_type=trade_type_sell,
            contract_rate=reference_rate_bk,
            debit_currency='MMK',
            credit_currency='USD',
            reference_rate=reference_rate_bk,
            value_date=working_date,
            swap_point='0.000000000',
            debit_by='Deposit',
            debit_account_no_dpt=dpt_mmk,
            debit_amount=amount_mmk,
            credit_amount=amount_usd,
            credit_by='Deposit',
            credit_account_no_dpt=dpt_usd
        )
        # approve transaction
        self.transaction_approve(
            transaction_references=transaction_references, 
            username=username_approve,
            password=password_approve
        )
        forex_account_sell=self.get_text_table_data('Account Number', 1)
        print(f'forex_account_sell: {forex_account_sell}')
        # view account information
        self.treasury_account_view(
            account_number=forex_account_sell,
            account_status='Authoring',
            counterparty_code=customer_code_single_mask,
            catalogue_code=catalogue_code_sell,
            trade_type=trade_type_sell,
            trade_rate=reference_rate_bk,
            debit_currency='MMK',
            credit_currency='USD',
            reference_rate=reference_rate_bk,
            value_date=working_date,
            swap_point='0.000000000',
            debit_by='Deposit',
            debit_account=dpt_mmk,
            debit_amount=amount_mmk,
            credit_amount=amount_usd,
            credit_by='Deposit',
            credit_account=dpt_usd
        )
        # view transaction after approve
        self.tfx_ofo_view(
            transaction_references=transaction_references, 
            account_number=forex_account_sell,
            counterparty_code=customer_code_single_mask,
            catalogue_code=catalogue_code_sell,
            trade_type=trade_type_sell,
            contract_rate=reference_rate_bk,
            debit_currency='MMK',
            credit_currency='USD',
            reference_rate=reference_rate_bk,
            value_date=working_date,
            swap_point='0.000000000',
            debit_by='Deposit',
            debit_account_no_dpt=dpt_mmk,
            debit_amount=amount_mmk,
            credit_amount=amount_usd,
            credit_by='Deposit',
            credit_account_no_dpt=dpt_usd
        )

    def test_006_sell_02_dpt_cdp_deposit_money_to_deposit_account_success(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        # cash deposit account
        dpt_cdp_result = self.dpt_cdp(
            account_number=dpt_mmk,
            amount_deposit=amount_mmk,
            approve_on_form='Y',
            username=username_approve,
            password=password_approve
        )
        self.assertEqual(dpt_mmk, dpt_cdp_result[1])

    def test_006_sell_03_tfx_fac_approve_forex_account_success(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        tfx_fac_result = self.tfx_fac(
            account_number=forex_account_sell,
            counterparty_code=customer_code_single_mask,
            catalogue_code=catalogue_code_sell,
            trade_type=trade_type_sell,
            contract_rate=reference_rate_bk,
            debit_currency='MMK',
            credit_currency='USD',
            reference_rate=reference_rate_bk,
            value_date=working_date,
            swap_point='0.000000000',
            debit_by='Deposit',
            debit_account_no_dpt=dpt_mmk,
            debit_amount=amount_mmk,
            credit_amount=amount_usd,
            credit_by='Deposit',
            credit_account_no_dpt=dpt_usd,
            approve_later='Y'
        )
        transaction_references=tfx_fac_result[0]
        forex_account_sell_mask=tfx_fac_result[1]
        # approve transaction
        self.transaction_approve(
            transaction_references=transaction_references, 
            username=username_approve,
            password=password_approve
        )
        # view transaction
        self.tfx_fac_view(
            transaction_references=transaction_references, 
            account_number=forex_account_sell_mask,
            counterparty_code=customer_code_single_mask,
            catalogue_code=catalogue_code_sell,
            trade_type=trade_type_sell,
            contract_rate=reference_rate_bk,
            debit_currency='MMK',
            credit_currency='USD',
            reference_rate=reference_rate_bk,
            value_date=working_date,
            swap_point='0.000000000',
            debit_by='Deposit',
            debit_account_no_dpt=dpt_mmk,
            debit_amount=amount_mmk,
            credit_amount=amount_usd,
            credit_by='Deposit',
            credit_account_no_dpt=dpt_usd
        )
        # check account number of posting
        self.assert_posting_debit_account_number('1', branch_code+'-2020301010202-01')
        self.assert_posting_debit_amount('1', amount_mmk)
        self.assert_posting_credit_account_number('1', branch_code+'-5020101000101-01')
        self.assert_posting_credit_amount('1', amount_mmk)
        self.assert_posting_debit_account_number('2', branch_code+'-6020101000101-02')
        self.assert_posting_debit_amount('2', amount_usd)
        self.assert_posting_credit_account_number('2', branch_code+'-2020301010101-02')
        self.assert_posting_credit_amount('2', amount_usd)
        # view account information
        self.treasury_account_view(
            account_number=forex_account_sell_mask,
            account_status='Approved contingent',
            counterparty_code=customer_code_single_mask,
            catalogue_code=catalogue_code_sell,
            trade_type=trade_type_sell,
            trade_rate=reference_rate_bk,
            debit_currency='MMK',
            credit_currency='USD',
            reference_rate=reference_rate_bk,
            value_date=working_date,
            swap_point='0.000000000',
            debit_by='Deposit',
            debit_account=dpt_mmk,
            debit_amount=amount_mmk,
            credit_amount=amount_usd,
            credit_by='Deposit',
            credit_account=dpt_usd
        )


# CASE 07: BUY GAIN AMEND AND CANCEL
    def test_007_buy_gain_amend_and_cancel_01_tfx_ofo_open_forex_account_success(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        global forex_account_buy_gain_amend_and_cancel_mask, forex_account_buy_gain_amend_and_cancel
        tfx_ofo_result = self.tfx_ofo(
            counterparty_code=customer_code_single_mask,
            catalogue_code=catalogue_code_buy,
            contract_rate=contract_rate_buy_gain,
            debit_currency='USD',
            credit_currency='MMK',
            reference_rate=reference_rate_bk,
            value_date=working_date,
            swap_point=swap_point_buy_gain,
            debit_by='GL',
            debit_account_no_act=gl_usd,
            debit_amount=amount_usd,
            credit_amount=amount_mmk_down,
            credit_by='GL',
            credit_account_no_act=gl_mmk,
            approve_on_form='Y',
            username=username_approve,
            password=password_approve
        )
        forex_account_buy_gain_amend_and_cancel_mask=tfx_ofo_result[1]
        forex_account_buy_gain_amend_and_cancel=str(forex_account_buy_gain_amend_and_cancel_mask).replace('-', '')
        print(f'forex_account_buy_gain_amend_and_cancel: {forex_account_buy_gain_amend_and_cancel}')

    def test_007_buy_gain_amend_and_cancel_02_tfx_oaa_amend_forex_account_success(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        tfx_oaa_result = self.tfx_oaa(
            account_number=forex_account_buy_gain_amend_and_cancel,
            counterparty_code=customer_code_single_mask,
            catalogue_code=catalogue_code_buy,
            trade_type=trade_type_buy,
            contract_rate=contract_rate_buy_gain,
            contract_rate_update=contract_rate_buy_gain_update_loss,
            debit_currency='USD',
            credit_currency='MMK',
            reference_rate=reference_rate_bk,
            value_date=working_date,
            swap_point=swap_point_buy_gain,
            swap_point_update=swap_point_buy_gain_update_loss,
            debit_by='GL',
            debit_account_no_act=gl_usd,
            debit_amount=amount_usd,
            credit_amount=amount_mmk_down,
            credit_amount_update=amount_mmk_up,
            credit_by='GL',
            credit_by_update='Cash',
            credit_account_no_act=gl_mmk,
            approve_later='Y'
        )
        transaction_references=tfx_oaa_result[0]
        self.assertEqual(forex_account_buy_gain_amend_and_cancel_mask, tfx_oaa_result[1])
        # view transaction before approve
        self.tfx_oaa_view(
            transaction_references=transaction_references,
            account_number=forex_account_buy_gain_amend_and_cancel_mask,
            counterparty_code=customer_code_single_mask,
            catalogue_code=catalogue_code_buy,
            trade_type=trade_type_buy,
            contract_rate=contract_rate_buy_gain_update_loss,
            debit_currency='USD',
            credit_currency='MMK',
            reference_rate=reference_rate_bk,
            value_date=working_date,
            swap_point=swap_point_buy_gain_update_loss,
            debit_by='GL',
            debit_account_no_act=gl_usd,
            debit_amount=amount_usd,
            credit_amount=amount_mmk_up,
            credit_by='Cash'
        )
        # approve transaction
        self.transaction_approve(
            transaction_references=transaction_references, 
            username=username_approve,
            password=password_approve
        )
        # view transaction after approve
        self.tfx_oaa_view(
            transaction_references=transaction_references,
            account_number=forex_account_buy_gain_amend_and_cancel_mask,
            counterparty_code=customer_code_single_mask,
            catalogue_code=catalogue_code_buy,
            trade_type=trade_type_buy,
            contract_rate=contract_rate_buy_gain_update_loss,
            debit_currency='USD',
            credit_currency='MMK',
            reference_rate=reference_rate_bk,
            value_date=working_date,
            swap_point=swap_point_buy_gain_update_loss,
            debit_by='GL',
            debit_account_no_act=gl_usd,
            debit_amount=amount_usd,
            credit_amount=amount_mmk_up,
            credit_by='Cash'
        )
        # view account information
        self.treasury_account_view(
            account_number=forex_account_buy_gain_amend_and_cancel,
            account_status='Authoring',
            counterparty_code=customer_code_single_mask,
            catalogue_code=catalogue_code_buy,
            trade_type=trade_type_buy,
            trade_rate=contract_rate_buy_gain_update_loss,
            debit_currency='USD',
            credit_currency='MMK',
            reference_rate=reference_rate_bk,
            value_date=working_date,
            swap_point=swap_point_buy_gain_update_loss,
            debit_by='GL',
            debit_account=gl_usd,
            debit_amount=amount_usd,
            credit_amount=amount_mmk_up,
            credit_by='Cash',
            credit_account=''
        )

    def test_007_buy_gain_amend_and_cancel_03_tfx_fca_cancel_forex_account_success(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        tfx_fca_result = self.tfx_fca(
            account_number=forex_account_buy_gain_amend_and_cancel,
            counterparty_code=customer_code_single_mask,
            catalogue_code=catalogue_code_buy,
            trade_type=trade_type_buy,
            contract_rate=contract_rate_buy_gain_update_loss,
            debit_currency='USD',
            credit_currency='MMK',
            reference_rate=reference_rate_bk,
            value_date=working_date,
            swap_point=swap_point_buy_gain_update_loss,
            debit_by='GL',
            debit_account_no_act=gl_usd,
            debit_amount=amount_usd,
            credit_amount=amount_mmk_up,
            credit_by='Cash',
            approve_later='Y'
        )
        transaction_references=tfx_fca_result[0]
        self.assertEqual(forex_account_buy_gain_amend_and_cancel_mask, tfx_fca_result[1])
        # view transaction before approve
        self.tfx_fca_view(
            transaction_references=transaction_references, 
            account_number=forex_account_buy_gain_amend_and_cancel_mask,
            counterparty_code=customer_code_single_mask,
            catalogue_code=catalogue_code_buy,
            trade_type=trade_type_buy,
            contract_rate=contract_rate_buy_gain_update_loss,
            debit_currency='USD',
            credit_currency='MMK',
            reference_rate=reference_rate_bk,
            value_date=working_date,
            swap_point=swap_point_buy_gain_update_loss,
            debit_by='GL',
            debit_account_no_act=gl_usd,
            debit_amount=amount_usd,
            credit_amount=amount_mmk_up,
            credit_by='Cash'
        )
        # approve transaction
        self.transaction_approve(
            transaction_references=transaction_references, 
            username=username_approve,
            password=password_approve
        )
        # view transaction after approve
        self.tfx_fca_view(
            transaction_references=transaction_references, 
            account_number=forex_account_buy_gain_amend_and_cancel_mask,
            counterparty_code=customer_code_single_mask,
            catalogue_code=catalogue_code_buy,
            trade_type=trade_type_buy,
            contract_rate=contract_rate_buy_gain_update_loss,
            debit_currency='USD',
            credit_currency='MMK',
            reference_rate=reference_rate_bk,
            value_date=working_date,
            swap_point=swap_point_buy_gain_update_loss,
            debit_by='GL',
            debit_account_no_act=gl_usd,
            debit_amount=amount_usd,
            credit_amount=amount_mmk_up,
            credit_by='Cash'
        )
        # view account information
        self.treasury_account_view(
            account_number=forex_account_buy_gain_amend_and_cancel,
            account_status='Cancelled',
            counterparty_code=customer_code_single_mask,
            catalogue_code=catalogue_code_buy,
            trade_type=trade_type_buy,
            trade_rate=contract_rate_buy_gain_update_loss,
            debit_currency='USD',
            credit_currency='MMK',
            reference_rate=reference_rate_bk,
            value_date=working_date,
            swap_point=swap_point_buy_gain_update_loss,
            debit_by='GL',
            debit_account=gl_usd,
            debit_amount=amount_usd,
            credit_amount=amount_mmk_up,
            credit_by='Cash',
            credit_account=''
        )


# CASE 08: BUY LOSS AMEND AND CANCEL
    def test_008_buy_loss_amend_and_cancel_01_tfx_ofo_open_forex_account_success(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        global forex_account_buy_loss_amend_and_cancel_mask, forex_account_buy_loss_amend_and_cancel
        tfx_ofo_result = self.tfx_ofo(
            counterparty_code=customer_code_single_mask,
            catalogue_code=catalogue_code_buy,
            contract_rate=contract_rate_buy_loss,
            debit_currency='USD',
            credit_currency='MMK',
            reference_rate=reference_rate_bk,
            value_date=working_date,
            swap_point=swap_point_buy_loss,
            debit_by='Cash',
            debit_amount=amount_usd,
            credit_amount=amount_mmk_up,
            credit_by='GL',
            credit_account_no_act=gl_mmk,
            approve_on_form='Y',
            username=username_approve,
            password=password_approve
        )
        forex_account_buy_loss_amend_and_cancel_mask=tfx_ofo_result[1]
        forex_account_buy_loss_amend_and_cancel=str(forex_account_buy_loss_amend_and_cancel_mask).replace('-', '')
        print(f'forex_account_buy_loss_amend_and_cancel: {forex_account_buy_loss_amend_and_cancel}')

    def test_008_buy_loss_amend_and_cancel_02_tfx_oaa_amend_forex_account_success(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        tfx_oaa_result = self.tfx_oaa(
            account_number=forex_account_buy_loss_amend_and_cancel,
            counterparty_code=customer_code_single_mask,
            catalogue_code=catalogue_code_buy,
            trade_type=trade_type_buy,
            contract_rate=contract_rate_buy_loss,
            contract_rate_update=contract_rate_buy_loss_update_gain,
            debit_currency='USD',
            credit_currency='MMK',
            reference_rate=reference_rate_bk,
            value_date=working_date,
            swap_point=swap_point_buy_loss,
            swap_point_update=swap_point_buy_loss_update_gain,
            debit_by='Cash',
            debit_by_update='GL',
            debit_account_no_act_update=gl_usd,
            debit_amount=amount_usd,
            credit_amount=amount_mmk_up,
            credit_amount_update=amount_mmk_down,
            credit_by='GL',
            credit_account_no_act=gl_mmk,
            approve_later='Y'
        )
        transaction_references=tfx_oaa_result[0]
        self.assertEqual(forex_account_buy_loss_amend_and_cancel_mask, tfx_oaa_result[1])
        # view transaction before approve
        self.tfx_oaa_view(
            transaction_references=transaction_references,
            account_number=forex_account_buy_loss_amend_and_cancel_mask,
            counterparty_code=customer_code_single_mask,
            catalogue_code=catalogue_code_buy,
            trade_type=trade_type_buy,
            contract_rate=contract_rate_buy_loss_update_gain,
            debit_currency='USD',
            credit_currency='MMK',
            reference_rate=reference_rate_bk,
            value_date=working_date,
            swap_point=swap_point_buy_loss_update_gain,
            debit_by='GL',
            debit_account_no_act=gl_usd,
            debit_amount=amount_usd,
            credit_amount=amount_mmk_down,
            credit_by='GL',
            credit_account_no_act=gl_mmk
        )
        # view account information before approve
        self.treasury_account_view(
            account_number=forex_account_buy_loss_amend_and_cancel,
            account_status='Authoring',
            counterparty_code=customer_code_single_mask,
            catalogue_code=catalogue_code_buy,
            trade_type=trade_type_buy,
            trade_rate=contract_rate_buy_loss,
            debit_currency='USD',
            credit_currency='MMK',
            reference_rate=reference_rate_bk,
            value_date=working_date,
            swap_point=swap_point_buy_loss,
            debit_by='Cash',
            debit_amount=amount_usd,
            credit_amount=amount_mmk_up,
            credit_by='GL',
            credit_account=gl_mmk
        )
        # approve transaction
        self.transaction_approve(
            transaction_references=transaction_references, 
            username=username_approve,
            password=password_approve
        )
        # view transaction after approve
        self.tfx_oaa_view(
            transaction_references=transaction_references, 
            account_number=forex_account_buy_loss_amend_and_cancel,
            counterparty_code=customer_code_single_mask,
            catalogue_code=catalogue_code_buy,
            trade_type=trade_type_buy,
            contract_rate=contract_rate_buy_loss_update_gain,
            debit_currency='USD',
            credit_currency='MMK',
            reference_rate=reference_rate_bk,
            value_date=working_date,
            swap_point=swap_point_buy_loss_update_gain,
            debit_by='GL',
            debit_account_no_act=gl_usd,
            debit_amount=amount_usd,
            credit_amount=amount_mmk_down,
            credit_by='GL',
            credit_account_no_act=gl_mmk
        )
        # view account information after approve
        self.treasury_account_view(
            account_number=forex_account_buy_loss_amend_and_cancel,
            account_status='Authoring',
            counterparty_code=customer_code_single_mask,
            catalogue_code=catalogue_code_buy,
            trade_type=trade_type_buy,
            trade_rate=contract_rate_buy_loss_update_gain,
            debit_currency='USD',
            credit_currency='MMK',
            reference_rate=reference_rate_bk,
            value_date=working_date,
            swap_point=swap_point_buy_loss_update_gain,
            debit_by='GL',
            debit_account=gl_usd,
            debit_amount=amount_usd,
            credit_amount=amount_mmk_down,
            credit_by='GL',
            credit_account=gl_mmk
        )

    def test_008_buy_loss_amend_and_cancel_03_tfx_fca_cancel_forex_account_success(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        tfx_fca_result = self.tfx_fca(
            account_number=forex_account_buy_loss_amend_and_cancel,
            counterparty_code=customer_code_single_mask,
            catalogue_code=catalogue_code_buy,
            trade_type=trade_type_buy,
            contract_rate=contract_rate_buy_loss_update_gain,
            debit_currency='USD',
            credit_currency='MMK',
            reference_rate=reference_rate_bk,
            value_date=working_date,
            swap_point=swap_point_buy_loss_update_gain,
            debit_by='GL',
            debit_account_no_act=gl_usd,
            debit_amount=amount_usd,
            credit_amount=amount_mmk_down,
            credit_by='GL',
            credit_account_no_act=gl_mmk,
            approve_later='Y'
        )
        transaction_references=tfx_fca_result[0]
        self.assertEqual(forex_account_buy_loss_amend_and_cancel_mask, tfx_fca_result[1])
        # view transaction before approve
        self.tfx_fca_view(
            transaction_references=transaction_references, 
            account_number=forex_account_buy_loss_amend_and_cancel,
            counterparty_code=customer_code_single_mask,
            catalogue_code=catalogue_code_buy,
            trade_type=trade_type_buy,
            contract_rate=contract_rate_buy_loss_update_gain,
            debit_currency='USD',
            credit_currency='MMK',
            reference_rate=reference_rate_bk,
            value_date=working_date,
            swap_point=swap_point_buy_loss_update_gain,
            debit_by='GL',
            debit_account_no_act=gl_usd,
            debit_amount=amount_usd,
            credit_amount=amount_mmk_down,
            credit_by='GL',
            credit_account_no_act=gl_mmk
        )
        # approve transaction
        self.transaction_approve(
            transaction_references=transaction_references, 
            username=username_approve,
            password=password_approve
        )
        # view transaction after approve
        self.tfx_fca_view(
            transaction_references=transaction_references, 
            account_number=forex_account_buy_loss_amend_and_cancel,
            counterparty_code=customer_code_single_mask,
            catalogue_code=catalogue_code_buy,
            trade_type=trade_type_buy,
            contract_rate=contract_rate_buy_loss_update_gain,
            debit_currency='USD',
            credit_currency='MMK',
            reference_rate=reference_rate_bk,
            value_date=working_date,
            swap_point=swap_point_buy_loss_update_gain,
            debit_by='GL',
            debit_account_no_act=gl_usd,
            debit_amount=amount_usd,
            credit_amount=amount_mmk_down,
            credit_by='GL',
            credit_account_no_act=gl_mmk
        )
        # view account information
        self.treasury_account_view(
            account_number=forex_account_buy_loss_amend_and_cancel,
            account_status='Cancelled',
            counterparty_code=customer_code_single_mask,
            catalogue_code=catalogue_code_buy,
            trade_type=trade_type_buy,
            trade_rate=contract_rate_buy_loss_update_gain,
            debit_currency='USD',
            credit_currency='MMK',
            reference_rate=reference_rate_bk,
            value_date=working_date,
            swap_point=swap_point_buy_loss_update_gain,
            debit_by='GL',
            debit_account=gl_usd,
            debit_amount=amount_usd,
            credit_amount=amount_mmk_down,
            credit_by='GL',
            credit_account=gl_mmk
        )


# CASE 09: SELL GAIN AMEND AND CANCEL
    def test_009_sell_gain_amend_and_cancel_01_tfx_ofo_open_forex_account_success(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        global forex_account_sell_gain_amend_and_cancel_mask, forex_account_sell_gain_amend_and_cancel
        tfx_ofo_result = self.tfx_ofo(
            counterparty_code=customer_code_single_mask,
            catalogue_code=catalogue_code_sell,
            contract_rate=contract_rate_sell_gain,
            debit_currency='MMK',
            credit_currency='USD',
            reference_rate=reference_rate_bk,
            value_date=working_date,
            swap_point=swap_point_sell_gain,
            debit_by='Cash',
            debit_amount=amount_mmk_up,
            credit_amount=amount_usd,
            credit_by='Cash',
            approve_on_form='Y',
            username=username_approve,
            password=password_approve
        )
        forex_account_sell_gain_amend_and_cancel_mask=tfx_ofo_result[1]
        forex_account_sell_gain_amend_and_cancel=str(forex_account_sell_gain_amend_and_cancel_mask).replace('-', '')
        print(f'forex_account_sell_gain_amend_and_cancel: {forex_account_sell_gain_amend_and_cancel}')

    def test_009_sell_gain_amend_and_cancel_02_tfx_oaa_amend_forex_account_success(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        tfx_oaa_result = self.tfx_oaa(
            account_number=forex_account_sell_gain_amend_and_cancel,
            counterparty_code=customer_code_single_mask,
            catalogue_code=catalogue_code_sell,
            trade_type=trade_type_sell,
            contract_rate=contract_rate_sell_gain,
            contract_rate_update=contract_rate_sell_gain_update,
            debit_currency='MMK',
            credit_currency='USD',
            reference_rate=reference_rate_bk,
            value_date=working_date,
            swap_point=swap_point_sell_gain,
            swap_point_update=swap_point_sell_gain_update,
            debit_by='Cash',
            debit_amount=amount_mmk_up,
            debit_amount_update=amount_mmk_up_update,
            credit_amount=amount_usd,
            credit_amount_update=amount_usd_update,
            credit_by='Cash',
            approve_later='Y'
        )
        transaction_references=tfx_oaa_result[0]
        self.assertEqual(forex_account_sell_gain_amend_and_cancel_mask, tfx_oaa_result[1])
        # view transaction before approve
        self.tfx_oaa_view(
            transaction_references=transaction_references, 
            account_number=forex_account_sell_gain_amend_and_cancel_mask,
            counterparty_code=customer_code_single_mask,
            catalogue_code=catalogue_code_sell,
            trade_type=trade_type_sell,
            contract_rate=contract_rate_sell_gain_update,
            debit_currency='MMK',
            credit_currency='USD',
            reference_rate=reference_rate_bk,
            value_date=working_date,
            swap_point=swap_point_sell_gain_update,
            debit_by='Cash',
            debit_amount=amount_mmk_up_update,
            credit_amount=amount_usd_update,
            credit_by='Cash'
        )
        # view account information before approve
        self.treasury_account_view(
            account_number=forex_account_sell_gain_amend_and_cancel_mask,
            account_status='Authoring',
            counterparty_code=customer_code_single_mask,
            catalogue_code=catalogue_code_sell,
            trade_type=trade_type_sell,
            trade_rate=contract_rate_sell_gain,
            debit_currency='MMK',
            credit_currency='USD',
            reference_rate=reference_rate_bk,
            value_date=working_date,
            swap_point=swap_point_sell_gain,
            debit_by='Cash',
            debit_amount=amount_mmk_up,
            credit_amount=amount_usd,
            credit_by='Cash'
        )
        # approve transaction
        self.transaction_approve(
            transaction_references=transaction_references, 
            username=username_approve,
            password=password_approve
        )
        # view transaction after approve
        self.tfx_oaa_view(
            transaction_references=transaction_references, 
            account_number=forex_account_sell_gain_amend_and_cancel_mask,
            counterparty_code=customer_code_single_mask,
            catalogue_code=catalogue_code_sell,
            trade_type=trade_type_sell,
            contract_rate=contract_rate_sell_gain_update,
            debit_currency='MMK',
            credit_currency='USD',
            reference_rate=reference_rate_bk,
            value_date=working_date,
            swap_point=swap_point_sell_gain_update,
            debit_by='Cash',
            debit_amount=amount_mmk_up_update,
            credit_amount=amount_usd_update,
            credit_by='Cash'
        )
        # view account information after approve
        self.treasury_account_view(
            account_number=forex_account_sell_gain_amend_and_cancel_mask,
            account_status='Authoring',
            counterparty_code=customer_code_single_mask,
            catalogue_code=catalogue_code_sell,
            trade_type=trade_type_sell,
            trade_rate=contract_rate_sell_gain_update,
            debit_currency='MMK',
            credit_currency='USD',
            reference_rate=reference_rate_bk,
            value_date=working_date,
            swap_point=swap_point_sell_gain_update,
            debit_by='Cash',
            debit_amount=amount_mmk_up_update,
            credit_amount=amount_usd_update,
            credit_by='Cash'
        )

    def test_009_sell_gain_amend_and_cancel_03_tfx_fca_cancel_forex_account_success(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        tfx_fca_result = self.tfx_fca(
            account_number=forex_account_sell_gain_amend_and_cancel,
            counterparty_code=customer_code_single_mask,
            catalogue_code=catalogue_code_sell,
            trade_type=trade_type_sell,
            contract_rate=contract_rate_sell_gain_update,
            debit_currency='MMK',
            credit_currency='USD',
            reference_rate=reference_rate_bk,
            value_date=working_date,
            swap_point=swap_point_sell_gain_update,
            debit_by='Cash',
            debit_amount=amount_mmk_up_update,
            credit_amount=amount_usd_update,
            credit_by='Cash',
            approve_later='Y'
        )
        transaction_references=tfx_fca_result[0]
        self.assertEqual(forex_account_sell_gain_amend_and_cancel_mask, tfx_fca_result[1])
        # view transaction before approve
        self.tfx_fca_view(
            transaction_references=transaction_references, 
            account_number=forex_account_sell_gain_amend_and_cancel,
            counterparty_code=customer_code_single_mask,
            catalogue_code=catalogue_code_sell,
            trade_type=trade_type_sell,
            contract_rate=contract_rate_sell_gain_update,
            debit_currency='MMK',
            credit_currency='USD',
            reference_rate=reference_rate_bk,
            value_date=working_date,
            swap_point=swap_point_sell_gain_update,
            debit_by='Cash',
            debit_amount=amount_mmk_up_update,
            credit_amount=amount_usd_update,
            credit_by='Cash'
        )
        # view account information before approve
        self.treasury_account_view(
            account_number=forex_account_sell_gain_amend_and_cancel,
            account_status='Authoring',
            counterparty_code=customer_code_single_mask,
            catalogue_code=catalogue_code_sell,
            trade_type=trade_type_sell,
            trade_rate=contract_rate_sell_gain_update,
            debit_currency='MMK',
            credit_currency='USD',
            reference_rate=reference_rate_bk,
            value_date=working_date,
            swap_point=swap_point_sell_gain_update,
            debit_by='Cash',
            debit_amount=amount_mmk_up_update,
            credit_amount=amount_usd_update,
            credit_by='Cash'
        )
        # approve transaction
        self.transaction_approve(
            transaction_references=transaction_references, 
            username=username_approve,
            password=password_approve
        )
        # view transaction after approve
        self.tfx_fca_view(
            transaction_references=transaction_references, 
            account_number=forex_account_sell_gain_amend_and_cancel,
            counterparty_code=customer_code_single_mask,
            catalogue_code=catalogue_code_sell,
            trade_type=trade_type_sell,
            contract_rate=contract_rate_sell_gain_update,
            debit_currency='MMK',
            credit_currency='USD',
            reference_rate=reference_rate_bk,
            value_date=working_date,
            swap_point=swap_point_sell_gain_update,
            debit_by='Cash',
            debit_amount=amount_mmk_up_update,
            credit_amount=amount_usd_update,
            credit_by='Cash'
        )
        # view account information
        self.treasury_account_view(
            account_number=forex_account_sell_gain_amend_and_cancel,
            account_status='Cancelled',
            counterparty_code=customer_code_single_mask,
            catalogue_code=catalogue_code_sell,
            trade_type=trade_type_sell,
            trade_rate=contract_rate_sell_gain_update,
            debit_currency='MMK',
            credit_currency='USD',
            reference_rate=reference_rate_bk,
            value_date=working_date,
            swap_point=swap_point_sell_gain_update,
            debit_by='Cash',
            debit_amount=amount_mmk_up_update,
            credit_amount=amount_usd_update,
            credit_by='Cash'
        )


# CASE 10: SELL LOSS AMEND AND CANCEL
    def test_010_sell_loss_amend_and_cancel_01_tfx_ofo_open_forex_account_success(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        print('working_date: ' + working_date)
        global forex_account_sell_loss_amend_and_cancel_mask, forex_account_sell_loss_amend_and_cancel
        tfx_ofo_result = self.tfx_ofo(
            counterparty_code=customer_code_single_mask,
            catalogue_code=catalogue_code_sell,
            contract_rate=contract_rate_sell_loss,
            debit_currency='MMK',
            credit_currency='USD',
            reference_rate=reference_rate_bk,
            value_date=working_date,
            swap_point=swap_point_sell_loss,
            debit_by='Cash',
            debit_amount=amount_mmk_down,
            credit_amount=amount_usd,
            credit_by='Deposit',
            credit_account_no_dpt=dpt_usd,
            approve_on_form='Y',
            username=username_approve,
            password=password_approve
        )
        forex_account_sell_loss_amend_and_cancel_mask=tfx_ofo_result[1]
        forex_account_sell_loss_amend_and_cancel=str(forex_account_sell_loss_amend_and_cancel_mask).replace('-', '')
        print(f'forex_account_sell_loss_amend_and_cancel: {forex_account_sell_loss_amend_and_cancel}')

    def test_010_sell_loss_amend_and_cancel_02_tfx_oaa_amend_forex_account_success(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        tfx_oaa_result = self.tfx_oaa(
            account_number=forex_account_sell_loss_amend_and_cancel,
            counterparty_code=customer_code_single_mask,
            catalogue_code=catalogue_code_sell,
            trade_type=trade_type_sell,
            contract_rate=contract_rate_sell_loss,
            contract_rate_update=contract_rate_sell_loss_update,
            debit_currency='MMK',
            credit_currency='USD',
            reference_rate=reference_rate_bk,
            value_date=working_date,
            swap_point=swap_point_sell_loss,
            swap_point_update=swap_point_sell_loss_update,
            debit_by='Cash',
            debit_amount=amount_mmk_down,
            debit_amount_update=amount_mmk_down_update,
            credit_amount=amount_usd,
            credit_amount_update=amount_usd_update,
            credit_by='Deposit',
            credit_account_no_dpt=dpt_usd,
            approve_later='Y'
        )
        transaction_references=tfx_oaa_result[0]
        self.assertEqual(forex_account_sell_loss_amend_and_cancel_mask, tfx_oaa_result[1])
        # view transaction before approve
        self.tfx_oaa_view(
            transaction_references=transaction_references, 
            account_number=forex_account_sell_loss_amend_and_cancel_mask,
            counterparty_code=customer_code_single_mask,
            catalogue_code=catalogue_code_sell,
            trade_type=trade_type_sell,
            contract_rate=contract_rate_sell_loss_update,
            debit_currency='MMK',
            credit_currency='USD',
            reference_rate=reference_rate_bk,
            value_date=working_date,
            swap_point=swap_point_sell_loss_update,
            debit_by='Cash',
            debit_amount=amount_mmk_down_update,
            credit_amount=amount_usd_update,
            credit_by='Deposit',
            credit_account_no_dpt=dpt_usd
        )
        # view account information before approve
        self.treasury_account_view(
            account_number=forex_account_sell_loss_amend_and_cancel,
            account_status='Authoring',
            counterparty_code=customer_code_single_mask,
            catalogue_code=catalogue_code_sell,
            trade_type=trade_type_sell,
            trade_rate=contract_rate_sell_loss,
            debit_currency='MMK',
            credit_currency='USD',
            reference_rate=reference_rate_bk,
            value_date=working_date,
            swap_point=swap_point_sell_loss,
            debit_by='Cash',
            debit_amount=amount_mmk_down,
            credit_amount=amount_usd,
            credit_by='Deposit',
            credit_account=dpt_usd
        )
        # approve transaction
        self.transaction_approve(
            transaction_references=transaction_references, 
            username=username_approve,
            password=password_approve
        )
        # view transaction after approve
        self.tfx_oaa_view(
            transaction_references=transaction_references, 
            account_number=forex_account_sell_loss_amend_and_cancel_mask,
            counterparty_code=customer_code_single_mask,
            catalogue_code=catalogue_code_sell,
            trade_type=trade_type_sell,
            contract_rate=contract_rate_sell_loss_update,
            debit_currency='MMK',
            credit_currency='USD',
            reference_rate=reference_rate_bk,
            value_date=working_date,
            swap_point=swap_point_sell_loss_update,
            debit_by='Cash',
            debit_amount=amount_mmk_down_update,
            credit_amount=amount_usd_update,
            credit_by='Deposit',
            credit_account_no_dpt=dpt_usd
        )
        # view account information after approve
        self.treasury_account_view(
            account_number=forex_account_sell_loss_amend_and_cancel_mask,
            account_status='Authoring',
            counterparty_code=customer_code_single_mask,
            catalogue_code=catalogue_code_sell,
            trade_type=trade_type_sell,
            trade_rate=contract_rate_sell_loss_update,
            debit_currency='MMK',
            credit_currency='USD',
            reference_rate=reference_rate_bk,
            value_date=working_date,
            swap_point=swap_point_sell_loss_update,
            debit_by='Cash',
            debit_amount=amount_mmk_down_update,
            credit_amount=amount_usd_update,
            credit_by='Deposit',
            credit_account=dpt_usd
        )

    def test_010_sell_loss_amend_and_cancel_03_tfx_fca_cancel_forex_account_success(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        tfx_fca_result = self.tfx_fca(
            account_number=forex_account_sell_loss_amend_and_cancel,
            counterparty_code=customer_code_single_mask,
            catalogue_code=catalogue_code_sell,
            trade_type=trade_type_sell,
            contract_rate=contract_rate_sell_loss_update,
            debit_currency='MMK',
            credit_currency='USD',
            reference_rate=reference_rate_bk,
            value_date=working_date,
            swap_point=swap_point_sell_loss_update,
            debit_by='Cash',
            debit_amount=amount_mmk_down_update,
            credit_amount=amount_usd_update,
            credit_by='Deposit',
            credit_account_no_dpt=dpt_usd,
            approve_later='Y'
        )
        transaction_references=tfx_fca_result[0]
        self.assertEqual(forex_account_sell_loss_amend_and_cancel_mask, tfx_fca_result[1])
        # view transaction before approve
        self.tfx_fca_view(
            transaction_references=transaction_references, 
            account_number=forex_account_sell_loss_amend_and_cancel,
            counterparty_code=customer_code_single_mask,
            catalogue_code=catalogue_code_sell,
            trade_type=trade_type_sell,
            contract_rate=contract_rate_sell_loss_update,
            debit_currency='MMK',
            credit_currency='USD',
            reference_rate=reference_rate_bk,
            value_date=working_date,
            swap_point=swap_point_sell_loss_update,
            debit_by='Cash',
            debit_amount=amount_mmk_down_update,
            credit_amount=amount_usd_update,
            credit_by='Deposit',
            credit_account_no_dpt=dpt_usd
        )
        # view account information before approve
        self.treasury_account_view(
            account_number=forex_account_sell_loss_amend_and_cancel_mask,
            account_status='Authoring',
            counterparty_code=customer_code_single_mask,
            catalogue_code=catalogue_code_sell,
            trade_type=trade_type_sell,
            trade_rate=contract_rate_sell_loss_update,
            debit_currency='MMK',
            credit_currency='USD',
            reference_rate=reference_rate_bk,
            value_date=working_date,
            swap_point=swap_point_sell_loss_update,
            debit_by='Cash',
            debit_amount=amount_mmk_down_update,
            credit_amount=amount_usd_update,
            credit_by='Deposit',
            credit_account=dpt_usd
        )
        # approve transaction
        self.transaction_approve(
            transaction_references=transaction_references, 
            username=username_approve,
            password=password_approve
        )
        # view transaction after approve
        self.tfx_fca_view(
            transaction_references=transaction_references, 
            account_number=forex_account_sell_loss_amend_and_cancel,
            counterparty_code=customer_code_single_mask,
            catalogue_code=catalogue_code_sell,
            trade_type=trade_type_sell,
            contract_rate=contract_rate_sell_loss_update,
            debit_currency='MMK',
            credit_currency='USD',
            reference_rate=reference_rate_bk,
            value_date=working_date,
            swap_point=swap_point_sell_loss_update,
            debit_by='Cash',
            debit_amount=amount_mmk_down_update,
            credit_amount=amount_usd_update,
            credit_by='Deposit',
            credit_account_no_dpt=dpt_usd
        )
        # view account information after approve
        self.treasury_account_view(
            account_number=forex_account_sell_loss_amend_and_cancel_mask,
            account_status='Cancelled',
            counterparty_code=customer_code_single_mask,
            catalogue_code=catalogue_code_sell,
            trade_type=trade_type_sell,
            trade_rate=contract_rate_sell_loss_update,
            debit_currency='MMK',
            credit_currency='USD',
            reference_rate=reference_rate_bk,
            value_date=working_date,
            swap_point=swap_point_sell_loss_update,
            debit_by='Cash',
            debit_amount=amount_mmk_down_update,
            credit_amount=amount_usd_update,
            credit_by='Deposit',
            credit_account=dpt_usd
        )


# CASE 11: BUY NO GAIN LOSS AMEND AND CANCEL


# CASE 12: SELL NO GAIN LOSS AMEND AND CANCEL

if __name__ == '__main__': 
    webui_test.main()