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
working_date='2023-11-01' 
currency_code_mmk='MMK'
customer_code='11000003'

# data open savings deposit
catalog_code_saving_deposit='SAMMK0000'
catalog_name_saving_deposit='Savings account in MMK'
deposit_type_saving_deposit='Savings'
deposit_sub_type_saving_deposit='S1'
deposit_purpose_saving_deposit='P'
account_type_saving_deposit='1'
account_name_saving_deposit='test batch account linkage for prepaid FD by transfer 004'
rollover_saving_deposit='N'
auto_transfer_option_saving_deposit='N'
business_purpose_code=''
customer_type='C'
description_dpt_opn='1100: Open new deposit account'
# data open fixed deposit
catalog_code_prepaid_fd_transfer='PR120MMK1'
catalog_name_prepaid_fd_transfer='SHWE prepaid fixed deposit account by transfer in MMK'
deposit_type_prepaid_fd_transfer='Fixed Deposit'
deposit_sub_type_prepaid_fd_transfer='T6'
deposit_purpose_prepaid_fd_transfer='S'
account_type_prepaid_fd_transfer='1'
account_name_prepaid_fd_transfer='test batch prepaid FD by transfer 004'
rollover_prepaid_fd_transfer='N'
auto_transfer_option_prepaid_fd_transfer='A'

business_purpose_code=''
customer_type='C'
description_dpt_opn='1100: Open new deposit account'

# data approve deposit
description_dpt_apr='Approve deposit account'

# data cash deposit current
amount_deposit_current=700000000
exchange_rate=1
deposit_type_cash_current='C'
description_dpt_cdp='1110: Cash deposit'
description_dpt_cdp='1130: Transfer from deposit account to deposit account'

# data transfer fixed
amount_deposit_fixed=600000000
exchange_rate=1
deposit_type_cash_fixed='T'
description_dpt_trf='1130: Transfer from deposit account to deposit account'

@pytest.fixture(scope='session')
def user():
    user_service = USER_LOGIN['user4']
    req = RequestUtility(user_service)
    req.login_neptune()
    req.login_service()
    return req

@pytest.mark.open_deposit_account_for_batch
class TestOpenDepositAccountForBatch(object):

    @pytest.mark.open_deposit_account
    def test_004_open_deposit_account_prepaid_fd_004(self, user):
        helper_fo_dpt = DepositFOHelper(user)
        # open saving deposit account 
        global account_number_new_saving_deposit
        account_number_new_saving_deposit = ''
        fields_data = deposit_fo_payload.dpt_opn(
            customer_type=customer_type,
            customer_code=customer_code,
            catalog_code=catalog_code_saving_deposit,
            catalog_name=catalog_name_saving_deposit,
            deposit_type=deposit_type_saving_deposit,
            deposit_sub_type=deposit_sub_type_saving_deposit,
            deposit_purpose=deposit_purpose_saving_deposit,
            account_type=account_type_saving_deposit,
            account_name=account_name_saving_deposit,
            business_purpose_code=business_purpose_code,
            rollover=rollover_saving_deposit,
            auto_transfer_option=auto_transfer_option_saving_deposit,
            description=description_dpt_opn
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
            customer_code=customer_code,
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

        # open fixed deposit account 
        global account_number_new_prepaid_fd_transfer
        account_number_new_prepaid_fd_transfer = ''
        fields_data = deposit_fo_payload.dpt_opn(
            customer_type=customer_type,
            customer_code=customer_code,
            catalog_code=catalog_code_prepaid_fd_transfer,
            catalog_name=catalog_name_prepaid_fd_transfer,
            deposit_type=deposit_type_prepaid_fd_transfer,
            deposit_sub_type=deposit_sub_type_prepaid_fd_transfer,
            deposit_purpose=deposit_purpose_prepaid_fd_transfer,
            account_type=account_type_prepaid_fd_transfer,
            account_name=account_name_prepaid_fd_transfer,
            business_purpose_code=business_purpose_code,
            rollover=rollover_prepaid_fd_transfer,
            auto_transfer_option=auto_transfer_option_prepaid_fd_transfer,
            to_account_number=account_number_new_saving_deposit,
            description=description_dpt_opn
        )
        try:
            rs = helper_fo_dpt.DPT_OPN(fields_data)
            assert 'account_number' in rs, f'Key \"account_number\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            account_number_new_prepaid_fd_transfer = rs['account_number']
            assert 'transaction_number' in rs, f'Key \"transaction_number\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            transaction_number = rs['transaction_number']
            # assert transaction_number != ''
            print('Transaction number DPT_OPN: ', transaction_number)
        except:
            assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        
        # approve fixed deposit account
        fields_data = deposit_fo_payload.dpt_apr(
            account_number=account_number_new_prepaid_fd_transfer,
            account_holder_name=account_name_prepaid_fd_transfer,
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

        # deposit by transfer
        fields_data = deposit_fo_payload.dpt_trf(
            debit_account=account_number_new_saving_deposit,
            amount=amount_deposit_fixed,
            credit_account=account_number_new_prepaid_fd_transfer,
            t_exchange_rate_debit_account_bcy=exchange_rate,
            exchange_rate_credit_ac_bcy=exchange_rate,
            b_exchange_rate_debit_account_bcy=exchange_rate,
            debit_account_name=account_name_saving_deposit,
            credit_account_name=account_name_prepaid_fd_transfer,
            customer_code=customer_code,
            value_date=working_date,
            issue_date_of_debit=working_date,
            description=description_dpt_trf
        )
        try:
            rs = helper_fo_dpt.DPT_TRF(fields_data)
            assert 'credit_account' in rs, f'Key \"credit_account\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'transaction_number' in rs, f'Key \"transaction_number\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            transaction_number = rs['transaction_number']
            # assert transaction_number != ''
            print('Transaction number DPT_TRF: ', transaction_number)
        except:
            assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'