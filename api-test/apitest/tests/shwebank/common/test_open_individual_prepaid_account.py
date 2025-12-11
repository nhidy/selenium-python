from datetime import datetime
import json
import random
import pytest
import time

from apitest.src.configs import USER_LOGIN
from apitest.src.utilities.requestUtility import RequestUtility

from apitest.src.helpers.customer.customer_single_helpers import CustomerSingleHelper
from apitest.src.payloads.customer.customer_single_payload import CustomerSinglePayload
from apitest.src.helpers.customer.customer_fo_helpers import CustomerFOHelper
from apitest.src.payloads.customer.customer_fo_payload import CustomerFOPayload
customer_single_payload = CustomerSinglePayload()
customer_fo_payload = CustomerFOPayload()
from apitest.src.helpers.deposit.deposit_fo_helpers import DepositFOHelper
from apitest.src.payloads.deposit.deposit_fo_payload import DepositFOPayload
from apitest.src.helpers.deposit.deposit_account_helpers import DepositAccountHelper
from apitest.src.payloads.deposit.deposit_account_payload import DepositAccountPayload
deposit_account_payload = DepositAccountPayload()
deposit_fo_payload = DepositFOPayload()

# customer
random_num=random.randrange(100, 100000)
working_date='2026-05-06' 
currency_code_mmk='MMK'
date_time = datetime.now().strftime('%d/%m/%Y %H:%M:%S')

# data open saving deposit
catalog_code_saving_deposit='BSMMK0000'
catalog_name_saving_deposit='Bonus savings account in MMK'
deposit_type_saving_deposit='Savings'
deposit_purpose_saving_deposit='P'
account_type_saving_deposit='1'
account_name_saving_deposit='TEST AUTO BONUS SAVING ' + date_time
rollover_saving_deposit='N'
auto_transfer_option_saving_deposit='N'
deposit_sub_type_saving_deposit='S2'
customer_type='C'
description_dpt_opn='1100: Open new deposit account'
im_banking='false'
mpu_card='false'
pc_book='false'
wallet='false'

# data open fixed deposit
catalog_code_prepaid_fixed_deposit='PR120MMK0'
catalog_name_prepaid_fixed_deposit='SHWE prepaid fixed deposit account by cash in MMK'
deposit_type_prepaid_fixed_deposit='Fixed Deposit'
deposit_sub_type_prepaid_fixed_deposit='T6'
deposit_purpose_prepaid_fixed_deposit='S'
account_type_prepaid_fixed_deposit='1'
account_name_prepaid_fixed_deposit='TEST AUTO PREPAID FD ' + date_time
rollover_prepaid_fixed_deposit='N'
auto_transfer_option_prepaid_fixed_deposit='A'

# data approve deposit
description_dpt_apr='Approve deposit account'

# data cash deposit current
amount_deposit_current=1000000.00
exchange_rate=1
deposit_type_cash_current='C'
description_dpt_cdp='1110: Cash deposit'

# data cash deposit fixed
amount_deposit_fixed=150000000
exchange_rate=1
deposit_type_cash_fixed='T'
description_dpt_cdp='1110: Cash deposit'

@pytest.fixture(scope='session')
def user():
    user_service = USER_LOGIN['user5']
    req = RequestUtility(user_service)
    req.login_neptune()
    req.login_service()
    return req

@pytest.mark.open_individual_prepaid_account
class TestOpenIndividualPrepaidAccount(object):

    @pytest.mark.open_deposit_account
    def test_001_open_individual_deposit_account(self, user):
        helper_fo_dpt = DepositFOHelper(user)
        i = 1
        while i < 201:
            # open50 current deposit account 
            global account_number_new_saving_deposit
            account_number_new_saving_deposit = ''
            fields_data = deposit_fo_payload.dpt_opn(
                customer_type=customer_type,
                customer_code='11056754',
                catalog_code=catalog_code_saving_deposit,
                catalog_name=catalog_name_saving_deposit,
                deposit_type=deposit_type_saving_deposit,
                deposit_purpose=deposit_purpose_saving_deposit,
                account_type=account_type_saving_deposit,
                account_name=account_name_saving_deposit + ' ' + str(i),
                deposit_sub_type=deposit_sub_type_saving_deposit,
                rollover=rollover_saving_deposit,
                auto_transfer_option=auto_transfer_option_saving_deposit,
                description=description_dpt_opn,
                im_banking=im_banking,
                mpu_card=mpu_card,
                pc_book=pc_book,
                wallet=wallet,
            )
            try:
                rs = helper_fo_dpt.DPT_OPN(fields_data)
                assert 'account_number' in rs, f'Key \"account_number\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                account_number_new_saving_deposit = rs['account_number']
                assert 'transaction_number' in rs, f'Key \"transaction_number\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                transaction_number = rs['transaction_number']
                # assert transaction_number != ''
                print('Transaction number DPT_OPN: ', transaction_number)
            except:
                assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            
            # approve current deposit account
            fields_data = deposit_fo_payload.dpt_apr(
                account_number=account_number_new_saving_deposit,
                account_holder_name=account_name_saving_deposit,
                description=description_dpt_apr
            )
            try:
                rs = helper_fo_dpt.DPT_APR(fields_data)
                assert 'account_number' in rs, f'Key \"account_number\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                assert 'transaction_number' in rs, f'Key \"transaction_number\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                transaction_number = rs['transaction_number']
                # assert transaction_number != ''
                print('Transaction number DPT_APR: ', transaction_number)
            except:
                assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'

            # cash deposit
            fields_data = deposit_fo_payload.dpt_cdp(
                account_number=account_number_new_saving_deposit,
                amount_deposit=amount_deposit_current,
                amount=amount_deposit_current,
                currency_deposit=currency_code_mmk,
                values_date=working_date,
                customer_code='11056754',
                cash_amount_bcy=amount_deposit_current,
                cash_exchange_rate=exchange_rate,
                cash_amount=amount_deposit_current,
                cash_currency=currency_code_mmk,
                account_name=account_name_saving_deposit,
                exchange_rate=exchange_rate,
                cross_rate=exchange_rate,
                deposit_type=deposit_type_cash_current,
                id_issue_date=working_date,
                description=description_dpt_cdp
            )
            try:
                rs = helper_fo_dpt.DPT_CDP(fields_data)
                assert 'account_number' in rs, f'Key \"account_number\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                assert 'transaction_number' in rs, f'Key \"transaction_number\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                transaction_number = rs['transaction_number']
                # assert transaction_number != ''
                print('Transaction number DPT_CDP: ', transaction_number)
            except:
                assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'

            # open fixed deposit account 1
            global account_number_new_prepaid_fixed_deposit_001
            account_number_new_prepaid_fixed_deposit_001 = ''
            fields_data = deposit_fo_payload.dpt_opn(
                customer_type=customer_type,
                customer_code='11056754',
                catalog_code=catalog_code_prepaid_fixed_deposit,
                catalog_name=catalog_name_prepaid_fixed_deposit,
                deposit_type=deposit_type_prepaid_fixed_deposit,
                deposit_sub_type=deposit_sub_type_prepaid_fixed_deposit,
                deposit_purpose=deposit_purpose_prepaid_fixed_deposit,
                account_type=account_type_prepaid_fixed_deposit,
                account_name=account_name_prepaid_fixed_deposit + ' ' + str(i),
                rollover=rollover_prepaid_fixed_deposit,
                auto_transfer_option=auto_transfer_option_prepaid_fixed_deposit,
                to_account_number=account_number_new_saving_deposit,
                description=description_dpt_opn,
                im_banking=im_banking,
                mpu_card=mpu_card,
                pc_book=pc_book,
                wallet=wallet,
            )
            try:
                rs = helper_fo_dpt.DPT_OPN(fields_data)
                assert 'account_number' in rs, f'Key \"account_number\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                account_number_new_prepaid_fixed_deposit_001 = rs['account_number']
                assert 'transaction_number' in rs, f'Key \"transaction_number\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                transaction_number = rs['transaction_number']
                # assert transaction_number != ''
                print('Transaction number DPT_OPN: ', transaction_number)
            except:
                assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            
            # approve fixed deposit account
            fields_data = deposit_fo_payload.dpt_apr(
                account_number=account_number_new_prepaid_fixed_deposit_001,
                account_holder_name=account_name_prepaid_fixed_deposit,
                description=description_dpt_apr
            )
            try:
                rs = helper_fo_dpt.DPT_APR(fields_data)
                assert 'account_number' in rs, f'Key \"account_number\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                assert 'transaction_number' in rs, f'Key \"transaction_number\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                transaction_number = rs['transaction_number']
                # assert transaction_number != ''
                print('Transaction number DPT_APR: ', transaction_number)
            except:
                assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'

            # cash deposit
            fields_data = deposit_fo_payload.dpt_cdp(
                account_number=account_number_new_prepaid_fixed_deposit_001,
                amount_deposit=amount_deposit_fixed,
                amount=amount_deposit_fixed,
                currency_deposit=currency_code_mmk,
                values_date=working_date,
                customer_code='11056754',
                cash_amount_bcy=amount_deposit_fixed,
                cash_exchange_rate=exchange_rate,
                cash_amount=amount_deposit_fixed,
                cash_currency=currency_code_mmk,
                account_name=account_name_prepaid_fixed_deposit,
                exchange_rate=exchange_rate,
                cross_rate=exchange_rate,
                deposit_type=deposit_type_cash_fixed,
                id_issue_date=working_date,
                description=description_dpt_cdp
            )
            try:
                rs = helper_fo_dpt.DPT_CDP(fields_data)
                assert 'account_number' in rs, f'Key \"account_number\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                assert 'transaction_number' in rs, f'Key \"transaction_number\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                transaction_number = rs['transaction_number']
                # assert transaction_number != ''
                print('Transaction number DPT_CDP: ', transaction_number)
            except:
                assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            
            i += 1